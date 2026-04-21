#!/bin/bash
##### ===== SDS Ticketed Terminal Session (HTML) ===== #####

# storage
export TICKET_DIR="$HOME/.rt/profile/tickets"
mkdir -p "$TICKET_DIR"

# session id (stable per shell) — reuse if you already export it before .bashrc
if [ -z "$Session_ID" ]; then
	# use pid for uniqueness; you can replace with your own generator if desired
	export Session_ID="$$"
fi

# start time (epoch) captured once per shell
if [ -z "$timestamp_start" ]; then
	export timestamp_start="$(date +%s)"
fi

# paths
__ticket_open_html="$TICKET_DIR/open-$Session_ID.html"
__ticket_closed_html="$TICKET_DIR/closed-$Session_ID.html"

# HTML-escape helper
__ticket_escape() {
	# reads stdin, writes escaped text to stdout
	sed -e 's/&/\&amp;/g' -e 's/</\&lt;/g' -e 's/>/\&gt;/g'
}

# initialize/open HTML if missing (so we can append live commands safely)
__ticket_init_html() {
	[ -f "$__ticket_open_html" ] && return 0

	local is_admin="False"
	[ "$EUID" -eq 0 ] && is_admin="True"

	{
		echo "<div class='box'>"
		echo "<div class='item'>Session: $Session_ID (Started: $(date -d @${timestamp_start} '+%Y.%m.%d @ %H.%M')) isAdmin:$is_admin</div>"
		echo "<br>"
		echo "<div class='guid'></div>"
		echo "<div class='sid'></div>"
		echo "<div class='details'>"
		echo "<div class='title'></div>"
		echo "<br>"
		echo "<pre>"
	} > "$__ticket_open_html"
}

# append one command (escaped) into the <pre>… block
__ticket_log_cmd() {
	# last executed command AFTER it ran
	local last="$(history 1 | sed 's/^ *[0-9]\+ *//')"
	[ -z "$last" ] && return 0
	printf "%s\n" "$last" | __ticket_escape >> "$__ticket_open_html"
}

# close out a complete HTML (copy of open + footer) to a target file
__ticket_finalize_to() {
	local out="$1"
	local end_epoch="$(date +%s)"

	# create a temp with footer
	local tmp="$(mktemp)"
	cat "$__ticket_open_html" > "$tmp"
	{
		echo "</pre>"
		echo "<br>"
		echo "<div class='footer'>"
		echo "Ended: $(date -d @${end_epoch} '+%Y.%m.%d @ %H:%M')"
		echo "</div>"
		echo "</div> </div> <br>"
	} >> "$tmp"

	mv -f "$tmp" "$out"
}

# public: set or update the ticket title and mark as “open”
ticket() {
	__ticket_init_html
	local title="$*"

	# if a title is provided, inject/replace it in the dedicated div
	if [ -n "$title" ]; then
		# if title div present, replace it; if not, append (belt & suspenders)
		if grep -q "<div class='title'>" "$__ticket_open_html"; then
			# replace existing <div class='title'>…</div>
			# (use perl for robust multiline replace)
			perl -0777 -pe "s|<div class='title'>.*?</div>|<div class='title'>$(printf '%s' "$title" | __ticket_escape)</div>|s" \
				-i "$__ticket_open_html"
		else
			sed -i "1i <div class='title'>$(printf '%s' "$title" | __ticket_escape)</div>" "$__ticket_open_html"
		fi
		echo "Ticket title set: $title  -> $__ticket_open_html"
	else
		echo "Ticket file: $__ticket_open_html"
	fi
}

# public: close ticket to a closed-*.html file; ASK before exiting shell
x() {
	__ticket_init_html
	__ticket_log_cmd  # flush last command line once more

	__ticket_finalize_to "$__ticket_closed_html"
	echo "Closed snapshot written: $__ticket_closed_html"

	# ask if user wants to exit shell
	read -r -p "Exit shell now? [y/N]: " __ans
	case "$__ans" in
		y|Y) exit ;;
		*)   echo "Staying in shell. (You can run 'x' again later.)" ;;
	esac
}

# public: plain-text summary for a ticket number (Session_ID). 
# Prints Start / End labels and stripped command log for your parsers.
# Usage: ticketnum 925473
ticketnum() {
	local id="$1"
	if [ -z "$id" ]; then
		echo "Usage: ticketnum <Session_ID>"; return 1
	fi
	local f_closed="$TICKET_DIR/closed-$id.html"
	local f_open="$TICKET_DIR/open-$id.html"
	local src=""
	if   [ -f "$f_closed" ]; then src="$f_closed"
	elif [ -f "$f_open"   ]; then src="$f_open"
	else
		echo "No ticket found for Session_ID=$id"; return 1
	fi

	# extract start/end from the HTML header/footer
	# Start format: "Started: YYYY.MM.DD @ HH.MM"
	# End format in closed: "Ended: YYYY.MM.DD @ HH:MM"  (if open, use now)
	local started ended
	started="$(grep -m1 -oE 'Started: [0-9]{4}\.[0-9]{2}\.[0-9]{2} @ [0-9]{2}\.[0-9]{2}' "$src" | sed 's/^Started: //')"
	ended="$(grep -m1 -oE 'Ended: [0-9]{4}\.[0-9]{2}\.[0-9]{2} @ [0-9]{2}:[0-9]{2}' "$src" | sed 's/^Ended: //')"

	if [ -z "$started" ]; then
		# fallback: parse epoch if needed (unlikely because we always write Started:)
		started="(unknown)"
	fi
	if [ -z "$ended" ]; then
		ended="$(date '+%Y.%m.%d @ %H:%M')"
	fi

	echo "Ticket: $id"
	echo "Start:  $started"
	echo "End:    $ended"
	echo "----- Plain Log (HTML stripped) -----"
	# Strip tags, keep only text content (commands are inside <pre>)
	sed -E 's/<[^>]+>//g' "$src"
}

# public: time adjustments for billing (move the START earlier/later)
#   +min N  -> subtract N minutes from start (started earlier)
#   -min N  -> add N minutes to start (started later)
#   +hr  N  -> subtract N hours
#   -hr  N  -> add N hours
adjust_time() {
	local op="$1"; shift
	local n="$1"
	case "$op" in
		+min) timestamp_start=$((timestamp_start - n*60));;
		-min) timestamp_start=$((timestamp_start + n*60));;
		+hr)  timestamp_start=$((timestamp_start - n*3600));;
		-hr)  timestamp_start=$((timestamp_start + n*3600));;
		*) echo "Usage: +min N | -min N | +hr N | -hr N"; return 1;;
	esac
	export timestamp_start
	echo "timestamp_start → $timestamp_start  ($(date -d @${timestamp_start}))"

	# also refresh the "Started:" stamp at top of the open HTML
	if [ -f "$__ticket_open_html" ]; then
		perl -0777 -pe "s|Started: [0-9]{4}\.[0-9]{2}\.[0-9]{2} @ [0-9]{2}\.[0-9]{2}|Started: $(date -d @${timestamp_start} '+%Y.%m.%d @ %H.%M')|g" \
			-i "$__ticket_open_html"
	fi
}

# convenience aliases to mimic your Windows workflow
alias +min='adjust_time +min'
alias -min='adjust_time -min'
alias +hr='adjust_time +hr'
alias -hr='adjust_time -hr'

# live logging: append every finished command to the HTML (robust, runs after each command)
__PROMPT_ORIG="$PROMPT_COMMAND"
PROMPT_COMMAND='__ticket_init_html; __ticket_log_cmd; '"$__PROMPT_ORIG"
##### ===== End SDS Ticketed Terminal Session (HTML) ===== #####