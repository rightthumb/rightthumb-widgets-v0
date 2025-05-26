
def get_drive_info():
    import os
    import platform
    import psutil
    import time
    import socket
    # Get current working directory
    cwd = os.getcwd()

    # Get the drive where the current directory is located
    if platform.system() == "Windows":
        drive = os.path.splitdrive(cwd)[0]
    else:
        drive = os.path.realpath(cwd).split('/')[1]
        drive = '/' + drive
    
    # Get drive information
    drive_info = psutil.disk_usage(drive)
    capacity = drive_info.total
    used = drive_info.used
    free = drive_info.free

    # Get file system info (this includes drive serial on Windows)
    if platform.system() == "Windows":
        import wmi
        c = wmi.WMI()
        for disk in c.Win32_LogicalDisk():
            if disk.DeviceID == drive:
                model = disk.Description
                serial = disk.VolumeSerialNumber
                break
    else:
        import subprocess
        model = "N/A"
        serial = "N/A"
        # Unix-like systems do not have a standard way to get drive serial
        # For Linux, you can use 'lsblk' or 'blkid' but it requires root privileges
        try:
            result = subprocess.run(['lsblk', '-o', 'NAME,SERIAL'], stdout=subprocess.PIPE)
            output = result.stdout.decode('utf-8')
            lines = output.split('\n')
            for line in lines:
                if drive in line:
                    serial = line.split()[1]
                    break
        except Exception as e:
            serial = "N/A"
    
    # Get the computer name
    pc_name = socket.gethostname()

    # Get the current epoch time
    epoch_time = int(time.time())

    return {
        "model": model,
        "serial": serial,
        "capacity": capacity,
        "used": used,
        "free": free,
        "drive_letter_or_mount_info": drive,
        "epoch": epoch_time,
        "pc": pc_name
    }


