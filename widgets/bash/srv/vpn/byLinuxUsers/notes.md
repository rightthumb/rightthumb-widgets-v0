# How to use

## Copy to your server (after you've already installed OpenVPN + PKI), then

```bash
sudo bash setup-openvpn-pam-with-group.sh --users alice,bob --create-users
```

* This creates group **`openvpn-users`**, creates `alice` and `bob` (with **nologin** shells), sets passwords, adds them to the group, enables PAM auth, and restarts OpenVPN.

## If the users already exist:

```bash
sudo bash setup-openvpn-pam-with-group.sh --users alice,bob
```

## If you have a file of usernames (one per line)

```bash
printf "alice\nbob\ncarol\n" > /root/vpn_allowed.txt
sudo bash setup-openvpn-pam-with-group.sh --allowed-file /root/vpn_allowed.txt
```

## Make sure your clients' `.ovpn` profiles include

```ovpn
auth-user-pass
```

They'll continue using their **certs** and will now be asked for **Linux credentials** too.