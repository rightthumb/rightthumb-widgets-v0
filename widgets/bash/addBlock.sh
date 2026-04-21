#!/usr/bin/env bash

addBlock() {

	local target_file="$1"
	local array_name="$2"

	# -------------------------
	# defaults
	# -------------------------
	[[ -z "$target_file" ]] && target_file="$HOME/.bashrc."
	[[ -z "$array_name"  ]] && array_name="BASHRC_BLOCKS"

	# -------------------------
	# validation
	# -------------------------
	if [[ ! -e "$target_file" ]]; then
		touch "$target_file" || {
			echo "failed to create file: $target_file" >&2
			return 1
		}
	fi

	if ! declare -p "$array_name" >/dev/null 2>&1; then
		echo "array not found: $array_name" >&2
		return 1
	fi

	# -------------------------
	# nameref
	# -------------------------
	declare -n _blocks_ref="$array_name"

	local key
	for key in "${!_blocks_ref[@]}"; do

		if ! grep -Fq "$key" "$target_file"; then
			{
				printf '\n%s\n' "${_blocks_ref[$key]}"
			} >> "$target_file"

			printf 'added: %s -> %s\n' "$key" "$target_file"
		else
			printf 'exists: %s -> %s\n' "$key" "$target_file"
		fi

	done
}


add_block() {
	local array_name="$1"
	local marker="$2"
	local content="$3"
	declare -n _arr="$array_name"
	_arr["$marker"]="$content"
}

declare -A BASHRC_BLOCKS

BASHRC_BLOCKS["# >>> is777 >>>"]='# >>> is777 >>>
is777() {

	local root="."
	local verbose=0

	for arg in "$@"; do
		case "$arg" in
			-v) verbose=1 ;;
			*) root="$arg" ;;
		esac
	done

	_scan_777_basic() {
		find "$root" \
			\( -type d -perm -0002 -print -prune \) -o \
			\( -type f -perm -0002 -print \)
	}

	_scan_777_verbose() {
		find "$root" \
			\( -type d -perm -0002 -exec stat -c "%a %n" {} \; -prune \) -o \
			\( -type f -perm -0002 -exec stat -c "%a %n" {} \; \)
	}

	if [[ $verbose -eq 1 ]]; then
		_scan_777_verbose
	else
		_scan_777_basic
	fi
}
# <<< scan_777 <<<'

BASHRC_BLOCKS["# >>> jqstruct >>>"]='# >>> jqstruct >>>
jqstruct() {
	jq '\''
		def struct:
			if type == "object" then
				with_entries(.value |= struct)
			elif type == "array" then
				if length == 0 then
					[]
				else
					[ (.[0] | struct) ]
				end
			else
				type
			end;
		struct
	'\'' "$@"
}
alias .json="jqstruct"
# <<< jqstruct <<<'


declare -A BASHRC_BLOCKS

add_block BASHRC_BLOCKS "# >>> test.block >>>" '# >>> test.block >>>
echo "hello"
# <<< test.block <<<'