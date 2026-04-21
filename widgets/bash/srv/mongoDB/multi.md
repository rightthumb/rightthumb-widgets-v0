# Multi MongoDB Config

## 🧾 MongoDB Multi-Instance Setup Guide

### 📁 1. Create Unique Configuration

For each instance (e.g. `mongo2`), create a new config file:

```bash
sudo cp /etc/mongo1.conf /etc/mongo2.conf
```

Then edit `/etc/mongo2.conf`:

```yaml
systemLog:
  path: /var/log/mongodb/mongod2.log

storage:
  dbPath: /var/lib/mongo2
  journal:
    enabled: true
  wiredTiger:
    engineConfig:
      cacheSizeGB: 0.25
      configString: "eviction=(threads_min=1,threads_max=2)"

processManagement:
  timeZoneInfo: /usr/share/zoneinfo

net:
  port: 27018
  bindIp: 127.0.0.1
  unixDomainSocket:
    pathPrefix: /var/run/mongodb2
```

> Make sure:
>
> * `path` is unique in `systemLog`
> * `dbPath` is different (e.g. `/var/lib/mongo2`)
> * `port` is unique
> * `pathPrefix` for socket is different

---

### 📂 2. Create Required Folders

```bash
sudo mkdir -p /var/lib/mongo2 /var/log/mongodb /var/run/mongodb2
sudo chown -R mongod:mongod /var/lib/mongo2 /var/run/mongodb2
```

---

### 🧾 3. Create a Matching systemd Unit

```bash
sudo cp /etc/systemd/system/mongod@mongo1.service /etc/systemd/system/mongod@mongo2.service
```

No need to edit if it's a template unit (`mongod@.service`) — otherwise ensure this line is correct:

```ini
ExecStart=/usr/bin/mongod --config /etc/mongo2.conf
```

---

### 🔁 4. Reload and Start

```bash
sudo systemctl daemon-reload
sudo systemctl enable mongod@mongo2
sudo systemctl start mongod@mongo2
sudo systemctl status mongod@mongo2
```

---

## ✅ You now have:

| Instance | Port  | Config             | DB Path           | Log File                       |
| -------- | ----- | ------------------ | ----------------- | ------------------------------ |
| mongo1   | 27017 | `/etc/mongo1.conf` | `/var/lib/mongo`  | `/var/log/mongodb/mongod.log`  |
| mongo2   | 27018 | `/etc/mongo2.conf` | `/var/lib/mongo2` | `/var/log/mongodb/mongod2.log` |

---

Let me know if you want to:

* Convert these into a replica set
* Use authentication (`keyFile` setup)
* Add sharding/routers
* Auto-generate configs for N instances

---
---
---
---

## Service Config

Here is the full contents of your working systemd unit file for `mongod@mongo1.service`:

```bash
sudo nano /etc/systemd/system/mongod@mongo1.service
```

```ini
[Unit]
Description=MongoDB Instance: mongo1
After=network.target

[Service]
User=mongod
Group=mongod
ExecStart=/usr/bin/mongod --config /etc/mongo1.conf
LimitNOFILE=64000
LimitNPROC=64000
TimeoutSec=300
Restart=always
RestartSec=3

[Install]
WantedBy=multi-user.target
```

### ✅ Key Features:

* `%i` makes this a **template unit**, so `mongod@mongo2` uses `/etc/mongo2.conf`, `mongod@mongo3` uses `/etc/mongo3.conf`, etc.
* Restarts automatically if `mongod` crashes.
* Does **not** use `--fork` — systemd handles the process.
* Handles high file descriptor and process limits, good for production and replication.

---

### 🔁 Reload after any change:

```bash
sudo systemctl daemon-reload
```
