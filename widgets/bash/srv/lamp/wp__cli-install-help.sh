#!/bin/bash

set -e

# Install WP-CLI if not found
if ! command -v wp &>/dev/null; then
	echo "🔧 WP-CLI not found. Installing..."
	curl -O https://raw.githubusercontent.com/wp-cli/builds/gh-pages/phar/wp-cli.phar
	php wp-cli.phar --info
	chmod +x wp-cli.phar
	sudo mv wp-cli.phar /usr/local/bin/wp
	echo "✅ WP-CLI installed at /usr/local/bin/wp"
else
	echo "✅ WP-CLI is already installed at $(command -v wp)"
fi

# Show concise + powerful help menu
echo
echo "🧠 WORDPRESS CLI POWER MENU"
echo "============================"
echo "💥 Most Useful Commands (Best at Top):"
echo
echo "🔄 1. Search & Replace (No Execute, Preview Only):"
echo "   wp search-replace 'http://old.site' 'https://new.site' --dry-run"
echo
echo "✅ 2. Search & Replace (Live Change):"
echo "   wp search-replace 'http://old.site' 'https://new.site'"
echo
echo "🛠 3. Fix Common File Permissions (for www-data user):"
echo "   sudo chown -R www-data:www-data ."
echo "   find . -type d -exec chmod 755 {} \;"
echo "   find . -type f -exec chmod 644 {} \;"
echo
echo "📦 4. Reset All Plugins (disable all):"
echo "   wp plugin deactivate --all"
echo
echo "🎨 5. Reset to Default Theme (e.g., twentytwentyfour):"
echo "   wp theme activate twentytwentyfour"
echo
echo "🔧 6. Database Repair:"
echo "   wp db repair"
echo
echo "🧰 7. Reinstall Core (no content loss):"
echo "   wp core download --force"
echo
echo "🔑 8. Reset Admin Password:"
echo "   wp user update admin --user_pass='newpassword'"
echo
echo "🌐 9. Fix URL Settings (Hardcoded in DB):"
echo "   wp option update home 'https://example.com'"
echo "   wp option update siteurl 'https://example.com'"
echo
echo "📜 10. Full WP Help:"
echo "   wp help"
echo
echo "🚨 Note: Always backup your DB before search-replace or repairs:"
echo "   wp db export backup.sql"
echo
echo "✨ You're ready to WP like a pro!"