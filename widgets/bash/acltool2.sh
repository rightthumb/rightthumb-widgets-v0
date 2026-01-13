#!/usr/bin/env bash
# acltool.sh — Users, Groups, Classic Permissions & ACLs (CRUD/LIST/CLEAR)
# Version: 1.1
# Works on: Debian/Ubuntu, RHEL/CentOS/Fedora, openSUSE, Arch, Alpine (auto installs ACL tools)
# Run with: sudo ./acltool.sh <command> ... OR sudo ./acltool.sh --switch ...

set -euo pipefail

log(){ echo "[*] $*"; }
ok(){ echo "[✓] $*"; }
warn(){ echo "[!] $*" >&2; }
err(){ echo "[ERROR] $*" >&2; exit 1; }
need_cmd(){ command -v "$1" >/dev/null 2>&1; }

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
	if need_cmd setfacl && need_cmd getfacl; then return 0; fi
	log "ACL tools not found. Installing…"
	case "$(detect_pkg_mgr)" in
		apt)    sudo apt-get update -y && sudo apt-get install -y acl ;;
		dnf)    sudo dnf install -y acl ;;
		yum)    sudo yum install -y acl ;;
		zypper) sudo zypper --non-interactive install acl ;;
		pacman) sudo pacman -Sy --noconfirm acl ;;
		apk)    sudo apk add --no-interactive acl ;;
		*)      err "Unsupported distro. Please install 'acl' manually."
	esac
	ok "ACL tools installed."
}

ensure_root(){
	if [[ "${EUID:-$(id -u)}" -ne 0 ]]; then
		err "Please run as root (sudo)."
	fi
}

exists_group(){ getent group "$1" >/dev/null 2>&1; }
exists_user(){ id -u "$1" >/dev/null 2>&1; }
csv_to_array(){ local IFS=','; read -r -a __arr <<< "$1"; printf '%s\n' "${__arr[@]}"; }

print_cheatsheet(){
	cat <<'EOF'
──────────────────────────────────────────────────────────────────────────────
PERMISSIONS CHEAT SHEET (classic chmod & ACL)
──────────────────────────────────────────────────────────────────────────────

NUMERIC BITS (per class u/g/o):  r=4  w=2  x=1
	7 = rwx     6 = rw-     5 = r-x     4 = r--     3 = -wx     2 = -w-     1 = --x     0 = ---

COMMON FILE MODES:
	644 = u=rw-, g=r--, o=r--      (owner edits; everyone reads)
	640 = u=rw-, g=r--, o=---      (owner+group read; others none)
	600 = u=rw-, g=---, o=---      (private file)
	660 = u=rw-, g=rw-, o=---      (team editable; no others)

COMMON DIRECTORY MODES (x = enter/list; w = create/delete):
	755 = u=rwx, g=rx,  o=rx       (publicly readable)
	750 = u=rwx, g=rx,  o=---      (group access; others none)
	770 = u=rwx, g=rwx, o=---      (team writable; others none)

SPECIAL BITS (thousands digit):
	2xxx setgid on directory  → new files/dirs inherit the directory's group
	4xxx setuid on file       → run as file owner (admin binaries)
	+t   sticky on directory  → users cannot delete files they don’t own (e.g., /tmp)
Examples:
	2770 = setgid + u=rwx,g=rwx,o=---       (ideal for shared team folders)
	1777 = sticky + a=rwx (like /tmp)

SYMBOLIC CHMOD:
	chmod u=rwX,g=rwX,o=         (X only gives execute on dirs or already-exec files)
	chmod -R g+wX .              (recursively add group write+exec where appropriate)

ACL PERMISSIONS (beyond owner/group/others):
	r (read), w (write), x (execute), X (conditional execute)
Examples:
	setfacl -m u:alice:rwx <path>     (user-specific)
	setfacl -m g:devs:rwX <path>      (group-specific)
	setfacl -m m::rwX <path>          (mask: max rights for named users/groups)
	setfacl -m d:g:devs:rwx <dir>     (DEFAULT ACL for new items in directory)

MASK (m::):
	Limits effective permissions for all named users/groups (not the owner).
	If your ACL looks correct but access is missing, check the mask:
	setfacl -m m::rwX <path>

TYPICAL RECIPES:
  • Private file:                                  chmod 600 file
  • Private directory:                             chmod 700 dir
  • Public read-only web content:                   chmod 755 -R /var/www/html
  • Shared team area (inherit group):               chmod 2770 /srv/project; chgrp projectgrp /srv/project
  • Team area + ACL defaults (inherit permissions): setfacl -m g:projectgrp:rwx /srv/project
												setfacl -m d:g:projectgrp:rwx /srv/project
  • Read-only viewer (outside the group):           setfacl -m u:viewer:rX /srv/project
												setfacl -m d:u:viewer:rX /srv/project

WHO-GETS-WHAT (at a glance)
  Users:
	- Primary group: exactly one
	- Supplementary groups: many (id username)
  Files/Folders (classic):
	- One owner, one primary group
	- Others = everyone else
  Files/Folders (with ACLs):
	- Any number of named users/groups with custom rights
	- Optional DEFAULT entries on directories for inheritance
──────────────────────────────────────────────────────────────────────────────
EOF
}

print_help(){
	cat <<'EOF'
acltool.sh — Users, Groups, Classic Permissions & ACLs (CRUD/LIST/CLEAR)
USAGE:
  sudo ./acltool.sh <command> [args] [options]
  sudo ./acltool.sh --switch [args] [options]

GENERAL:
  help | --help                 Show help + cheatsheet
  cheat | --cheat               Show only the permissions cheat sheet
  doctor | --doctor             Check/install ACL tools (setfacl/getfacl)

USER & GROUP CRUD:
  user create <user>                    |  --user-create <user>
  user delete <user>                    |  --user-delete <user>
  user delete --purge <user>            |  --user-delete-purge <user>
  user add-to-group <user> <group>      |  --user-add-to-group <user> <group>
  user remove-from-group <user> <group> |  --user-remove-from-group <user> <group>

  group create <group>                  |  --group-create <group>
  group delete <group>                  |  --group-delete <group>
  group info   <group>                  |  --group-info <group>
  whoami <user>                         |  --whoami <user>

CLASSIC PERMS & ATTRS:
  chgrp <group> <path>                  |  --chgrp <group> <path>
  chmod <mode> <path>                   |  --chmod <mode> <path>
  sticky on|off <path>                  |  --sticky on|off <path>
  setgid on|off <path>                  |  --setgid on|off <path>

ACL LIST/CLEAR:
  acl list <path>                       |  --acl-list <path>
  acl clear <path>                      |  --acl-clear <path>
  acl clear-recursive <path>            |  --acl-clear-recursive <path>

ACL ADD/REMOVE (+ DEFAULTS) (supports recursive variants):
  acl add-user <user>:<perms> <path>            |  --acl-add-user <user>:<perms> <path>
  acl add-group <group>:<perms> <path>          |  --acl-add-group <group>:<perms> <path>
  acl del-user <user> <path>                    |  --acl-del-user <user> <path>
  acl del-group <group> <path>                  |  --acl-del-group <group> <path>

  acl default add-user <user>:<perms> <dir>     |  --acl-default-add-user <user>:<perms> <dir>
  acl default add-group <group>:<perms> <dir>   |  --acl-default-add-group <group>:<perms> <dir>
  acl default del-user <user> <dir>             |  --acl-default-del-user <user> <dir>
  acl default del-group <group> <dir>           |  --acl-default-del-group <group> <dir>

  acl add-user-recursive <user>:<perms> <dir>   |  --acl-add-user-recursive <user>:<perms> <dir>
  acl add-group-recursive <group>:<perms> <dir> |  --acl-add-group-recursive <group>:<perms> <dir>
  acl del-user-recursive <user> <dir>           |  --acl-del-user-recursive <user> <dir>
  acl del-group-recursive <group> <dir>         |  --acl-del-group-recursive <group> <dir>
  acl mask <perms> <path>                       |  --acl-mask <perms> <path>
  acl mask-recursive <perms> <dir>              |  --acl-mask-recursive <perms> <dir>

PROJECT SCAFFOLD:
  project setup <group> <dir> [--users u1,u2] [--mode 2770] [--sticky] [--no-acl]
  --project-setup <group> <dir> [--users u1,u2] [--mode 2770] [--sticky] [--no-acl]

BULK (LIST OF PATHS):
  bulk <file-with-paths> "<subcommand ...>"   # runs subcommand for each path in file
  Example:
	sudo ./acltool.sh bulk paths.txt "acl add-group devs:rwX"
	sudo ./acltool.sh bulk paths.txt "--acl-add-group devs:rwX"

EXAMPLES (short):
  sudo ./acltool.sh --doctor
  sudo ./acltool.sh --project-setup projectgrp /srv/project --users alice,bob --mode 2770
  sudo ./acltool.sh --acl-add-group-recursive qa:rX /srv/project
  sudo ./acltool.sh --acl-clear-recursive /srv/project
  sudo ./acltool.sh --sticky on /srv/drop

(Scroll for the full built-in cheat sheet)
EOF
	print_cheatsheet
}

# If no args, show help + cheatsheet
[[ $# -eq 0 ]] && { print_help; exit 0; }

# Normalize: if first arg begins with '-', treat as switch-mode.
cmd="${1:-}"; shift || true

# -------------------- Subcommand + Switch handlers -------------------------
handle_user(){
	local sub="$1"; shift || true
	case "$sub" in
		create|--user-create)
			ensure_root; u="${1:?Usage: user create <user>}"; exists_user "$u" && ok "User exists: $u" || { useradd -m "$u"; ok "User created: $u"; }
		;;
		delete|--user-delete)
			ensure_root; u="${1:?Usage: user delete <user>}"; exists_user "$u" || err "User not found: $u"; userdel "$u"; ok "Deleted user $u (home kept)."
		;;
		--user-delete-purge)
			ensure_root; u="${1:?Usage: --user-delete-purge <user>}"; exists_user "$u" || err "User not found: $u"; userdel -r "$u"; ok "Deleted user $u with home."
		;;
		add-to-group|--user-add-to-group)
			ensure_root; u="${1:?}"; g="${2:?Usage: user add-to-group <user> <group>}"; exists_user "$u" || err "No user $u"; exists_group "$g" || err "No group $g"; usermod -aG "$g" "$u"; ok "Added $u to $g."
		;;
		remove-from-group|--user-remove-from-group)
			ensure_root; u="${1:?}"; g="${2:?Usage: user remove-from-group <user> <group>}"; exists_user "$u" || err "No user $u"; exists_group "$g" || err "No group $g"
			if need_cmd gpasswd; then gpasswd -d "$u" "$g" >/dev/null; else
				current="$(id -nG "$u" | tr ' ' '\n' | grep -v "^$g$" | tr '\n' ',' | sed 's/,$//')"
				usermod -G "$current" "$u"
			fi
			ok "Removed $u from $g."
		;;
		*)
			err "Unknown user op."
		;;
	esac
}

handle_group(){
	local sub="$1"; shift || true
	case "$sub" in
		create|--group-create)
			ensure_root; g="${1:?Usage: group create <group>}"; exists_group "$g" && ok "Group exists: $g" || { groupadd "$g"; ok "Group created: $g"; }
		;;
		delete|--group-delete)
			ensure_root; g="${1:?Usage: group delete <group>}"; exists_group "$g" || err "No group $g"; groupdel "$g"; ok "Group deleted: $g"
		;;
		info|--group-info)
			g="${1:?Usage: group info <group>}"; getent group "$g" || err "No group $g"
		;;
		*)
			err "Unknown group op."
		;;
	esac
}

handle_classic(){
	case "$1" in
		chgrp|--chgrp)
			ensure_root; g="${2:-}"; p="${3:-}"; [[ -n "$g" && -n "$p" ]] || err "Usage: chgrp <group> <path>"; exists_group "$g" || err "No group $g"; chown -R :"$g" "$p"; ok "Set group '$g' on $p"
		;;
		chmod|--chmod)
			ensure_root; mode="${2:-}"; p="${3:-}"; [[ -n "$mode" && -n "$p" ]] || err "Usage: chmod <mode> <path>"; chmod "$mode" "$p"; ok "chmod $mode → $p"
		;;
		sticky|--sticky)
			ensure_root; act="${2:-}"; p="${3:-}"; [[ "$act" =~ ^(on|off)$ ]] || err "Usage: sticky on|off <path>"; [[ "$act" == "on" ]] && chmod +t "$p" || chmod -t "$p"; ok "sticky $act on $p"
		;;
		setgid|--setgid)
			ensure_root; act="${2:-}"; p="${3:-}"; [[ "$act" =~ ^(on|off)$ ]] || err "Usage: setgid on|off <path>"; [[ "$act" == "on" ]] && chmod g+s "$p" || chmod g-s "$p"; ok "setgid $act on $p"
		;;
		*)
			err "Unknown classic op."
		;;
	esac
}

handle_acl(){
	auto_install_acl
	local sub="$1"; shift || true
	case "$sub" in
		list|--acl-list)
			p="${1:?Usage: acl list <path>}"; getfacl -p "$p"
		;;
		clear|--acl-clear)
			ensure_root; p="${1:?}"; setfacl -b "$p" || true; setfacl -k "$p" || true; ok "Cleared ACLs on $p"
		;;
		clear-recursive|--acl-clear-recursive)
			ensure_root; p="${1:?}"; setfacl -Rb "$p" || true; find "$p" -exec setfacl -k {} + 2>/dev/null || true; ok "Cleared ACLs recursively on $p"
		;;
		add-user|--acl-add-user)
			ensure_root; spec="${1:?user:perms}"; p="${2:?path}"; IFS=':' read -r u perms <<<"$spec"; setfacl -m "u:${u}:${perms}" "$p"; ok "ACL user $u:$perms → $p"
		;;
		add-group|--acl-add-group)
			ensure_root; spec="${1:?group:perms}"; p="${2:?path}"; IFS=':' read -r g perms <<<"$spec"; setfacl -m "g:${g}:${perms}" "$p"; ok "ACL group $g:$perms → $p"
		;;
		del-user|--acl-del-user)
			ensure_root; u="${1:?user}"; p="${2:?path}"; setfacl -x "u:${u}" "$p"; ok "Removed user ACL $u on $p"
		;;
		del-group|--acl-del-group)
			ensure_root; g="${1:?group}"; p="${2:?path}"; setfacl -x "g:${g}" "$p"; ok "Removed group ACL $g on $p"
		;;
		default)
			sub2="${1:-}"; shift || true
			case "$sub2" in
				add-user|--acl-default-add-user)
					ensure_root; spec="${1:?user:perms}"; d="${2:?dir}"; IFS=':' read -r u perms <<<"$spec"; setfacl -m "d:u:${u}:${perms}" "$d"; ok "DEFAULT user $u:$perms → $d"
				;;
				add-group|--acl-default-add-group)
					ensure_root; spec="${1:?group:perms}"; d="${2:?dir}"; IFS=':' read -r g perms <<<"$spec"; setfacl -m "d:g:${g}:${perms}" "$d"; ok "DEFAULT group $g:$perms → $d"
				;;
				del-user|--acl-default-del-user)
					ensure_root; u="${1:?user}"; d="${2:?dir}"; setfacl -x "d:u:${u}" "$d"; ok "DEFAULT del user $u on $d"
				;;
				del-group|--acl-default-del-group)
					ensure_root; g="${1:?group}"; d="${2:?dir}"; setfacl -x "d:g:${g}" "$d"; ok "DEFAULT del group $g on $d"
				;;
				*) err "Unknown 'acl default' op." ;;
			esac
		;;
		add-user-recursive|--acl-add-user-recursive)
			ensure_root; spec="${1:?user:perms}"; d="${2:?dir}"; IFS=':' read -r u perms <<<"$spec"; setfacl -R -m "u:${u}:${perms}" "$d"; ok "Recursive user $u:$perms → $d"
		;;
		add-group-recursive|--acl-add-group-recursive)
			ensure_root; spec="${1:?group:perms}"; d="${2:?dir}"; IFS=':' read -r g perms <<<"$spec"; setfacl -R -m "g:${g}:${perms}" "$d"; ok "Recursive group $g:$perms → $d"
		;;
		del-user-recursive|--acl-del-user-recursive)
			ensure_root; u="${1:?user}"; d="${2:?dir}"; find "$d" -exec setfacl -x "u:${u}" {} + 2>/dev/null || true; ok "Recursive del user $u on $d"
		;;
		del-group-recursive|--acl-del-group-recursive)
			ensure_root; g="${1:?group}"; d="${2:?dir}"; find "$d" -exec setfacl -x "g:${g}" {} + 2>/dev/null || true; ok "Recursive del group $g on $d"
		;;
		mask|--acl-mask)
			ensure_root; perms="${1:?perms}"; p="${2:?path}"; setfacl -m "m::${perms}" "$p"; ok "Mask $perms → $p"
		;;
		mask-recursive|--acl-mask-recursive)
			ensure_root; perms="${1:?perms}"; d="${2:?dir}"; setfacl -R -m "m::${perms}" "$d"; ok "Mask $perms (recursive) → $d"
		;;
		*)
			err "Unknown ACL op."
		;;
	esac
}

handle_project_setup(){
	ensure_root
	local g="${1:?Usage: project setup <group> <dir> [--users u1,u2] [--mode 2770] [--sticky] [--no-acl]}"
	local d="${2:?Usage: project setup <group> <dir> ...}"
	shift 2 || true
	local users="" mode="2770" do_sticky="no" do_acl="yes"
	while [[ $# -gt 0 ]]; do
		case "$1" in
			--users) users="${2:-}"; shift 2 ;;
			--mode) mode="${2:-}"; shift 2 ;;
			--sticky) do_sticky="yes"; shift ;;
			--no-acl) do_acl="no"; shift ;;
			*) err "Unknown option: $1" ;;
		esac
	done
	exists_group "$g" || { groupadd "$g"; ok "Created group $g"; }
	if [[ -n "$users" ]]; then
		while read -r u; do
			[[ -z "$u" ]] && continue
			exists_user "$u" || { useradd -m "$u"; ok "Created user $u"; }
			usermod -aG "$g" "$u"; ok "Added $u to $g"
		done < <(csv_to_array "$users")
	fi
	mkdir -p "$d"
	chown root:"$g" "$d"
	chmod "$mode" "$d"
	[[ "$do_sticky" == "yes" ]] && chmod +t "$d"
	if [[ "$do_acl" == "yes" ]]; then
		auto_install_acl
		setfacl -m "g:${g}:rwx" "$d"
		setfacl -m "d:g:${g}:rwx" "$d"
		setfacl -m d:o::--- "$d"
	fi
	ok "Project ready: $d (group=$g, mode=$mode, sticky=$do_sticky, acl=$do_acl)"
	getfacl "$d" | sed 's/^/# /'
}

handle_bulk(){
	ensure_root
	local file="${1:?Usage: bulk <file-with-paths> \"<subcommand or --switch ...>\"}"
	shift || true
	[[ $# -ge 1 ]] || err "Provide a subcommand string to run for each path."
	local subcmd="$*"
	[[ -f "$file" ]] || err "File not found: $file"
	while IFS= read -r path; do
		[[ -z "$path" ]] && continue
		log "Bulk on: $path -> ${subcmd} \"$path\""
		# shellcheck disable=SC2086
		eval "./$(basename "$0") ${subcmd} \"$path\""
	done < "$file"
	ok "Bulk operation completed."
}

# -------------------- Router --------------------
case "$cmd" in
	help|--help)          print_help ;;
	cheat|--cheat)        print_cheatsheet ;;
	doctor|--doctor)      auto_install_acl; ok "Environment OK." ;;

	user|--user-create|--user-delete|--user-delete-purge|--user-add-to-group|--user-remove-from-group)
		if [[ "$cmd" == "user" ]]; then handle_user "$1" "${@:2}"; else handle_user "$cmd" "$@"; fi
	;;
	group|--group-create|--group-delete|--group-info)
		if [[ "$cmd" == "group" ]]; then handle_group "$1" "${@:2}"; else handle_group "$cmd" "$@"; fi
	;;
	whoami|--whoami)      u="${1:?Usage: whoami <user>}"; id "$u" ;;

	chgrp|chmod|sticky|setgid|--chgrp|--chmod|--sticky|--setgid)
		handle_classic "$cmd" "$cmd" "$@"
	;;

	acl|--acl-list|--acl-clear|--acl-clear-recursive|--acl-add-user|--acl-add-group|--acl-del-user|--acl-del-group|--acl-default-add-user|--acl-default-add-group|--acl-default-del-user|--acl-default-del-group|--acl-add-user-recursive|--acl-add-group-recursive|--acl-del-user-recursive|--acl-del-group-recursive|--acl-mask|--acl-mask-recursive)
		if [[ "$cmd" == "acl" ]]; then handle_acl "$1" "${@:2}"; else handle_acl "$cmd" "$@"; fi
	;;

	project)
		[[ "${1:-}" == "setup" ]] || err "Usage: project setup <group> <dir> [--users ...]"
		shift
		handle_project_setup "$@"
	;;
	--project-setup)
		handle_project_setup "$@"
	;;

	bulk)                 handle_bulk "$@" ;;

	*) err "Unknown command/switch. Try: ./acltool.sh --help" ;;
esac