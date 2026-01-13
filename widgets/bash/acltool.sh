#!/usr/bin/env bash
# acltool.sh — Users, Groups, Permissions & ACLs (create/read/update/delete/list/clear)
# Version: 1.0
# Requires: coreutils, findutils, grep, awk, sed, passwd tools, and ACL tools (setfacl/getfacl)
# This script will auto-install missing ACL tooling on common distros.

set -euo pipefail

# ------------------------------- UTILITIES ---------------------------------
log(){ echo "[*] $*"; }
ok(){ echo "[✓] $*"; }
warn(){ echo "[!] $*" >&2; }
err(){ echo "[ERROR] $*" >&2; exit 1; }

need_cmd(){ command -v "$1" >/dev/null 2>&1 || return 1; }

detect_pkg_mgr(){
	if need_cmd apt-get; then echo "apt"; return; fi
	if need_cmd dnf; then echo "dnf"; return; fi
	if need_cmd yum; then echo "yum"; return; fi
	if need_cmd zypper; then echo "zypper"; return; fi
	if need_cmd pacman; then echo "pacman"; return; fi
	if need_cmd apk; then echo "apk"; return; fi
	echo "unknown"
}

auto_install_acl(){
	local mgr; mgr="$(detect_pkg_mgr)"
	if need_cmd setfacl && need_cmd getfacl; then return 0; fi
	log "ACL tools not found. Attempting to install…"
	case "$mgr" in
		apt)
			sudo apt-get update -y
			sudo apt-get install -y acl
		;;
		dnf) sudo dnf install -y acl ;;
		yum) sudo yum install -y acl ;;
		zypper) sudo zypper --non-interactive install acl ;;
		pacman)
			sudo pacman -Sy --noconfirm acl
		;;
		apk)
			sudo apk add --no-interactive acl
		;;
		*)
			err "Unsupported distro/package manager. Please install 'acl' manually."
		;;
	esac
	ok "ACL tools installed."
}

ensure_root(){
	if [[ "${EUID:-$(id -u)}" -ne 0 ]]; then
		err "Please run as root or with sudo."
	fi
}

exists_group(){ getent group "$1" >/dev/null 2>&1; }
exists_user(){ id -u "$1" >/dev/null 2>&1; }

csv_to_array(){
	# usage: csv_to_array "a,b,c"
	local IFS=','; read -r -a __arr <<< "$1"; printf '%s\n' "${__arr[@]}"
}

# ------------------------------- HELP --------------------------------------
print_help(){
	cat <<'EOF'
acltool.sh — Users, Groups, Classic Permissions & ACLs (Create/Read/Update/Delete/List/Clear)

USAGE:
  sudo ./acltool.sh <command> [args] [options]

GENERAL COMMANDS:
  help                               Show this help (also default when no args)
  doctor                             Check/install needed tools (setfacl/getfacl)

USER & GROUP CRUD:
  user create <user>                 Create user with home directory
  user delete <user>                 Delete user (keeps home)
  user delete --purge <user>         Delete user and remove home (-r)
  user add-to-group <user> <group>   Add existing user to existing group (supplementary)
  user remove-from-group <user> <group>  Remove user from group

  group create <group>               Create group
  group delete <group>               Delete group
  group info <group>                 Show group entry
  whoami <user>                      Show user's uid/gid & supplementary groups

FOLDER/GROUP BINDING (classic Unix):
  chgrp <group> <path>               Set primary group ownership of path
  chmod <mode> <path>                Apply classic perms (e.g., 770, 2750, u=rwX,g=rwX,o=)
  sticky on|off <path>               Enable/disable sticky bit on directory (shared drop zones)
  setgid on|off <path>               Enable/disable setgid bit on directory (inherit group on new files)

ACL — LIST & CLEAR:
  acl list <path>                    Show ACLs on file/dir
  acl clear <path>                   Remove all extended & default ACLs (-b and -k)
  acl clear-recursive <path>         Like 'acl clear' but recursively

ACL — ADD / UPDATE:
  acl add-user <user>:<perms> <path>            Add/update ACL entry for user (e.g., alice:rwx)
  acl add-group <group>:<perms> <path>          Add/update ACL entry for group (e.g., devs:rwX)
  acl default add-user <user>:<perms> <dir>     Add DEFAULT ACL for user on directory
  acl default add-group <group>:<perms> <dir>   Add DEFAULT ACL for group on directory
  acl mask <perms> <path>                       Set ACL mask (limits group & named-user perms)

ACL — REMOVE:
  acl del-user <user> <path>                    Remove named-user ACL
  acl del-group <group> <path>                  Remove named-group ACL
  acl default del-user <user> <dir>             Remove DEFAULT named-user ACL
  acl default del-group <group> <dir>           Remove DEFAULT named-group ACL

ACL — RECURSIVE VARIANTS:
  acl add-user-recursive <user>:<perms> <dir>           Recursive
  acl add-group-recursive <group>:<perms> <dir>         Recursive
  acl del-user-recursive <user> <dir>                   Recursive
  acl del-group-recursive <group> <dir>                 Recursive
  acl mask-recursive <perms> <dir>                      Recursive

PROJECT SCAFFOLD (quick team setup):
  project setup <group> <dir> [--users u1,u2,...] [--mode 2770] [--sticky] [--no-acl]
	- Creates group if missing, adds users, creates directory, sets:
		* chgrp <group> <dir>
		* chmod <mode> (default 2770: setgid + rwx for owner/group)
		* DEFAULT ACLs so new files/dirs inherit group rwx (unless --no-acl)
	- --sticky: enable sticky bit (prevent deleting others' files in shared drops)
	- Example:
		sudo ./acltool.sh project setup projectgrp /srv/project --users alice,bob,carol --mode 2770

BULK (LIST OF FILES/FOLDERS):
  bulk <file-with-paths> <subcommand> [...]
	- Runs the given subcommand for each line path in the file.
	- Example:
		sudo ./acltool.sh bulk paths.txt "acl add-group devs:rwX"
		sudo ./acltool.sh bulk paths.txt "acl clear"

EXAMPLES — COMMON PERMISSION PATTERNS:
  # Team-writable project folder with strict outsider lockout:
	sudo ./acltool.sh project setup projectgrp /srv/project --users alice,bob --mode 2770

  # Give QA group read-only on an existing tree:
	sudo ./acltool.sh acl add-group-recursive qa:rX /srv/project

  # Give one outside user read/execute (no write) and inherit for new content:
	sudo ./acltool.sh acl add-user alice:rX /srv/project
	sudo ./acltool.sh acl default add-user alice:rX /srv/project

  # Remove all ACLs:
	sudo ./acltool.sh acl clear-recursive /srv/project

  # Classic perms: setgid (inherit group) and no others:
	sudo ./acltool.sh setgid on /srv/repo
	sudo ./acltool.sh chmod 2770 /srv/repo

PERMISSION QUICK REFERENCE:
  Classic chmod (numeric):
	7=rwx, 6=rw-, 5=r-x, 4=r--, 3=-wx, 2=-w-, 1=--x, 0=---
	Examples: 750 (u=rwx,g=rx,o=---), 640 (u=rw,g=r,o=---), 2770 (setgid + rwx/rwx/---)
  Classic chmod (symbolic):
	u,g,o,a with +/- and = and X (conditional execute on dirs/executable files)
	e.g., chmod u=rwX,g=rwX,o= file; chmod -R g+wX .
  Special bits:
	setgid on dir (2xxx) -> new files inherit group; sticky (+t) -> users can't delete others' files in dir

  ACL perms string:
	r (read), w (write), x (execute), X (execute if directory or already executable),
	e.g., devs:rwX, qa:rX, alice:rwx
  ACL mask:
	Limits the maximum effective permissions for all named users and groups (not the owner).
	Example: set to rwX to allow full use; set to r-X for read-only style ceiling:
	acl mask rwX <path>

NOTES:
  • Linux files/dirs have only one primary group, but ACLs can grant access to multiple users/groups.
  • DEFAULT ACLs (d:) apply to new children created in a directory; they don’t retroactively change existing ones.
  • After adding a user to a group, the user may need to log out/in (or new session) to refresh group memberships.

EOF
}

# Default to help with no args
[[ $# -eq 0 ]] && { print_help; exit 0; }

# ------------------------------- ACTIONS -----------------------------------
cmd="$1"; shift || true

case "$cmd" in
	help|-h|--help)
		print_help
	;;
	doctor)
		auto_install_acl
		ok "Environment looks good."
	;;

	# -------- USER & GROUP --------
	user)
		sub="${1:-}"; shift || true
		case "$sub" in
			create)
				ensure_root
				u="${1:?Usage: user create <user>}"
				if exists_user "$u"; then ok "User exists: $u"; else
					log "Creating user: $u"
					useradd -m "$u"
					ok "User created: $u"
				fi
			;;
			delete)
				ensure_root
				if [[ "${1:-}" == "--purge" ]]; then
					shift || true
					u="${1:?Usage: user delete --purge <user>}"
					exists_user "$u" || err "User not found: $u"
					log "Deleting user and home: $u"
					userdel -r "$u"
					ok "Deleted user $u with home."
				else
					u="${1:?Usage: user delete <user>}"
					exists_user "$u" || err "User not found: $u"
					log "Deleting user (home kept): $u"
					userdel "$u"
					ok "Deleted user $u."
				fi
			;;
			add-to-group)
				ensure_root
				u="${1:?Usage: user add-to-group <user> <group>}"
				g="${2:?Usage: user add-to-group <user> <group>}"
				exists_user "$u" || err "User not found: $u"
				exists_group "$g" || err "Group not found: $g"
				usermod -aG "$g" "$u"
				ok "Added $u to $g (supplementary)."
			;;
			remove-from-group)
				ensure_root
				u="${1:?Usage: user remove-from-group <user> <group>}"
				g="${2:?Usage: user remove-from-group <user> <group>}"
				exists_user "$u" || err "User not found: $u"
				exists_group "$g" || err "Group not found: $g"
				# portable removal: edit group membership using gpasswd or deluser/usermod -G
				if need_cmd gpasswd; then
					gpasswd -d "$u" "$g" >/dev/null
				else
					# Fallback: reconstruct supplementary group list (dangerous if race); prefer gpasswd
					current="$(id -nG "$u" | tr ' ' '\n' | grep -v "^$g$" | tr '\n' ',' | sed 's/,$//')"
					usermod -G "$current" "$u"
				fi
				ok "Removed $u from $g."
			;;
			*)
				err "Unknown 'user' subcommand. See: ./acltool.sh help"
			;;
		esac
	;;

	group)
		sub="${1:-}"; shift || true
		case "$sub" in
			create)
				ensure_root
				g="${1:?Usage: group create <group>}"
				if exists_group "$g"; then ok "Group exists: $g"; else
					groupadd "$g"
					ok "Group created: $g"
				fi
			;;
			delete)
				ensure_root
				g="${1:?Usage: group delete <group>}"
				exists_group "$g" || err "Group not found: $g"
				groupdel "$g"
				ok "Group deleted: $g"
			;;
			info)
				g="${1:?Usage: group info <group>}"
				getent group "$g" || err "Group not found: $g"
			;;
			*)
				err "Unknown 'group' subcommand. See: ./acltool.sh help"
			;;
		esac
	;;

	whoami)
		u="${1:?Usage: whoami <user>}"
		id "$u"
	;;

	# -------- CLASSIC PERMS & ATTRS --------
	chgrp)
		ensure_root
		g="${1:?Usage: chgrp <group> <path>}"
		p="${2:?Usage: chgrp <group> <path>}"
		exists_group "$g" || err "Group not found: $g"
		chown -R :"$g" "$p"
		ok "Set group '$g' on: $p"
	;;
	chmod)
		ensure_root
		mode="${1:?Usage: chmod <mode> <path>}"
		p="${2:?Usage: chmod <mode> <path>}"
		command chmod "$mode" "$p"
		ok "chmod $mode applied to $p"
	;;
	sticky)
		ensure_root
		act="${1:?Usage: sticky on|off <path>}"
		p="${2:?Usage: sticky on|off <path>}"
		if [[ "$act" == "on" ]]; then
			chmod +t "$p"; ok "Sticky bit enabled on $p"
		elif [[ "$act" == "off" ]]; then
			chmod -t "$p"; ok "Sticky bit disabled on $p"
		else
			err "Use: sticky on|off <path>"
		fi
	;;
	setgid)
		ensure_root
		act="${1:?Usage: setgid on|off <path>}"
		p="${2:?Usage: setgid on|off <path>}"
		if [[ "$act" == "on" ]]; then
			chmod g+s "$p"; ok "setgid bit enabled on $p"
		elif [[ "$act" == "off" ]]; then
			chmod g-s "$p"; ok "setgid bit disabled on $p"
		else
			err "Use: setgid on|off <path>"
		fi
	;;

	# -------- ACL LIST & CLEAR --------
	acl)
		auto_install_acl
		sub="${1:-}"; shift || true
		case "$sub" in
			list)
				p="${1:?Usage: acl list <path>}"
				getfacl -p "$p"
			;;
			clear)
				ensure_root
				p="${1:?Usage: acl clear <path>}"
				setfacl -b "$p" || true
				setfacl -k "$p" || true
				ok "Cleared ACLs on $p"
			;;
			clear-recursive)
				ensure_root
				p="${1:?Usage: acl clear-recursive <path>}"
				setfacl -Rb "$p" || true
				# setfacl has no -Rk, so use find:
				find "$p" -exec setfacl -k {} + 2>/dev/null || true
				ok "Cleared ACLs recursively on $p"
			;;

			add-user)
				ensure_root
				spec="${1:?Usage: acl add-user <user>:<perms> <path>}"
				p="${2:?Usage: acl add-user <user>:<perms> <path>}"
				IFS=':' read -r u perms <<<"$spec"
				[[ -n "${u:-}" && -n "${perms:-}" ]] || err "Use user:perms (e.g., alice:rwX)"
				setfacl -m "u:${u}:${perms}" "$p"
				ok "Added ACL for user $u ($perms) on $p"
			;;
			add-group)
				ensure_root
				spec="${1:?Usage: acl add-group <group>:<perms> <path>}"
				p="${2:?Usage: acl add-group <group>:<perms> <path>}"
				IFS=':' read -r g perms <<<"$spec"
				[[ -n "${g:-}" && -n "${perms:-}" ]] || err "Use group:perms (e.g., devs:rwX)"
				setfacl -m "g:${g}:${perms}" "$p"
				ok "Added ACL for group $g ($perms) on $p"
			;;
			"default")
				sub2="${1:-}"; shift || true
				case "$sub2" in
					add-user)
						ensure_root
						spec="${1:?Usage: acl default add-user <user>:<perms> <dir>}"
						d="${2:?Usage: acl default add-user <user>:<perms> <dir>}"
						IFS=':' read -r u perms <<<"$spec"
						setfacl -m "d:u:${u}:${perms}" "$d"
						ok "Added DEFAULT ACL for user $u ($perms) on $d"
					;;
					add-group)
						ensure_root
						spec="${1:?Usage: acl default add-group <group>:<perms> <dir>}"
						d="${2:?Usage: acl default add-group <group>:<perms> <dir>}"
						IFS=':' read -r g perms <<<"$spec"
						setfacl -m "d:g:${g}:${perms}" "$d"
						ok "Added DEFAULT ACL for group $g ($perms) on $d"
					;;
					del-user)
						ensure_root
						u="${1:?Usage: acl default del-user <user> <dir>}"
						d="${2:?Usage: acl default del-user <user> <dir>}"
						setfacl -x "d:u:${u}" "$d"
						ok "Removed DEFAULT user ACL for $u on $d"
					;;
					del-group)
						ensure_root
						g="${1:?Usage: acl default del-group <group> <dir>}"
						d="${2:?Usage: acl default del-group <group> <dir>}"
						setfacl -x "d:g:${g}" "$d"
						ok "Removed DEFAULT group ACL for $g on $d"
					;;
					*)
						err "Unknown 'acl default' subcommand. See: ./acltool.sh help"
					;;
				esac
			;;
			del-user)
				ensure_root
				u="${1:?Usage: acl del-user <user> <path>}"
				p="${2:?Usage: acl del-user <user> <path>}"
				setfacl -x "u:${u}" "$p"
				ok "Removed ACL for user $u on $p"
			;;
			del-group)
				ensure_root
				g="${1:?Usage: acl del-group <group> <path>}"
				p="${2:?Usage: acl del-group <group> <path>}"
				setfacl -x "g:${g}" "$p"
				ok "Removed ACL for group $g on $p"
			;;
			add-user-recursive)
				ensure_root
				spec="${1:?Usage: acl add-user-recursive <user>:<perms> <dir>}"
				d="${2:?Usage: acl add-user-recursive <user>:<perms> <dir>}"
				IFS=':' read -r u perms <<<"$spec"
				setfacl -R -m "u:${u}:${perms}" "$d"
				ok "Added user ACL ($u:$perms) recursively on $d"
			;;
			add-group-recursive)
				ensure_root
				spec="${1:?Usage: acl add-group-recursive <group>:<perms> <dir>}"
				d="${2:?Usage: acl add-group-recursive <group>:<perms> <dir>}"
				IFS=':' read -r g perms <<<"$spec"
				setfacl -R -m "g:${g}:${perms}" "$d"
				ok "Added group ACL ($g:$perms) recursively on $d"
			;;
			del-user-recursive)
				ensure_root
				u="${1:?Usage: acl del-user-recursive <user> <dir>}"
				d="${2:?Usage: acl del-user-recursive <user> <dir>}"
				find "$d" -exec setfacl -x "u:${u}" {} + 2>/dev/null || true
				ok "Removed user ACL ($u) recursively on $d"
			;;
			del-group-recursive)
				ensure_root
				g="${1:?Usage: acl del-group-recursive <group> <dir>}"
				d="${2:?Usage: acl del-group-recursive <group> <dir>}"
				find "$d" -exec setfacl -x "g:${g}" {} + 2>/dev/null || true
				ok "Removed group ACL ($g) recursively on $d"
			;;
			mask)
				ensure_root
				perms="${1:?Usage: acl mask <perms> <path>}"
				p="${2:?Usage: acl mask <perms> <path>}"
				setfacl -m "m::${perms}" "$p"
				ok "Set ACL mask ($perms) on $p"
			;;
			mask-recursive)
				ensure_root
				perms="${1:?Usage: acl mask-recursive <perms> <dir>}"
				d="${2:?Usage: acl mask-recursive <perms> <dir>}"
				setfacl -R -m "m::${perms}" "$d"
				ok "Set ACL mask ($perms) recursively on $d"
			;;
			*)
				err "Unknown 'acl' subcommand. See: ./acltool.sh help"
			;;
		esac
	;;

	# -------- PROJECT SCAFFOLD --------
	project)
		sub="${1:-}"; shift || true
		case "$sub" in
			setup)
				ensure_root
				g="${1:?Usage: project setup <group> <dir> [--users u1,u2] [--mode 2770] [--sticky] [--no-acl]}"
				d="${2:?Usage: project setup <group> <dir> [--users u1,u2] [--mode 2770] [--sticky] [--no-acl]}"
				shift 2 || true
				users=""
				mode="2770"
				do_sticky="no"
				do_acl="yes"
				# parse options
				while [[ $# -gt 0 ]]; do
					case "$1" in
						--users) users="${2:-}"; shift 2 ;;
						--mode) mode="${2:-}"; shift 2 ;;
						--sticky) do_sticky="yes"; shift ;;
						--no-acl) do_acl="no"; shift ;;
						*) err "Unknown option: $1" ;;
					esac
				done
				# group
				if ! exists_group "$g"; then groupadd "$g"; ok "Created group $g"; else ok "Group exists: $g"; fi
				# users
				if [[ -n "$users" ]]; then
					while read -r u; do
						[[ -z "$u" ]] && continue
						if ! exists_user "$u"; then useradd -m "$u"; ok "Created user $u"; fi
						usermod -aG "$g" "$u"; ok "Added $u to $g"
					done < <(csv_to_array "$users")
				fi
				# dir
				mkdir -p "$d"
				chown root:"$g" "$d"
				chmod "$mode" "$d"
				[[ "$do_sticky" == "yes" ]] && chmod +t "$d"
				if [[ "$do_acl" == "yes" ]]; then
					auto_install_acl
					# Ensure group has rwx now and for future children
					setfacl -m "g:${g}:rwx" "$d"
					setfacl -m "d:g:${g}:rwx" "$d"
					# Keep others out by default
					setfacl -m d:o::--- "$d"
				fi
				ok "Project ready: $d (group=$g, mode=$mode, sticky=$do_sticky, acl=$do_acl)"
				getfacl "$d" | sed 's/^/# /'
			;;
			*)
				err "Unknown 'project' subcommand. See: ./acltool.sh help"
			;;
		esac
	;;

	# -------- BULK (list of paths file) --------
	bulk)
		ensure_root
		file="${1:?Usage: bulk <file-with-paths> <quoted-subcommand>}"
		shift || true
		[[ $# -ge 1 ]] || err "Provide a subcommand string to run for each path."
		subcmd="$*"
		[[ -f "$file" ]] || err "File not found: $file"
		while IFS= read -r path; do
			[[ -z "$path" ]] && continue
			log "Bulk on: $path -> $subcmd \"$path\""
			# shellcheck disable=SC2086
			eval "./$(basename "$0") ${subcmd} \"$path\""
		done < "$file"
		ok "Bulk operation completed."
	;;

	*)
		err "Unknown command: $cmd. See: ./acltool.sh help"
	;;
esac