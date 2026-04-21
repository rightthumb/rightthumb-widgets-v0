# **`virsh` Documentation**

`virsh` is a command-line tool used to manage and interact with virtual machines (VMs) on a host system. It is part of the `libvirt` toolkit and provides a variety of commands for controlling, monitoring, and configuring VMs.

---

## **Getting Started**

### **Basic Syntax**

```bash
virsh [options] <command> [arguments]
```

- **Options**: Modify `virsh` behavior (e.g., `--connect` for remote servers).
- **Command**: Specify the action to perform (e.g., `start`, `list`).
- **Arguments**: Pass additional details to the command (e.g., VM name).

---

## **Common Commands**

### **1. List VMs**

```bash
virsh list --all
```

- Lists all virtual machines, including running and inactive ones.
- Columns:
  - **Id**: Numeric ID of the VM (only for running VMs).
  - **Name**: Name of the VM.
  - **State**: Status of the VM (e.g., `running`, `shut off`).

### **2. Start a VM**

```bash
virsh start <vm_name>
```

- Starts a stopped VM.

### **3. Stop a VM (Gracefully)**

```bash
virsh shutdown <vm_name>
```

- Sends an ACPI shutdown signal to the VM, equivalent to pressing the power button.

### **4. Stop a VM (Forcefully)**

```bash
virsh destroy <vm_name>
```

- Forcefully powers off the VM without a graceful shutdown.
- Use with caution as it may cause data loss.

### **5. Restart a VM**

```bash
virsh reboot <vm_name>
```

- Reboots a running VM.

### **6. Pause and Resume a VM**

- Pause:

  ```bash
  virsh suspend <vm_name>
  ```

  - Suspends the VM, stopping all CPU activity without shutting it down.
- Resume:

  ```bash
  virsh resume <vm_name>
  ```

  - Resumes a paused VM.

### **7. Define or Undefine a VM**

- Define:

  ```bash
  virsh define <xml_file>
  ```

  - Creates a persistent VM configuration from an XML file.
- Undefine:

  ```bash
  virsh undefine <vm_name>
  ```

  - Removes the VM's configuration.

### **8. Delete a VM Disk**

```bash
rm -f /var/lib/libvirt/images/<vm_name>.qcow2
```

- Deletes the VM's disk file. Use with caution.

### **9. Connect to a VM Console**

```bash
virsh console <vm_name>
```

- Connects to the serial console of the VM.
- Press **Ctrl+]** to exit.

### **10. Set Autostart for a VM**

- Enable autostart:

  ```bash
  virsh autostart <vm_name>
  ```

- Disable autostart:

  ```bash
  virsh autostart --disable <vm_name>
  ```

### **11. Check VM Status**

```bash
virsh domstate <vm_name>
```

- Displays the current state of the VM (e.g., `running`, `shut off`).

### **12. Monitor VM Resources**

- View resource usage (CPU, memory):

  ```bash
  virsh dominfo <vm_name>
  ```

- List virtual devices attached to the VM:

  ```bash
  virsh domblklist <vm_name>
  ```

---

## **Advanced Commands**

### **1. Create a VM from XML**

```bash
virsh create <xml_file>
```

- Creates a transient (non-persistent) VM from an XML file.

### **2. Edit a VM's Configuration**

```bash
virsh edit <vm_name>
```

- Opens the VM's XML configuration file in the default editor.

### **3. Attach/Detach Devices**

- Attach a disk:

  ```bash
  virsh attach-disk <vm_name> <disk_path> <target_device> --persistent
  ```

  Example:

  ```bash
  virsh attach-disk myvm /var/lib/libvirt/images/mydisk.qcow2 vdb --persistent
  ```

- Detach a disk:

  ```bash
  virsh detach-disk <vm_name> <target_device> --persistent
  ```

### **4. Manage Snapshots**

- Create a snapshot:

  ```bash
  virsh snapshot-create-as <vm_name> <snapshot_name>
  ```

- List snapshots:

  ```bash
  virsh snapshot-list <vm_name>
  ```

- Revert to a snapshot:

  ```bash
  virsh snapshot-revert <vm_name> <snapshot_name>
  ```

### **5. Migrate a VM**

```bash
virsh migrate --live <vm_name> qemu+ssh://<remote_host>/system
```

- Migrates a running VM to another host.

---

## **Useful Options**

- **Connect to a Remote Host**:

  ```bash
  virsh --connect qemu+ssh://<remote_host>/system
  ```

- **List Commands**:

  ```bash
  virsh help
  ```

- **Get Help for a Command**:

  ```bash
  virsh help <command>
  ```

---

## **Common Files and Directories**

- **VM Disk Files**:
  `/var/lib/libvirt/images/`
- **VM Configuration Files**:
  `/etc/libvirt/qemu/`
- **Logs**:
  `/var/log/libvirt/`

---

## **Troubleshooting**

### **1. VM is Not Starting**

- Check logs:

  ```bash
  tail -f /var/log/libvirt/qemu/<vm_name>.log
  ```

### **2. Cannot Connect to Console**

- Ensure the VM has a serial console configured in its XML file:

  ```xml
  <console type='pty'>
    <target type='serial' port='0'/>
  </console>
  ```

### **3. Commands Failing for a Transient Domain**

- A transient domain is removed when stopped. Ensure the VM is persistent by defining it:

  ```bash
  virsh define <xml_file>
  ```
