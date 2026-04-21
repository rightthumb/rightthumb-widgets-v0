# ✅ WHM Post Install Good Practices

## 1. 🚨 **Secure Your WHM Access**

- **Set the hostname** (`WHM » Networking Setup » Change Hostname`)
  - e.g. `domain.com`
- **Configure the resolver** (`WHM » Networking Setup » Resolver Configuration`)
  - Use your provider's resolvers or `1.1.1.1` / `8.8.8.8`
- **Enable Two-Factor Auth** (`WHM » Security Center » Two-Factor Authentication`)
- **Change SSH Port** (optional — via CSF or manually)

---

## 2. 🛡️ **Basic Security Hardening**

- Install **CSF (ConfigServer Security & Firewall)** if not already done
- Enable **cPHulk Brute Force Protection**
  - `WHM » Security Center » cPHulk Brute Force Protection`
- Configure **Shell Fork Bomb Protection**
  - `WHM » Security Center » Shell Fork Bomb Protection`

---

## 3. 🔐 **SSL & AutoSSL Setup**

- **Enable AutoSSL** (`WHM » SSL/TLS » Manage AutoSSL`)
  - Provider: Let's Encrypt or cPanel
- Configure **AutoSSL notification settings**
- Add your hostname to AutoSSL coverage

---

## 4. 🧠 **General Server Config**

- `WHM » Server Configuration » Basic WebHost Manager® Setup`
  - Set:
    - Primary IP address
    - Contact email
    - Default nameservers (e.g. `ns1.domain.com`)
- Set **TTL defaults** if you want shorter DNS propagation
- Set **default PHP version** under `WHM » MultiPHP Manager`

---

## 5. 📧 **Email and Notifications**

- Set **root contact email**
- Configure **WHM » Contact Manager** to choose what alerts get sent (disk, abuse, failure, etc.)
- Review **Mailserver Configuration** and **Service Manager**

---

## 6. 🧩 **Optional: Prepare Add-ons or Tools**

- Install:
  - WordPress Toolkit (optional)
  - ImunifyAV (free malware scanner)
  - Softaculous (if you want app installers)
- Configure backups (even before accounts are live):
  - `WHM » Backup » Backup Configuration`
  - Choose compressed/incremental, destinations, etc.
