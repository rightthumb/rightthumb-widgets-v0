#!/bin/bash

# Function to install required tools
install_tools() {
  DISTRO=$(cat /etc/os-release | grep -i '^ID=' | cut -d= -f2)

  case $DISTRO in
	debian|ubuntu)
	echo "Installing required tools for Debian/Ubuntu..."
	sudo apt update
	sudo apt install -y mongodb-clients cron
	;;
	fedora|centos|rhel)
	echo "Installing required tools for Fedora/CentOS/RHEL..."
	sudo dnf install -y mongodb-clients cronie
	;;
	arch)
	echo "Installing required tools for Arch Linux..."
	sudo pacman -Syu --noconfirm mongodb-tools cronie
	;;
	*)
	echo "Unknown distribution: $DISTRO. Please install tools manually."
	exit 1
	;;
  esac
}

# Function to display help menu
show_help() {
  echo "Usage: $0 [options]"
  echo ""
  echo "Options:"
  echo "  -h, --help              Show this help menu"
  echo "  -v, --version           Display script version"
  echo "  -d, --database <name>    Name of the MongoDB database to back up"
  echo "  -t, --time <time>        Time (in minutes) for the backup schedule"
  echo "  -p, --path <path>        Path to store backups (default: /backups)"
  echo ""
  echo "Examples:"
  echo "  $0 -d mydatabase -t 60 -p /backups"
  echo "  $0 -v"
  echo ""
}

# Script version
SCRIPT_VERSION="1.0.0"
MONGO_DATABASE=""
BACKUP_PATH="/backups"
BACKUP_TIME="60"  # default backup schedule in minutes

# Parse command line options
while [[ "$1" =~ ^- ]]; do
  case "$1" in
	-h|--help)
	show_help
	exit 0
	;;
	-v|--version)
	echo "setup-database-backup.sh version $SCRIPT_VERSION"
	exit 0
	;;
	-d|--database)
	shift
	MONGO_DATABASE="$1"
	;;
	-t|--time)
	shift
	BACKUP_TIME="$1"
	;;
	-p|--path)
	shift
	BACKUP_PATH="$1"
	;;
	*)
	echo "Invalid option: $1"
	show_help
	exit 1
	;;
  esac
  shift
done

# Check if MongoDB database name is provided
if [ -z "$MONGO_DATABASE" ]; then
  echo "Error: MongoDB database name is required."
  show_help
  exit 1
fi

# Install tools if necessary
install_tools

# Create backup directory if it doesn't exist
echo "Creating backup directory $BACKUP_PATH..."
sudo mkdir -p $BACKUP_PATH
sudo chown $(whoami):$(whoami) $BACKUP_PATH

# Create backup script
BACKUP_SCRIPT="$BACKUP_PATH/backup_mongo.sh"
cat <<EOL > $BACKUP_SCRIPT
#!/bin/bash
DATE=\$(date +\%F-\%H\%M\%S)
BACKUP_FILE="$BACKUP_PATH/\$MONGO_DATABASE-\$DATE.gz"
echo "Starting backup for \$MONGO_DATABASE at \$DATE..."
mongodump --db \$MONGO_DATABASE --archive=\$BACKUP_FILE --gzip
echo "Backup completed: \$BACKUP_FILE"
EOL

# Make the backup script executable
chmod +x $BACKUP_SCRIPT

# Set up cron job to run the backup script periodically
echo "Setting up cron job to back up the database every $BACKUP_TIME minutes..."
CRON_JOB="*/$BACKUP_TIME * * * * $BACKUP_SCRIPT"
(crontab -l ; echo "$CRON_JOB") | crontab -

# Check if the cron job was added successfully
echo "Cron job added to back up the database every $BACKUP_TIME minutes."
echo "To view the cron job, use the command: crontab -l"

echo "Database backup setup completed!"

# ./setup-database-backup.sh -d mydatabase -t 60
# ./setup-database-backup.sh -d mydatabase -t 30 -p /mnt/backup
# ./setup-database-backup.sh -v