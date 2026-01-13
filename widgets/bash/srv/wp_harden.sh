#!/bin/bash

# Harden WordPress Script
# Usage: sudo ./harden-wordpress.sh /var/www/html/your-wordpress-dir

WORDPRESS_DIR="$1"

if [[ -z "$WORDPRESS_DIR" || ! -d "$WORDPRESS_DIR" ]]; then
	echo "❌ Provide a valid WordPress directory"
	exit 1
fi

WP_CONFIG="$WORDPRESS_DIR/wp-config.php"
HTACCESS="$WORDPRESS_DIR/.htaccess"

# 1. Set file and directory permissions
find "$WORDPRESS_DIR" -type d -exec chmod 755 {} \;
find "$WORDPRESS_DIR" -type f -exec chmod 644 {} \;
chmod 600 "$WP_CONFIG"

# 2. Protect wp-config.php via .htaccess
cat <<EOL >> "$HTACCESS"
<Files wp-config.php>
	order allow,deny
	deny from all
</Files>
EOL

# 3. Disable file editing in the dashboard
grep -q DISALLOW_FILE_EDIT "$WP_CONFIG" || echo "define('DISALLOW_FILE_EDIT', true);" >> "$WP_CONFIG"

# 4. Block access to sensitive files
cat <<EOL >> "$HTACCESS"
<FilesMatch "\.(htaccess|htpasswd|ini|log|env|json)\$">
	Order allow,deny
	Deny from all
</FilesMatch>
EOL

# 5. Disable XML-RPC
cat <<EOL >> "$HTACCESS"
<Files xmlrpc.php>
	Order deny,allow
	Deny from all
</Files>
EOL

# 6. Add security headers
cat <<EOL >> "$HTACCESS"
<IfModule mod_headers.c>
	Header always set X-Content-Type-Options "nosniff"
	Header always set X-XSS-Protection "1; mode=block"
	Header always set X-Frame-Options "SAMEORIGIN"
	Header always set Referrer-Policy "no-referrer-when-downgrade"
	Header always set Content-Security-Policy "default-src 'self';"
</IfModule>
EOL

# 7. Lock down MySQL
if grep -q "127.0.0.1" /etc/mysql/my.cnf 2>/dev/null || grep -q "127.0.0.1" /etc/my.cnf 2>/dev/null; then
	echo "✅ MySQL already bound to localhost"
else
	echo "⚠️  Make sure to manually set 'bind-address = 127.0.0.1' in MySQL config (my.cnf)"
fi

# 8. Remind about plugins
cat <<EOF
🔧 Plugin Recommendations (install manually):
- Wordfence or iThemes Security
- Limit Login Attempts Reloaded
- WPS Hide Login (to change login URL)
- WP 2FA
EOF

# 9. Summary
cat <<EOF
✅ WordPress hardening applied:
- Permissions set
- wp-config.php protected
- File editing disabled
- Sensitive file access blocked
- XML-RPC disabled
- Security headers added

🛠️  Next Steps:
- Change DB table prefix if not already
- Enable HTTPS + HSTS
- Install recommended plugins
- Setup fail2ban and backups
EOF