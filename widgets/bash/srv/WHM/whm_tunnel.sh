#!/bin/bash

# ───────────────────────────────────────────────
# WHM/cPanel Reverse SSH Tunnel Script (Real-World Use)
# Usage: ./whm_tunnel.sh user@your-vps-ip
# Author: Hosting-Grade 🛠️
# ───────────────────────────────────────────────

REMOTE="$1"

if [[ -z "$REMOTE" ]]; then
	echo "Usage: $0 user@your-vps-ip"
	exit 1
fi

# ───────────────────────────────────────────────
# Exhaustive Port List for WHM/cPanel (No Plugins)
# ───────────────────────────────────────────────
PORTS=(
	# ───── Core Services ─────
	2087    # WHM (SSL)
	2086    # WHM (non-SSL)
	2083    # cPanel (SSL)
	2082    # cPanel (non-SSL)
	2096    # Webmail (SSL)
	2095    # Webmail (non-SSL)
	2089    # License check

	# ───── Web Traffic ─────
	80      # HTTP
	443     # HTTPS

	# ───── Mail Services ─────
	25      # SMTP
	465     # SMTP (SSL)
	587     # SMTP (submission/authenticated)
	110     # POP3
	995     # POP3 (SSL)
	143     # IMAP
	993     # IMAP (SSL)

	# ───── Database ─────
	3306    # MySQL/MariaDB

	# ───── SSH (for rsync, Transfer Tool) ─────
	22      # SSH access

	# ───── Optional but Common ─────
	783     # SpamAssassin (included in base installs)
)

# ───────────────────────────────────────────────
# Build the SSH Tunnel Command
# ───────────────────────────────────────────────
TUNNEL_CMD="ssh -N -T"

for PORT in "${PORTS[@]}"; do
	TUNNEL_CMD+=" -R $PORT:localhost:$PORT"
done

TUNNEL_CMD+=" $REMOTE"

echo "───────────────────────────────────────────────"
echo "⛓️  Starting WHM Reverse Tunnel to: $REMOTE"
echo "📡 Ports forwarded: ${#PORTS[@]}"
echo "───────────────────────────────────────────────"
eval "$TUNNEL_CMD"