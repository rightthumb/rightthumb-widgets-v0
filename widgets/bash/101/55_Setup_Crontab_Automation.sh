#!/bin/bash
# Script to set up cron jobs

# Display current cron jobs
crontab -l

# Add a new cron job
echo "0 0 * * * /path/to/script.sh" | crontab -