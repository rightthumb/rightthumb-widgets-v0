# **Bitcoin Core Setup and Usage Documentation**

## **1. Introduction**

This documentation provides instructions for managing Bitcoin Core installed via Snap. It includes steps to start the server, use `bitcoin-cli`, and manage the server using `tmux` for long-term uptime.

---

## **2. Configuration File**

The configuration file for Bitcoin Core is located at:

```plaintext
~/.bitcoin/bitcoin.conf
```

Example content of the file:

```ini
server=1
daemon=1
rpcuser=bitcoinrpc
rpcpassword=your_secure_password
rpcallowip=127.0.0.1
rpcport=8332
disablewallet=0
```

- `rpcuser` and `rpcpassword`: Credentials for interacting with the Bitcoin RPC server.
- `rpcallowip`: Restricts RPC access to local connections only.
- `rpcport`: Specifies the RPC port, default is `8332`.

If you update this file, ensure to restart the daemon to apply the changes.

---

## **3. Starting the Bitcoin Core Daemon**

To start the Bitcoin Core daemon (`bitcoind`), run the following command:

```bash
/snap/bin/bitcoin-core.daemon
```

---

## **4. Using `tmux` for Persistent Daemon Management**

`tmux` is a terminal multiplexer that allows you to run processes like the Bitcoin Core daemon in a persistent session, even after you disconnect from SSH or close your terminal.

### **4.1 Install tmux**

If `tmux` is not installed, install it:

```bash
sudo apt install tmux -y
```

### **4.2 Start Bitcoin Core in a tmux Session**

1. Create a new tmux session named `bitcoin`:

   ```bash
   tmux new -s bitcoin
   ```

2. Inside the tmux session, start the Bitcoin Core daemon:

   ```bash
   /snap/bin/bitcoin-core.daemon
   ```

3. Detach from the tmux session (leave it running in the background):

   ```bash
   Ctrl+b d
   ```

### **4.3 Reattach to the tmux Session**

To reconnect to the tmux session later:

```bash
tmux attach -t bitcoin
```

### **4.4 List tmux Sessions**

If you have multiple tmux sessions and want to list them:

```bash
tmux list-sessions
```

### **4.5 Kill a tmux Session**

To stop the Bitcoin Core session and close it:

```bash
tmux kill-session -t bitcoin
```

---

## **5. Interacting with Bitcoin Core**

Use the `bitcoin-cli` tool to interact with the daemon. Below are some common commands:

### **5.1 Check Blockchain Info**

```bash
bitcoin-cli -rpcuser=bitcoinrpc -rpcpassword=your_secure_password getblockchaininfo
```

### **5.2 Generate a New Address**

```bash
bitcoin-cli -rpcuser=bitcoinrpc -rpcpassword=your_secure_password getnewaddress
```

### **5.3 Check Wallet Balance**

```bash
bitcoin-cli -rpcuser=bitcoinrpc -rpcpassword=your_secure_password getbalance
```

### **5.4 Send Bitcoin**

```bash
bitcoin-cli -rpcuser=bitcoinrpc -rpcpassword=your_secure_password sendtoaddress <recipient_address> <amount_in_btc>
```

Replace `<recipient_address>` and `<amount_in_btc>` with the appropriate values.

---

## **6. Checking Logs**

To troubleshoot or monitor the Bitcoin Core daemon, check the logs:

### **6.1 Snap Logs**

```bash
snap logs bitcoin-core
```

### **6.2 Debug Logs**

If `~/.bitcoin/debug.log` exists:

```bash
tail -f ~/.bitcoin/debug.log
```

---

## **7. Stopping the Bitcoin Core Daemon**

If you need to stop the daemon, run:

```bash
bitcoin-cli -rpcuser=bitcoinrpc -rpcpassword=your_secure_password stop
```

If you are using a `tmux` session, you can also kill the session:

```bash
tmux kill-session -t bitcoin
```

---

## **8. Troubleshooting**

- **Daemon Fails to Start**:
  - Check the Snap logs:

	```bash
	snap logs bitcoin-core
	```

  - Verify the configuration file for errors:

	```bash
	nano ~/.bitcoin/bitcoin.conf
	```

- **RPC Connection Fails**:
  - Ensure the daemon is running:

	```bash
	ps aux | grep bitcoind
	```

  - Test the RPC connection using `curl`:

	```bash
	curl --user bitcoinrpc:your_secure_password --data-binary '{"jsonrpc":"1.0","id":"curltest","method":"getblockchaininfo","params":[]}' -H 'content-type: text/plain;' http://127.0.0.1:8332/
	```

---

## **9. Additional Resources**

- **Official Bitcoin Core Documentation**: [https://bitcoincore.org](https://bitcoincore.org)
- **Bitcoin CLI Commands Reference**: [Bitcoin RPC Wiki](https://en.bitcoin.it/wiki/Original_Bitcoin_client/API_calls_list)