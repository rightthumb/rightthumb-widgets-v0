# How to use it

## **Install/enable file-based auth (keeps certs)**

```bash
sudo bash setup-openvpn-file-auth.sh
```

## **Add a user (interactive password prompt)**

```bash
sudo bash setup-openvpn-file-auth.sh --add-user alice
```

…or non-interactive:

```bash
sudo bash setup-openvpn-file-auth.sh --add-user alice --password 'S3cret!'
```

## **Delete a user:**

```bash
sudo bash setup-openvpn-file-auth.sh --del-user alice
```

## **Client side:** make sure the `.ovpn` profile has

```ovpn
auth-user-pass
```

You’ll keep using **certs** and the client will be prompted for **username/password** from your `users.htpasswd`.

---

### Notes & tips

* Passwords are stored **bcrypt-hashed** in `users.htpasswd`.
* You can manage that file directly with `htpasswd` if you prefer.
* We **do not** enable `client-cert-not-required` or `verify-client-cert none`, so certs remain required (stronger).
* Want to disable a user temporarily? You can change their hash to something invalid or remove the line; reconnects will fail.