#!/bin/bash

# ANSI escape codes for color output
RED='\033[0;31m'
GREEN='\033[0;32m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
RESET='\033[0m'

echo -e "${CYAN}Understanding Crontab Schedule Format${RESET}"
echo -e "${GREEN}-----------------------------------${RESET}\n"

echo -e "${RED}* * * * * command-to-be-executed${RESET}"
echo -e "┬ ┬ ┬ ┬ ┬"
echo -e "│ │ │ │ │"
echo -e "│ │ │ │ │"
echo -e "│ │ │ │ └───── ${GREEN}day of week${RESET} (0 - 7) (Sunday is both 0 and 7)"
echo -e "│ │ │ └────────── ${GREEN}month${RESET} (1 - 12)"
echo -e "│ │ └─────────────── ${GREEN}day of the month${RESET} (1 - 31)"
echo -e "│ └─────────────────── ${GREEN}hour${RESET} (0 - 23)"
echo -e "└─────────────────────── ${GREEN}min${RESET} (0 - 59)\n"

echo -e "${BLUE}Examples:${RESET}"
echo -e "1. ${GREEN}0 5 * * 1${RESET} means 'At 5:00am on every Monday.'"
echo -e "2. ${GREEN}*/10 * * * *${RESET} means 'Every 10 minutes.'"
echo -e "3. ${GREEN}0 0 1 * *${RESET} means 'At midnight on the first day of every month.'"
echo -e "4. ${GREEN}0 12 * * *${RESET} means 'At 12:00pm (noon) every day.'"
echo -e "5. ${GREEN}5,10,15 * * * *${RESET} means 'At 5, 10, and 15 minutes past every hour.'"
echo -e "6. ${GREEN}0 0 * * 7${RESET} means 'At midnight every Sunday.'"
echo -e "7. ${GREEN}0 */2 * * *${RESET} means 'At the start of every 2nd hour.'"
echo -e "8. ${GREEN}0 9-17 * * *${RESET} means 'At the start of every hour from 9am to 5pm.'"
echo -e "9. ${GREEN}30 3 1-15 * *${RESET} means 'At 3:30am on the 1st to the 15th of every month.'"
echo -e "10. ${GREEN}0 0 1 1,7 *${RESET} means 'At midnight on the 1st of January and July.'"
echo -e "11. ${GREEN}*/5 9-17 * * 1-5${RESET} means 'Every 5 minutes during 9am to 5pm, Monday to Friday.'"
echo -e "12. ${GREEN}59 23 31 12 *${RESET} means 'At 11:59pm on December 31st.'"
echo -e "13. ${GREEN}0 0 * 2 0${RESET} means 'At midnight of every Sunday in February.'"
echo -e "14. ${GREEN}0 6 1,15,30 * *${RESET} means 'At 6:00am on the 1st, 15th, and 30th of every month.'"
echo -e "15. ${GREEN}15,45 */3 * 4-10 *${RESET} means 'At 15 and 45 minutes past every 3rd hour, from April to October.'\n"

echo -e "Remember, the order is: ${GREEN}Minute Hour DayOfMonth Month DayOfWeek${RESET}\n"

echo -e "${CYAN}Note:${RESET} Always ensure you test your cron jobs in a safe environment before applying them in a production scenario."

# Exit
exit 0