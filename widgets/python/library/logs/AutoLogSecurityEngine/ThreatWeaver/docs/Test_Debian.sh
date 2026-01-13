#!/bin/bash

touch /opt/whitelist_ip.txt

python3 ../FirewallEngine.py \
  --file /var/log/auth.log \
  --log-type auth \
  --whitelist-ip /opt/whitelist_ip.txt \
  --firewall iptables \
  --ingest-events-sqlite /opt/FirewallEngine_ingest_events.sqlite \
  --window-min 3000 \
  --ssh-fail-thresh 5 \
  --ssh-fail-score 2 \
  --ssh-fail-bonus 4 \
  --score-block 8 \
  --ledger-scan \
  --ledger-since-min 0 \
  --ledger-min-ssh 10 \
  --ledger-min-total 500 \
  --ingest-summary