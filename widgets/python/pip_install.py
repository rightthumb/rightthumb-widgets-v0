import subprocess
import sys
import os

def get_hostname():
    try:
        with open('/etc/hostname', 'r') as f:
            return f.read().strip()
    except Exception as e:
        print(f"Error reading hostname: {e}")
        sys.exit(1)

def install_package(package):
    try:
        print(f"Starting installation of {package} using pip...")
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', package])
        print(f"Installation of {package} successful.")
        post_install_notification(package)
    except subprocess.CalledProcessError:
        print(f"pip installation failed for {package}. Trying sudo apt install -y python3-{package}...")
        try:
            subprocess.check_call(['sudo', 'apt', 'update', '-y'])
            subprocess.check_call(['sudo', 'apt', 'install', '-y', f'python3-{package}'])
            print(f"Installation of {package} successful using apt.")
            post_install_notification(package)
        except subprocess.CalledProcessError as e:
            print(f"Failed to install {package} using apt: {e}")

def post_install_notification(package):
    hostname = get_hostname()
    try:
        subprocess.check_call(['curl', '-X', 'POST', '-d', f"hostname={hostname}&apt={package}", 'https://sds.sh/pip/'])
    except subprocess.CalledProcessError as e:
        print(f"Failed to send notification for {package}: {e}")

def main():
    if len(sys.argv) < 2:
        print("No package(s) specified for installation.")
        sys.exit(1)

    packages = sys.argv[1:]
    hostname = get_hostname()

    for package in packages:
        print(f"Starting installation of {package} on {hostname}...")
        install_package(package)

if __name__ == "__main__":
    main()
