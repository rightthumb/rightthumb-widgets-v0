
# Samba Server Documentation

## File Structure:

- `/etc/samba/smb.conf`: The main configuration file for Samba. It defines global settings and shares.
- `/var/log/samba/`: Directory containing Samba log files.
- `/opt/share/`: Example shared directory.

## Samba Configuration (`smb.conf`):

- **Global Settings**:
  - `workgroup`: Defines the workgroup name.
  - `server string`: Description of the Samba server.
  - `netbios name`: NetBIOS name of the Samba server.
  - `security`: Specifies the security mode (e.g., user).
  - `map to guest`: Specifies how unauthorized users are treated.
  - `dns proxy`: Whether Samba should act as a DNS proxy.
- **Share Definitions**:
  - `[shared]`: Example share definition.
    - `path`: Path to the shared directory.
    - `browseable`: Whether the share is visible.
    - `writable`: Whether users can write to the share.
    - `guest ok`: Whether guest access is allowed.
    - `read only`: Whether the share is read-only.

## Troubleshooting:

1. **Check Samba Service**:
   - Verify that the Samba service (`smbd`) is running:

     ```bash
     sudo systemctl status smbd
     ```

2. **Firewall Settings**:
   - Ensure that the firewall allows Samba traffic:

     ```bash
     sudo ufw allow samba
     ```

3. **Network Connectivity**:
   - Verify network connectivity between the Windows machine and the Samba server.
   - Check if you can ping the server from the Windows machine:

     ```bash
     ping <SERVER_IP>
     ```

4. **Windows Configuration**:
   - Enable network discovery and ensure correct workgroup settings.
   - Check Windows Firewall settings to allow Samba traffic.

5. **Access by IP Address**:
   - Try accessing the share using the server's IP address:

     ```
     \\<SERVER_IP>\shared
     ```

6. **Credentials**:
   - Double-check username and password when accessing the share from Windows.
   - Ensure that the credentials match those configured on the Samba server.

7. **Windows Event Viewer**:
   - Review the Windows Event Viewer for any relevant error messages or warnings related to networking or file sharing.

8. **Wireshark Analysis**:
   - Use Wireshark to capture network traffic between the Windows machine and the Samba server for detailed analysis.

### Conclusion:

This documentation provides an overview of the Samba server setup, including file structure, configuration, and troubleshooting steps to resolve common issues. By following these guidelines, you can ensure the smooth operation of your Samba server and troubleshoot any connectivity issues effectively.

sudo systemctl restart nmbd
sudo systemctl restart smbd
