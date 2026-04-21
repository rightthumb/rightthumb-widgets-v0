#!/usr/bin/env bash

set -u
IFS=$'\n\t'

PC_VERSION="4.0.0"

###############################################################################
# MASTER STATE
###############################################################################

declare -Ag PC_STATE
declare -ag PC_SUMMARY

PC_SAVE_FILE=""
PC_SAVE_ONLY=0
PC_PRINT_ONLY=0

PC_LIST_DELIM=$'\n'

pc_state_reset() {
	PC_STATE=()
	PC_SUMMARY=()

	# scalar settings
	PC_STATE[version]="$PC_VERSION"
	PC_STATE[silent]="0"
	PC_STATE[force]="0"
	PC_STATE[dry_run]="0"
	PC_STATE[verbose]="0"
	PC_STATE[delay]="5"

	PC_STATE[recursive]="1"
	PC_STATE[follow_symlinks]="0"
	PC_STATE[allow_top]="0"

	PC_STATE[owner_spec]=""
	PC_STATE[group_spec]=""
	PC_STATE[owner_auto_fallback]=""
	PC_STATE[group_auto_fallback]=""

	PC_STATE[profile]=""
	PC_STATE[fix_777]="0"

	PC_STATE[dir_mode]=""
	PC_STATE[file_mode]=""
	PC_STATE[apply_setgid]="0"

	PC_STATE[clone_source]=""

	# list settings stored as newline-delimited strings
	PC_STATE[users]=""
	PC_STATE[paths]=""
	PC_STATE[files]=""
	PC_STATE[folders]=""
	PC_STATE[excludes]=""

	# ephemeral runtime flags, not saved
	PC_SAVE_FILE=""
	PC_SAVE_ONLY=0
	PC_PRINT_ONLY=0
}

###############################################################################
# BASIC UTILS
###############################################################################

pc_is_sourced() {
	[[ "${BASH_SOURCE[0]}" != "$0" ]]
}

pc_msg() {
	printf '%s\n' "$*"
}

pc_warn() {
	printf 'Warning: %s\n' "$*" >&2
}

pc_err() {
	printf 'Error: %s\n' "$*" >&2
}

pc_die() {
	pc_err "$*"
	return 1 2>/dev/null || exit 1
}

pc_verbose() {
	[[ "${PC_STATE[verbose]}" == "1" ]] && pc_msg "$*"
}

pc_add_summary() {
	PC_SUMMARY+=("$*")
}

pc_print_summary() {
	[[ "${#PC_SUMMARY[@]}" -eq 0 ]] && return 0
	pc_msg
	pc_msg "Summary:"
	local line
	for line in "${PC_SUMMARY[@]}"; do
		pc_msg "  - $line"
	done
}

pc_command_exists() {
	command -v "$1" >/dev/null 2>&1
}

pc_require_root() {
	if [[ "${EUID:-$(id -u)}" -ne 0 ]]; then
		pc_die "this tool must be run as root or with sudo"
	fi
}

pc_run() {
	if [[ "${PC_STATE[dry_run]}" == "1" ]]; then
		printf '[dry-run] '
		printf '%q ' "$@"
		printf '\n'
		return 0
	fi
	"$@"
}

pc_confirm() {
	local prompt="$1"
	local default="${2:-Y}"
	local reply

	if [[ "${PC_STATE[force]}" == "1" || "${PC_STATE[silent]}" == "1" ]]; then
		[[ "$default" =~ ^[Yy]$ ]] && return 0 || return 1
	fi

	if [[ "$default" =~ ^[Yy]$ ]]; then
		read -r -p "$prompt [Y/n]: " reply
		[[ -z "$reply" || "$reply" =~ ^[Yy]$ ]]
	else
		read -r -p "$prompt [y/N]: " reply
		[[ "$reply" =~ ^[Yy]$ ]]
	fi
}

pc_sleep_countdown() {
	local seconds="$1"
	[[ "$seconds" -le 0 ]] && return 0
	pc_msg
	pc_msg "Silent mode active."
	pc_msg "Starting in ${seconds} second(s). Press Ctrl+C to cancel."
	local i
	for (( i=seconds; i>=1; i-- )); do
		pc_msg "$i..."
		sleep 1
	done
}

pc_abs_path() {
	local p="$1"
	if pc_command_exists realpath; then
		realpath "$p" 2>/dev/null && return 0
	fi
	python3 - <<'PY' "$p" 2>/dev/null
import os, sys
print(os.path.abspath(sys.argv[1]))
PY
}

pc_is_switch() {
	local v="$1"
	[[ "$v" == -* ]]
}

pc_array_contains_prefix() {
	local item="$1"
	shift
	local parent
	for parent in "$@"; do
		[[ "$item" == "$parent" || "$item" == "$parent/"* ]] && return 0
	done
	return 1
}

###############################################################################
# LIST HELPERS FOR SINGLE MASTER ARRAY
###############################################################################

pc_list_get_lines() {
	local state_name="$1"
	local key="$2"
	local -n st="$state_name"
	[[ -n "${st[$key]}" ]] && printf '%s\n' "${st[$key]}"
}

pc_list_to_array() {
	local state_name="$1"
	local key="$2"
	local out_name="$3"
	local -n st="$state_name"
	local -n out="$out_name"

	out=()
	[[ -n "${st[$key]}" ]] || return 0

	while IFS= read -r line; do
		[[ -n "$line" ]] && out+=("$line")
	done <<< "${st[$key]}"
}

pc_list_add() {
	local state_name="$1"
	local key="$2"
	shift 2
	local -n st="$state_name"
	local item

	for item in "$@"; do
		[[ -n "$item" ]] || continue
		if [[ -z "${st[$key]}" ]]; then
			st[$key]="$item"
		else
			st[$key]+="${PC_LIST_DELIM}${item}"
		fi
	done
}

pc_list_set_from_array() {
	local state_name="$1"
	local key="$2"
	local src_name="$3"
	local -n st="$state_name"
	local -n src="$src_name"

	st[$key]=""
	local item
	for item in "${src[@]}"; do
		[[ -n "$item" ]] || continue
		if [[ -z "${st[$key]}" ]]; then
			st[$key]="$item"
		else
			st[$key]+="${PC_LIST_DELIM}${item}"
		fi
	done
}

pc_array_dedupe() {
	local src_name="$1"
	local dst_name="$2"
	local -n src="$src_name"
	local -n dst="$dst_name"
	declare -A seen=()
	local item

	dst=()
	for item in "${src[@]}"; do
		[[ -n "$item" ]] || continue
		if [[ -z "${seen[$item]+x}" ]]; then
			seen["$item"]=1
			dst+=("$item")
		fi
	done
}

pc_state_dedupe_lists() {
	local state_name="$1"
	local key arr deduped
	local -a arr deduped

	for key in users paths files folders excludes; do
		pc_list_to_array "$state_name" "$key" arr
		pc_array_dedupe arr deduped
		pc_list_set_from_array "$state_name" "$key" deduped
	done
}

###############################################################################
# SYSTEM LOOKUPS
###############################################################################

pc_user_exists() {
	local user="$1"
	if pc_command_exists getent; then
		getent passwd "$user" >/dev/null 2>&1
	else
		grep -q "^${user}:" /etc/passwd 2>/dev/null
	fi
}

pc_group_exists() {
	local group="$1"
	if pc_command_exists getent; then
		getent group "$group" >/dev/null 2>&1
	else
		grep -q "^${group}:" /etc/group 2>/dev/null
	fi
}

pc_list_users() {
	if pc_command_exists getent; then
		getent passwd | cut -d: -f1 | sort
	else
		cut -d: -f1 /etc/passwd | sort
	fi
}

pc_list_groups() {
	if pc_command_exists getent; then
		getent group | cut -d: -f1 | sort
	else
		cut -d: -f1 /etc/group | sort
	fi
}

pc_user_primary_group() {
	local user="$1"
	id -gn "$user" 2>/dev/null || true
}

pc_stat_owner() {
	local path="$1"
	stat -c '%U' "$path" 2>/dev/null || stat -f '%Su' "$path" 2>/dev/null
}

pc_stat_group() {
	local path="$1"
	stat -c '%G' "$path" 2>/dev/null || stat -f '%Sg' "$path" 2>/dev/null
}

pc_stat_mode_octal() {
	local path="$1"
	stat -c '%a' "$path" 2>/dev/null || stat -f '%Mp%Lp' "$path" 2>/dev/null
}

pc_stat_mode_symbolic() {
	local path="$1"
	stat -c '%A' "$path" 2>/dev/null || ls -ld "$path" | awk '{print $1}'
}

pc_stat_type() {
	local path="$1"
	if [[ -L "$path" ]]; then
		printf 'symlink\n'
	elif [[ -d "$path" ]]; then
		printf 'dir\n'
	elif [[ -f "$path" ]]; then
		printf 'file\n'
	else
		printf 'other\n'
	fi
}

###############################################################################
# JSON SAVE / LOAD
###############################################################################

pc_state_export_json() {
	local state_name="$1"
	local file="$2"
	local -n st="$state_name"
	[[ -n "$file" ]] || return 0

	local dir
	dir="$(dirname "$file")"
	[[ ! -d "$dir" ]] && pc_run mkdir -p "$dir"

	export PC_JSON_OUT="$file"
	export PCJ_version="${st[version]}"
	export PCJ_silent="${st[silent]}"
	export PCJ_force="${st[force]}"
	export PCJ_dry_run="${st[dry_run]}"
	export PCJ_verbose="${st[verbose]}"
	export PCJ_delay="${st[delay]}"
	export PCJ_recursive="${st[recursive]}"
	export PCJ_follow_symlinks="${st[follow_symlinks]}"
	export PCJ_allow_top="${st[allow_top]}"
	export PCJ_owner_spec="${st[owner_spec]}"
	export PCJ_group_spec="${st[group_spec]}"
	export PCJ_owner_auto_fallback="${st[owner_auto_fallback]}"
	export PCJ_group_auto_fallback="${st[group_auto_fallback]}"
	export PCJ_profile="${st[profile]}"
	export PCJ_fix_777="${st[fix_777]}"
	export PCJ_dir_mode="${st[dir_mode]}"
	export PCJ_file_mode="${st[file_mode]}"
	export PCJ_apply_setgid="${st[apply_setgid]}"
	export PCJ_clone_source="${st[clone_source]}"
	export PCJ_users="${st[users]}"
	export PCJ_paths="${st[paths]}"
	export PCJ_files="${st[files]}"
	export PCJ_folders="${st[folders]}"
	export PCJ_excludes="${st[excludes]}"

	if [[ "${st[dry_run]}" == "1" ]]; then
		pc_msg "[dry-run] would write json state to $file"
		return 0
	fi

	python3 - <<'PY'
import json, os

def split_lines(value: str):
	if not value:
		return []
	return [line for line in value.splitlines() if line]

data = {
	"version": os.environ.get("PCJ_version", ""),
	"settings": {
		"silent": os.environ.get("PCJ_silent", "0"),
		"force": os.environ.get("PCJ_force", "0"),
		"dry_run": os.environ.get("PCJ_dry_run", "0"),
		"verbose": os.environ.get("PCJ_verbose", "0"),
		"delay": os.environ.get("PCJ_delay", "5"),
		"recursive": os.environ.get("PCJ_recursive", "1"),
		"follow_symlinks": os.environ.get("PCJ_follow_symlinks", "0"),
		"allow_top": os.environ.get("PCJ_allow_top", "0"),
		"owner_spec": os.environ.get("PCJ_owner_spec", ""),
		"group_spec": os.environ.get("PCJ_group_spec", ""),
		"owner_auto_fallback": os.environ.get("PCJ_owner_auto_fallback", ""),
		"group_auto_fallback": os.environ.get("PCJ_group_auto_fallback", ""),
		"profile": os.environ.get("PCJ_profile", ""),
		"fix_777": os.environ.get("PCJ_fix_777", "0"),
		"dir_mode": os.environ.get("PCJ_dir_mode", ""),
		"file_mode": os.environ.get("PCJ_file_mode", ""),
		"apply_setgid": os.environ.get("PCJ_apply_setgid", "0"),
		"clone_source": os.environ.get("PCJ_clone_source", ""),
	},
	"lists": {
		"users": split_lines(os.environ.get("PCJ_users", "")),
		"paths": split_lines(os.environ.get("PCJ_paths", "")),
		"files": split_lines(os.environ.get("PCJ_files", "")),
		"folders": split_lines(os.environ.get("PCJ_folders", "")),
		"excludes": split_lines(os.environ.get("PCJ_excludes", "")),
	}
}

with open(os.environ["PC_JSON_OUT"], "w", encoding="utf-8") as fh:
	json.dump(data, fh, indent=2, sort_keys=True)
	fh.write("\n")
PY
}


pc_state_import_json() {
	local state_name="$1"
	local file="$2"
	local -n st="$state_name"
	[[ -f "$file" ]] || pc_die "profile file not found: $file"

	local pyout
	pyout="$(
		python3 - <<'PY' "$file"
import json, shlex, sys

p = sys.argv[1]
with open(p, "r", encoding="utf-8") as fh:
	data = json.load(fh)

settings = data.get("settings", {})
lists = data.get("lists", {})

scalar_keys = [
	"silent",
	"force",
	"dry_run",
	"verbose",
	"delay",
	"recursive",
	"follow_symlinks",
	"allow_top",
	"owner_spec",
	"group_spec",
	"owner_auto_fallback",
	"group_auto_fallback",
	"profile",
	"fix_777",
	"dir_mode",
	"file_mode",
	"apply_setgid",
	"clone_source",
]

for key in scalar_keys:
	value = settings.get(key, "")
	if value is None:
		value = ""
	print(f'SCALAR\t{key}\t{value}')

for key in ("users", "paths", "files", "folders", "excludes"):
	arr = lists.get(key, [])
	if not isinstance(arr, list):
		arr = []
	quoted = " ".join(shlex.quote(str(x)) for x in arr)
	print(f'LIST\t{key}\t{quoted}')
PY
	)"

	local line kind key payload
	local -a tmp_arr=()

	while IFS= read -r line; do
		[[ -n "$line" ]] || continue

		kind="${line%%$'\t'*}"
		payload="${line#*$'\t'}"
		key="${payload%%$'\t'*}"
		payload="${payload#*$'\t'}"

		case "$kind" in
			SCALAR)
				st["$key"]="$payload"
				;;
			LIST)
				tmp_arr=()
				if [[ -n "$payload" ]]; then
					eval "tmp_arr=($payload)"
				fi
				pc_list_set_from_array "$state_name" "$key" tmp_arr
				;;
		esac
	done <<< "$pyout"

	pc_add_summary "loaded profile from $file"
}


pc_state_import_json000() {
	local state_name="$1"
	local file="$2"
	local -n st="$state_name"
	[[ -f "$file" ]] || pc_die "profile file not found: $file"

	local line key val
	while IFS=$'\t' read -r key val; do
		case "$key" in
			users|paths|files|folders|excludes)
				st["$key"]="$val"
				;;
			*)
				st["$key"]="$val"
				;;
		esac
	done < <(
		python3 - <<'PY' "$file"
import json, sys
p = sys.argv[1]
with open(p, "r", encoding="utf-8") as fh:
	data = json.load(fh)

settings = data.get("settings", {})
lists = data.get("lists", {})

for key, value in settings.items():
	if value is None:
		value = ""
	print(f"{key}\t{value}")

for key in ("users", "paths", "files", "folders", "excludes"):
	value = lists.get(key, [])
	if not isinstance(value, list):
		value = []
	print(f"{key}\t" + "\n".join(str(x) for x in value if str(x)))
PY
	)

	pc_add_summary "loaded profile from $file"
}

###############################################################################
# HELP
###############################################################################

pc_help() {
	cat <<'EOF'
PermCore.sh - Smart owner / group / permission manager

SWITCH MAPPING

  Single-value settings:
	-o,  -owner            -> owner_spec
	-g,  -group            -> group_spec
	-delay                 -> delay
	-dm, -dir-mode         -> dir_mode
	-fm, -file-mode        -> file_mode
	-clone                 -> clone_source
	-web                   -> profile=web
	-default               -> profile=default
	-x                     -> profile=x
	-7                     -> profile=7
	-777                   -> fix_777=1
	-silent                -> silent=1
	-force                 -> force=1
	-dry-run               -> dry_run=1
	-verbose               -> verbose=1
	-no-recursive          -> recursive=0
	-follow-symlinks       -> follow_symlinks=1
	-allow-top             -> allow_top=1

  Multi-value settings:
	-u,  -users            -> users[]
	-p,  -paths            -> paths[]
	-f,  -files            -> files[]
	-d,  -folders          -> folders[]
	-e,  -exclude          -> excludes[]

SAVE / LOAD

  -load FILE
	processed first, before any output

  -save FILE
	saves final resolved state as JSON and quits

  -print
	prints final resolved state and quits
	never saved

EXAMPLES

  per -g sds -u user1 user2
  per -load /opt/base.permcore.json -u user3
  per -load /opt/base.permcore.json -p /home/user1/public_html /opt/shared
  per -load /opt/base.permcore.json -g wheel -save /opt/modified.permcore.json
  per -load /opt/base.permcore.json -print

EOF
}

###############################################################################
# PROFILE / CLONE
###############################################################################

pc_apply_profile() {
	local state_name="$1"
	local profile="$2"
	local -n st="$state_name"

	st[profile]="$profile"

	case "$profile" in
		web)
			st[dir_mode]="755"
			st[file_mode]="644"
			st[apply_setgid]="0"
			;;
		default)
			st[dir_mode]="2770"
			st[file_mode]="660"
			st[apply_setgid]="1"
			;;
		x)
			st[dir_mode]="755"
			st[file_mode]="755"
			st[apply_setgid]="0"
			;;
		7)
			st[dir_mode]="777"
			st[file_mode]="777"
			st[apply_setgid]="0"
			;;
		*)
			pc_die "unknown profile: $profile"
			;;
	esac
}

pc_clone_from_path() {
	local state_name="$1"
	local ref="$2"
	local -n st="$state_name"

	[[ -e "$ref" ]] || pc_die "clone source not found: $ref"

	st[clone_source]="$ref"

	[[ -z "${st[owner_spec]}" ]] && st[owner_spec]="$(pc_stat_owner "$ref")"
	[[ -z "${st[group_spec]}" ]] && st[group_spec]="$(pc_stat_group "$ref")"

	if [[ -d "$ref" ]]; then
		[[ -z "${st[dir_mode]}" ]] && st[dir_mode]="$(pc_stat_mode_octal "$ref")"
		[[ -z "${st[file_mode]}" ]] && st[file_mode]="644"
	else
		[[ -z "${st[file_mode]}" ]] && st[file_mode]="$(pc_stat_mode_octal "$ref")"
		if [[ -z "${st[dir_mode]}" ]]; then
			local parent
			parent="$(dirname "$ref")"
			if [[ -d "$parent" ]]; then
				st[dir_mode]="$(pc_stat_mode_octal "$parent")"
			else
				st[dir_mode]="755"
			fi
		fi
	fi

	[[ "${st[dir_mode]}" == 2* ]] && st[apply_setgid]="1"
	pc_add_summary "cloned settings from $ref"
}

###############################################################################
# ARG PARSER
###############################################################################

pc_need_value() {
	local i="$1"
	local total="$2"
	[[ "$i" -lt "$total" ]] || pc_die "missing required value"
}

pc_collect_multi_values() {
	local state_name="$1"
	local list_key="$2"
	shift 2
	local -n argv_ref="$1"
	shift
	local -n idx_ref="$1"
	local count="${#argv_ref[@]}"
	local consumed=0
	local values=()

	while [[ "$idx_ref" -lt "$count" ]]; do
		if pc_is_switch "${argv_ref[$idx_ref]}"; then
			break
		fi
		values+=("${argv_ref[$idx_ref]}")
		((idx_ref++))
		consumed=1
	done

	[[ "$consumed" -eq 1 ]] || pc_die "switch requires one or more values"
	pc_list_add "$state_name" "$list_key" "${values[@]}"
}

pc_preload_profiles() {
	local state_name="$1"
	shift
	local -n st="$state_name"
	local argv=("$@")
	local i=0
	local total="${#argv[@]}"

	while [[ "$i" -lt "$total" ]]; do
		case "${argv[$i]}" in
			-load)
				((i++))
				pc_need_value "$i" "$total"
				pc_state_import_json "$state_name" "${argv[$i]}"
				;;
		esac
		((i++))
	done
}

pc_parse_args() {
	local state_name="$1"
	shift
	local -n st="$state_name"
	local argv=("$@")
	local i=0
	local total="${#argv[@]}"
	local arg

	[[ "$total" -gt 0 ]] || {
		pc_help
		return 1
	}

	pc_preload_profiles "$state_name" "${argv[@]}"

	while [[ "$i" -lt "$total" ]]; do
		arg="${argv[$i]}"

		case "$arg" in
			-h|--help)
				pc_help
				return 1
				;;

			-silent)
				st[silent]="1"
				;;

			-force)
				st[force]="1"
				;;

			-dry-run)
				st[dry_run]="1"
				;;

			-verbose)
				st[verbose]="1"
				;;

			-delay)
				((i++))
				pc_need_value "$i" "$total"
				[[ "${argv[$i]}" =~ ^[0-9]+$ ]] || pc_die "-delay must be an integer"
				st[delay]="${argv[$i]}"
				;;

			-no-recursive)
				st[recursive]="0"
				;;

			-follow-symlinks)
				st[follow_symlinks]="1"
				;;

			-allow-top)
				st[allow_top]="1"
				;;

			-web)
				pc_apply_profile "$state_name" "web"
				;;

			-default)
				pc_apply_profile "$state_name" "default"
				;;

			-x)
				pc_apply_profile "$state_name" "x"
				;;

			-7)
				pc_apply_profile "$state_name" "7"
				;;

			-777)
				st[fix_777]="1"
				;;

			-dm|-dir-mode)
				((i++))
				pc_need_value "$i" "$total"
				[[ "${argv[$i]}" =~ ^[0-7]{3,4}$ ]] || pc_die "invalid dir mode: ${argv[$i]}"
				st[dir_mode]="${argv[$i]}"
				;;

			-fm|-file-mode)
				((i++))
				pc_need_value "$i" "$total"
				[[ "${argv[$i]}" =~ ^[0-7]{3,4}$ ]] || pc_die "invalid file mode: ${argv[$i]}"
				st[file_mode]="${argv[$i]}"
				;;

			-o|-owner)
				((i++))
				pc_need_value "$i" "$total"
				st[owner_spec]="${argv[$i]}"
				;;

			-g|-group)
				((i++))
				pc_need_value "$i" "$total"
				st[group_spec]="${argv[$i]}"
				;;

			-save)
				((i++))
				pc_need_value "$i" "$total"
				PC_SAVE_FILE="${argv[$i]}"
				PC_SAVE_ONLY=1
				;;

			-load)
				((i++))
				pc_need_value "$i" "$total"
				;;

			-clone)
				((i++))
				pc_need_value "$i" "$total"
				pc_clone_from_path "$state_name" "${argv[$i]}"
				;;

			-print)
				PC_PRINT_ONLY=1
				;;

			-u|-users)
				((i++))
				pc_collect_multi_values "$state_name" "users" argv i
				((i--))
				;;

			-p|-paths)
				((i++))
				pc_collect_multi_values "$state_name" "paths" argv i
				((i--))
				;;

			-f|-files)
				((i++))
				pc_collect_multi_values "$state_name" "files" argv i
				((i--))
				;;

			-d|-folders)
				((i++))
				pc_collect_multi_values "$state_name" "folders" argv i
				((i--))
				;;

			-e|-exclude)
				((i++))
				pc_collect_multi_values "$state_name" "excludes" argv i
				((i--))
				;;

			-list-users)
				pc_list_users
				return 1
				;;

			-list-groups)
				pc_list_groups
				return 1
				;;

			-list-users-groups)
				local user
				while IFS= read -r user; do
					printf '%s: %s\n' "$user" "$(id -nG "$user" 2>/dev/null || true)"
				done < <(pc_list_users)
				return 1
				;;

			-list-group)
				((i++))
				pc_need_value "$i" "$total"
				pc_list_group_members "${argv[$i]}"
				return 1
				;;

			-folder)
				((i++))
				pc_need_value "$i" "$total"
				pc_show_path_info "${argv[$i]}"
				return 1
				;;

			-folder-files)
				((i++))
				pc_need_value "$i" "$total"
				pc_show_folder_children "${argv[$i]}"
				return 1
				;;

			*)
				pc_die "unknown switch or unexpected positional value: $arg"
				;;
		esac

		((i++))
	done

	if [[ "${st[force]}" == "1" ]]; then
		st[silent]="0"
	fi
}

###############################################################################
# INSPECTION
###############################################################################

pc_show_path_info() {
	local path="$1"
	[[ -e "$path" || -L "$path" ]] || pc_die "path not found: $path"

	printf '%s | type=%s | owner=%s | group=%s | mode=%s | perms=%s\n' \
		"$path" \
		"$(pc_stat_type "$path")" \
		"$(pc_stat_owner "$path")" \
		"$(pc_stat_group "$path")" \
		"$(pc_stat_mode_octal "$path")" \
		"$(pc_stat_mode_symbolic "$path")"
}

pc_show_folder_children() {
	local path="$1"
	[[ -d "$path" ]] || pc_die "not a directory: $path"

	pc_show_path_info "$path"
	pc_msg "Children:"
	while IFS= read -r item; do
		pc_show_path_info "$item"
	done < <(find "$path" -mindepth 1 -maxdepth 1 -print 2>/dev/null | sort)
}

pc_list_group_members() {
	local group="$1"
	pc_group_exists "$group" || pc_die "group not found: $group"

	local user primary_gid target_gid found=0
	target_gid="$(getent group "$group" | cut -d: -f3 2>/dev/null || true)"

	pc_msg "Group: $group"
	pc_msg "Users:"

	while IFS= read -r user; do
		if id -nG "$user" 2>/dev/null | tr ' ' '\n' | grep -qx "$group"; then
			printf '  %s\n' "$user"
			found=1
		else
			primary_gid="$(id -g "$user" 2>/dev/null || true)"
			if [[ -n "$target_gid" && "$primary_gid" == "$target_gid" ]]; then
				printf '  %s\n' "$user"
				found=1
			fi
		fi
	done < <(pc_list_users)

	[[ "$found" -eq 0 ]] && pc_msg "  (none found)"
}

###############################################################################
# TARGET MERGING / SAFETY
###############################################################################

pc_get_effective_paths() {
	local state_name="$1"
	local out_name="$2"
	local -n st="$state_name"
	local -n out="$out_name"

	local -a paths=() files=() folders=() merged=() deduped=()
	pc_list_to_array "$state_name" "paths" paths
	pc_list_to_array "$state_name" "files" files
	pc_list_to_array "$state_name" "folders" folders

	merged=("${paths[@]}" "${files[@]}" "${folders[@]}")
	pc_array_dedupe merged deduped
	out=("${deduped[@]}")
}

pc_path_is_excluded() {
	local state_name="$1"
	local path="$2"
	local -a excludes
	pc_list_to_array "$state_name" "excludes" excludes

	local ex
	for ex in "${excludes[@]}"; do
		[[ "$path" == "$ex" || "$path" == "$ex/"* ]] && return 0
	done
	return 1
}

pc_is_dangerous_recursive_target() {
	local path="$1"
	local abs
	abs="$(pc_abs_path "$path" 2>/dev/null || printf '%s' "$path")"

	case "$abs" in
		/|/home|/usr|/etc|/var|/bin|/sbin|/lib|/lib64|/boot|/root)
			return 0
			;;
	esac
	return 1
}

pc_validate_safe_targets() {
	local state_name="$1"
	local -n st="$state_name"

	[[ "${st[recursive]}" == "1" ]] || return 0
	[[ "${st[allow_top]}" == "1" ]] && return 0

	local -a paths=()
	pc_get_effective_paths "$state_name" paths

	local path
	for path in "${paths[@]}"; do
		if pc_is_dangerous_recursive_target "$path"; then
			pc_die "refusing recursive operation on dangerous top-level target: $(pc_abs_path "$path" 2>/dev/null || printf '%s' "$path"). use -allow-top if you truly mean it"
		fi
	done
}

###############################################################################
# AUTO RESOLUTION
###############################################################################

pc_infer_owner_from_path() {
	local path="$1"
	local abs second
	abs="$(pc_abs_path "$path" 2>/dev/null || printf '%s' "$path")"

	case "$abs" in
		/home/*)
			second="$(printf '%s\n' "$abs" | cut -d/ -f3)"
			if [[ -n "$second" ]] && pc_user_exists "$second"; then
				printf '%s\n' "$second"
				return 0
			fi
			;;
	esac

	return 1
}

pc_infer_group_from_path() {
	local path="$1"
	local owner
	owner="$(pc_infer_owner_from_path "$path" 2>/dev/null || true)"
	if [[ -n "$owner" ]] && pc_user_exists "$owner"; then
		pc_user_primary_group "$owner"
		return 0
	fi
	return 1
}

pc_collect_auto_questions() {
	local state_name="$1"
	local -n st="$state_name"

	[[ "${st[force]}" == "1" || "${st[silent]}" == "1" ]] && return 0

	local -a paths=()
	pc_get_effective_paths "$state_name" paths
	[[ "${#paths[@]}" -gt 0 ]] || return 0

	local need_owner_prompt=0
	local need_group_prompt=0
	local path abs second

	if [[ "${st[owner_spec]}" == "auto" ]]; then
		for path in "${paths[@]}"; do
			abs="$(pc_abs_path "$path" 2>/dev/null || printf '%s' "$path")"
			if [[ "$abs" == /home/* ]]; then
				second="$(printf '%s\n' "$abs" | cut -d/ -f3)"
				if [[ -n "$second" ]] && ! pc_user_exists "$second"; then
					need_owner_prompt=1
					break
				fi
			fi
		done
	fi

	if [[ "${st[group_spec]}" == "auto" ]]; then
		for path in "${paths[@]}"; do
			abs="$(pc_abs_path "$path" 2>/dev/null || printf '%s' "$path")"
			if [[ "$abs" == /home/* ]]; then
				second="$(printf '%s\n' "$abs" | cut -d/ -f3)"
				if [[ -n "$second" ]] && ! pc_user_exists "$second"; then
					need_group_prompt=1
					break
				fi
			fi
		done
	fi

	if [[ "$need_owner_prompt" -eq 1 ]]; then
		read -r -p "Owner auto could not infer for one or more /home/<folder>/ paths. Enter fallback owner (blank = keep current owner): " st[owner_auto_fallback]
		if [[ -n "${st[owner_auto_fallback]}" ]]; then
			pc_user_exists "${st[owner_auto_fallback]}" || pc_die "fallback owner does not exist: ${st[owner_auto_fallback]}"
		fi
	fi

	if [[ "$need_group_prompt" -eq 1 ]]; then
		read -r -p "Group auto could not infer for one or more /home/<folder>/ paths. Enter fallback group (blank = keep current group): " st[group_auto_fallback]
		if [[ -n "${st[group_auto_fallback]}" ]]; then
			if ! pc_group_exists "${st[group_auto_fallback]}"; then
				pc_msg "Creating group: ${st[group_auto_fallback]}"
				pc_run groupadd "${st[group_auto_fallback]}"
			fi
		fi
	fi
}

pc_resolve_owner_for_path() {
	local state_name="$1"
	local path="$2"
	local -n st="$state_name"

	if [[ -z "${st[owner_spec]}" ]]; then
		printf '\n'
		return 0
	fi

	if [[ "${st[owner_spec]}" != "auto" ]]; then
		printf '%s\n' "${st[owner_spec]}"
		return 0
	fi

	local inferred
	inferred="$(pc_infer_owner_from_path "$path" 2>/dev/null || true)"
	if [[ -n "$inferred" ]]; then
		printf '%s\n' "$inferred"
		return 0
	fi

	if [[ -n "${st[owner_auto_fallback]}" ]]; then
		printf '%s\n' "${st[owner_auto_fallback]}"
		return 0
	fi

	printf '\n'
}

pc_resolve_group_for_path() {
	local state_name="$1"
	local path="$2"
	local -n st="$state_name"

	if [[ -z "${st[group_spec]}" ]]; then
		printf '\n'
		return 0
	fi

	if [[ "${st[group_spec]}" != "auto" ]]; then
		printf '%s\n' "${st[group_spec]}"
		return 0
	fi

	local inferred
	inferred="$(pc_infer_group_from_path "$path" 2>/dev/null || true)"
	if [[ -n "$inferred" ]]; then
		printf '%s\n' "$inferred"
		return 0
	fi

	if [[ -n "${st[group_auto_fallback]}" ]]; then
		printf '%s\n' "${st[group_auto_fallback]}"
		return 0
	fi

	printf '\n'
}

###############################################################################
# VALIDATION
###############################################################################

pc_validate_config() {
	local state_name="$1"
	local -n st="$state_name"

	if [[ -n "${st[owner_spec]}" && "${st[owner_spec]}" != "auto" ]]; then
		pc_user_exists "${st[owner_spec]}" || pc_die "owner does not exist: ${st[owner_spec]}"
	fi

	if [[ -n "${st[group_spec]}" && "${st[group_spec]}" != "auto" ]]; then
		if ! pc_group_exists "${st[group_spec]}"; then
			pc_msg "Creating group: ${st[group_spec]}"
			pc_run groupadd "${st[group_spec]}"
			pc_add_summary "created group ${st[group_spec]}"
		fi
	fi

	local -a users
	pc_list_to_array "$state_name" "users" users
	if [[ "${#users[@]}" -gt 0 ]]; then
		[[ -n "${st[group_spec]}" ]] || pc_die "user operations require -group NAME"
		[[ "${st[group_spec]}" != "auto" ]] || pc_die "user operations cannot use -group auto"
	fi

	if [[ "${st[fix_777]}" == "1" && -z "${st[profile]}" && -z "${st[dir_mode]}" && -z "${st[file_mode]}" ]]; then
		pc_apply_profile "$state_name" "default"
	fi

	pc_state_dedupe_lists "$state_name"

	local -a paths=()
	pc_get_effective_paths "$state_name" paths
	if [[ "${st[fix_777]}" == "1" && "${#paths[@]}" -eq 0 ]]; then
		pc_list_add "$state_name" "paths" "."
	fi

	pc_validate_safe_targets "$state_name"
}

###############################################################################
# PLAN PRINTING
###############################################################################

pc_show_plan() {
	local state_name="$1"
	local should_ask="${2:-0}"
	local mode="${3:-run}"
	local -n st="$state_name"

	local label="Execution plan"
	[[ "$mode" == "save" ]] && label="Save plan"
	[[ "$mode" == "print" ]] && label="Print plan"

	pc_msg
	pc_msg "${label}:"
	pc_msg "  owner spec:      ${st[owner_spec]:-unchanged}"
	pc_msg "  group spec:      ${st[group_spec]:-unchanged}"
	pc_msg "  profile:         ${st[profile]:-none}"
	pc_msg "  dir mode:        ${st[dir_mode]:-unchanged}"
	pc_msg "  file mode:       ${st[file_mode]:-unchanged}"
	pc_msg "  fix exact 777:   ${st[fix_777]}"
	pc_msg "  recursive:       ${st[recursive]}"
	pc_msg "  follow symlinks: ${st[follow_symlinks]}"
	pc_msg "  dry-run:         ${st[dry_run]}"
	pc_msg "  silent:          ${st[silent]}"
	pc_msg "  force:           ${st[force]}"
	pc_msg "  delay:           ${st[delay]}"
	[[ -n "${st[clone_source]}" ]] && pc_msg "  clone source:    ${st[clone_source]}"
	[[ -n "$PC_SAVE_FILE" ]] && pc_msg "  save file:       $PC_SAVE_FILE"

	local -a users paths files folders excludes effective
	pc_list_to_array "$state_name" "users" users
	pc_list_to_array "$state_name" "paths" paths
	pc_list_to_array "$state_name" "files" files
	pc_list_to_array "$state_name" "folders" folders
	pc_list_to_array "$state_name" "excludes" excludes
	pc_get_effective_paths "$state_name" effective

	if [[ "${#users[@]}" -gt 0 ]]; then
		pc_msg "  users:"
		printf '    %s\n' "${users[@]}"
	fi

	if [[ "${#paths[@]}" -gt 0 ]]; then
		pc_msg "  paths:"
		printf '    %s\n' "${paths[@]}"
	fi

	if [[ "${#files[@]}" -gt 0 ]]; then
		pc_msg "  files:"
		printf '    %s\n' "${files[@]}"
	fi

	if [[ "${#folders[@]}" -gt 0 ]]; then
		pc_msg "  folders:"
		printf '    %s\n' "${folders[@]}"
	fi

	if [[ "${#effective[@]}" -gt 0 ]]; then
		pc_msg "  effective targets:"
		local p ro rg
		for p in "${effective[@]}"; do
			ro="$(pc_resolve_owner_for_path "$state_name" "$p")"
			rg="$(pc_resolve_group_for_path "$state_name" "$p")"
			pc_msg "    $(pc_abs_path "$p" 2>/dev/null || printf '%s' "$p") | owner=${ro:-unchanged} | group=${rg:-unchanged}"
		done
	fi

	if [[ "${#excludes[@]}" -gt 0 ]]; then
		pc_msg "  excludes:"
		printf '    %s\n' "${excludes[@]}"
	fi

	pc_msg

	if [[ "$should_ask" == "1" ]]; then
		if ! pc_confirm "Continue?" "Y"; then
			pc_msg "Cancelled."
			return 1
		fi
	fi

	return 0
}

###############################################################################
# EXECUTION
###############################################################################

pc_add_user_to_group_if_needed() {
	local user="$1"
	local group="$2"

	pc_user_exists "$user" || pc_die "user does not exist: $user"

	if id -nG "$user" 2>/dev/null | tr ' ' '\n' | grep -qx "$group"; then
		pc_verbose "user '$user' already in group '$group'"
		return 0
	fi

	pc_msg "Adding user '$user' to group '$group'"
	pc_run usermod -a -G "$group" "$user"
	pc_add_summary "added user $user to group $group"
}

pc_execute_user_operations() {
	local state_name="$1"
	local -n st="$state_name"

	local -a users
	pc_list_to_array "$state_name" "users" users
	[[ "${#users[@]}" -gt 0 ]] || return 0

	local user
	for user in "${users[@]}"; do
		pc_add_user_to_group_if_needed "$user" "${st[group_spec]}"
	done
}

pc_apply_owner_group_single() {
	local path="$1"
	local owner="$2"
	local group="$3"

	[[ -n "$owner" ]] && pc_run chown "$owner" "$path"
	[[ -n "$group" ]] && pc_run chgrp "$group" "$path"
}

pc_apply_mode_single() {
	local state_name="$1"
	local path="$2"
	local -n st="$state_name"

	if [[ -d "$path" ]]; then
		[[ -n "${st[dir_mode]}" ]] && pc_run chmod "${st[dir_mode]}" "$path"
	elif [[ -f "$path" ]]; then
		[[ -n "${st[file_mode]}" ]] && pc_run chmod "${st[file_mode]}" "$path"
	fi
}

pc_apply_to_single_path() {
	local state_name="$1"
	local path="$2"

	local owner group
	owner="$(pc_resolve_owner_for_path "$state_name" "$path")"
	group="$(pc_resolve_group_for_path "$state_name" "$path")"

	pc_apply_owner_group_single "$path" "$owner" "$group"
	pc_apply_mode_single "$state_name" "$path"
}

pc_apply_tree() {
	local state_name="$1"
	local root="$2"
	local -n st="$state_name"

	[[ -e "$root" || -L "$root" ]] || pc_die "path not found: $root"

	if pc_path_is_excluded "$state_name" "$root"; then
		pc_verbose "excluded: $root"
		return 0
	fi

	if [[ "${st[recursive]}" == "0" || ! -d "$root" ]]; then
		pc_apply_to_single_path "$state_name" "$root"
		pc_add_summary "applied settings to $root"
		return 0
	fi

	if [[ -L "$root" && "${st[follow_symlinks]}" == "0" ]]; then
		pc_verbose "skipping symlink root: $root"
		return 0
	fi

	local find_cmd=(find)
	[[ "${st[follow_symlinks]}" == "1" ]] && find_cmd+=(-L)
	find_cmd+=("$root" -print)

	while IFS= read -r item; do
		pc_path_is_excluded "$state_name" "$item" && continue
		[[ -L "$item" && "${st[follow_symlinks]}" == "0" ]] && continue
		pc_apply_to_single_path "$state_name" "$item"
	done < <("${find_cmd[@]}" 2>/dev/null)

	pc_add_summary "applied settings recursively to $root"
}

pc_fix_exact_777_under_root() {
	local state_name="$1"
	local root="$2"
	local -n st="$state_name"

	[[ -d "$root" ]] || pc_die "-777 requires directory targets; not a directory: $root"

	local item mode
	local fixed_dirs=()

	while IFS= read -r item; do
		pc_path_is_excluded "$state_name" "$item" && continue
		[[ -L "$item" && "${st[follow_symlinks]}" == "0" ]] && continue

		if pc_array_contains_prefix "$item" "${fixed_dirs[@]}"; then
			continue
		fi

		mode="$(pc_stat_mode_octal "$item")"
		if [[ "$mode" == "777" ]]; then
			if [[ -d "$item" ]]; then
				pc_msg "Fixing 777 directory tree: $item"
				local old_recursive="${st[recursive]}"
				st[recursive]="1"
				pc_apply_tree "$state_name" "$item"
				st[recursive]="$old_recursive"
				fixed_dirs+=("$item")
			elif [[ -f "$item" ]]; then
				pc_msg "Fixing 777 file: $item"
				pc_apply_to_single_path "$state_name" "$item"
				pc_add_summary "fixed exact 777 file $item"
			fi
		fi
	done < <(find "$root" \( -type d -o -type f \) -print 2>/dev/null)
}

pc_execute_path_operations() {
	local state_name="$1"
	local -n st="$state_name"

	local -a paths=()
	pc_get_effective_paths "$state_name" paths
	[[ "${#paths[@]}" -gt 0 ]] || return 0

	local path
	if [[ "${st[fix_777]}" == "1" ]]; then
		for path in "${paths[@]}"; do
			pc_fix_exact_777_under_root "$state_name" "$path"
		done
	else
		for path in "${paths[@]}"; do
			pc_apply_tree "$state_name" "$path"
		done
	fi
}

###############################################################################
# MAIN
###############################################################################

pc_main() {
	pc_state_reset
	pc_parse_args PC_STATE "$@" || return 0
	pc_require_root
	pc_validate_config PC_STATE
	pc_collect_auto_questions PC_STATE

	if [[ "$PC_SAVE_ONLY" == "1" ]]; then
		pc_show_plan PC_STATE 0 "save"
		pc_state_export_json PC_STATE "$PC_SAVE_FILE"
		pc_msg "Profile saved to: $PC_SAVE_FILE"
		pc_print_summary
		return 0
	fi

	if [[ "$PC_PRINT_ONLY" == "1" ]]; then
		pc_show_plan PC_STATE 0 "print"
		pc_print_summary
		return 0
	fi

	local ask=0
	if [[ "${PC_STATE[force]}" == "0" && "${PC_STATE[silent]}" == "0" ]]; then
		ask=1
	fi

	pc_show_plan PC_STATE "$ask" "run" || return 0

	if [[ "${PC_STATE[force]}" == "0" && "${PC_STATE[silent]}" == "1" ]]; then
		pc_sleep_countdown "${PC_STATE[delay]}"
	fi

	pc_execute_user_operations PC_STATE
	pc_execute_path_operations PC_STATE
	pc_print_summary
}

if ! pc_is_sourced; then
	pc_main "$@"
fi









# --------------------------------------------------------------------
# SEARCH TAGS / INDEX
#
# perm forge permission manager tool
# filesystem owner group permission automation
# linux permission repair utility chmod chown chgrp helper
# permission profile manager web default shared ownership
# unix permission management devops admin filesystem control
# recursive permission fixer 777 repair group owner sync
# clone permissions from file or folder save load permission profiles
# smart permission orchestration tool for linux servers
# filesystem policy enforcement utility
# devops permission automation script
#
# keywords: permissions groups owners chmod chown chgrp recursive
# keywords: permission repair clone permission profiles
# keywords: filesystem permission automation tool
#
# tool-index: perm forge permission-manager filesystem-admin
# tool-index: permission-repair permission-clone permission-profile
# tool-index: linux-devops permission-automation filesystem-control
#
# --------------------------------------------------------------------