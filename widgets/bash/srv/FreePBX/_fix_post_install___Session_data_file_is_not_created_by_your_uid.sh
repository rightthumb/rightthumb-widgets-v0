# See where PHP is writing sessions
php -i | grep -i 'session.save_path'
# Expect something like: session.save_path => /var/lib/php/sessions

# Make sure the directory exists and has correct perms
sudo mkdir -p /var/lib/php/sessions
sudo chown -R www-data:www-data /var/lib/php/sessions
sudo chmod 1733 /var/lib/php/sessions

# If your install script created /var/lib/php/session (singular), it’s harmless,
# but PHP won’t use it. You can remove stale files just in case:
sudo rm -f /var/lib/php/session/* 2>/dev/null || true

# Clear old session files and restart Apache
sudo find /var/lib/php/sessions -type f -delete
sudo systemctl restart apache2

# Fix FreePBX file ownerships for good measure
sudo fwconsole chown
sudo fwconsole reload
