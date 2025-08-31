import _rightThumb._construct as __;appDBA=__.clearFocus(__name__,__file__);__.appReg=appDBA;import _rightThumb._base3 as _; # type: ignore
def focus(parentApp='', childApp='', reg=True): global appDBA; f = __.appName(appDBA, parentApp, childApp); return f if reg else f
fieldSet=_.l.vars(focus(),__name__,__file__,appDBA);_.load();_v=__.imp('_rightThumb._vars')

def sw():
    pass
    _.switches.register( 'Server', '-srv' )
    _.switches.register( 'Client', '-client' )
    _.switches.register( 'AsymmetricKeys', '-keys' )
    _.switches.register( 'DownloadPublicKey', '-dl' )
_._default_settings_()

_.appInfo[focus()] = {
    'file': 'thisApp.py',
    'description': 'Changes the world',
    'categories': [
                        'DEFAULT',
                ],
    'examples': [
                        _.hp('p thisApp -file file.txt'),
                        _.linePrint(label='simple',p=0),
                        '',
    ],
    'columns': [
    ],
    'aliases': [],
    'relatedapps': [],
    'prerequisite': [],
    'notes': [],
}

_.appInfo[focus()] = _.appInfoContinuity(__.thisApp( __file__ ),_.appInfo[focus()])
_.appData[focus()] = _.appDataContinuity()
def appRegDics(): return { 'appInfo': _.appInfo[focus()], 'appData': _.appData[focus()] }

def triggers():
    _._default_triggers_()
    _.switches.trigger( 'Files',   _.isFileAdvanced, vs=False )     # Advanced File Registration    (Fn Alias Resolves To: def myFileLocations)
    _.switches.trigger( 'DB', _.aliasesFi )
    _.switches.trigger( 'Folder', _.myFolderLocations )
    _.switches.trigger( 'Folders', _.myFolderLocations )
    __.SwitchesModifier.Trigger['Folders'] = _.myFolder
    _.switches.trigger( 'OutputFolder', _.aliasesFo )
def _local_(do): exec(do)
_.l.conf('clean-pipe',True); _.l.sw.register( triggers, sw )
########################################################################################
#n)--> start

import os

def Server():
    import os, socket, pty, select, random, time, subprocess, threading
    from cryptography.hazmat.primitives import serialization, hashes # type: ignore
    from cryptography.hazmat.primitives.asymmetric import padding # type: ignore

    HOST = '127.0.0.1'

    def get_free_port():
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((HOST, 0))
            return s.getsockname()[1]

    PORT = get_free_port()
    relay_server = None
    relay = _v.yFig('remote_terminal', 'relay')
    if relay:
        relay_server = relay
    relay_port = random.randint(20000, 30000)
    private_path = os.path.expanduser('~/.rt/remote-terminal_private.pem')

    with open(private_path, "rb") as key_file:
        private_key = serialization.load_pem_private_key(key_file.read(), password=None)

    raw_pin = f"{random.randint(100000, 999999):06d}"
    PIN = f"{raw_pin[:3]}-{raw_pin[3:]}"
    _.pr(f"[+] SESSION PIN: {PIN}", c='yellow')

    def rsa_decrypt_command(encrypted_data):
        return private_key.decrypt(
            encrypted_data,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        ).decode()

    def run_terminal_session(conn):
        pid, fd = pty.fork()
        if pid == 0:
            os.execv('/bin/bash', ['bash', '-i', '-l'])
        else:
            pin_verified = False
            while True:
                rlist, _, _ = select.select([conn, fd], [], [])
                if conn in rlist:
                    try:
                        incoming = conn.recv(4096)
                        if not incoming:
                            break
                        if not pin_verified:
                            if incoming.decode().strip() == raw_pin:
                                conn.send(b'[+] PIN Verified\n')
                                pin_verified = True
                            else:
                                conn.send(b'[!] INVALID PIN\n')
                            continue
                        if incoming.strip() == b'__CTRL_C__':
                            os.write(fd, b'\x03')
                        else:
                            cmd = rsa_decrypt_command(incoming).strip() + '\n'
                            os.write(fd, cmd.encode())
                    except Exception as e:
                        conn.send(f'[ERROR] {e}\n'.encode())
                if fd in rlist:
                    try:
                        output = os.read(fd, 1024)
                        if not output:
                            break
                        conn.send(output)
                    except Exception:
                        break

    def start_server():
        if relay_server:
            cmd = [
                "ssh", "-o", "ExitOnForwardFailure=yes", "-fN",
                "-R", f"{relay_port}:localhost:{PORT}", relay_server
            ]
            try:
                subprocess.check_call(cmd)
                _.pr(f"[+] Relay active: {relay_server}:{relay_port}", c='green')
            except subprocess.CalledProcessError as e:
                _.pr(f"[!] SSH tunnel failed: {e}")
                return

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((HOST, PORT))
            s.listen(1)
            _.pr(f"[+] Ready on {HOST}:{PORT}", c='purple')
            conn, addr = s.accept()
            _.pr(f"[+] Connected: {addr}", c='purple')
            with conn:
                run_terminal_session(conn)

    if __name__ == "__main__":
        start_server()

def Client():
    _.pr('CTRL+X  Behaves like CTRL+C to force quit remote commands\n\n', c='yellow')
    import socket
    import threading
    import sys
    import platform
    from cryptography.hazmat.primitives import serialization, hashes # type: ignore
    from cryptography.hazmat.primitives.asymmetric import padding # type: ignore

    relay_server = None
    relay = _v.yFig('remote_terminal', 'relay')
    if relay:
        relay_server = relay
    relay_port = int(input('Port: '))
    PIN = input("Enter PIN (e.g. 123-456): ").replace('-', '')

    public_path = os.path.expanduser('~/.rt/remote-terminal_public.pem')

    with open(public_path, "rb") as f:
        public_key = serialization.load_pem_public_key(f.read())

    def encrypt_command(command):
        return public_key.encrypt(
            command.encode(),
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )

    def receive_output(sock):
        global skip_first_line
        skip_first_line = False
        while True:
            try:
                data = sock.recv(1024)
                if data:
                    text = data.decode(errors='ignore')
                    if skip_first_line:
                        # print('skipped first line')
                        text = '\n'.join(text.split('\n')[1:])
                        skip_first_line = False
                    sys.stdout.write(text)
                    sys.stdout.flush()
            except Exception:
                break

    def interactive_input(sock):
        global skip_first_line
        if platform.system() == 'Windows':
            import msvcrt
            buffer = ''
            try:
                while True:
                    if msvcrt.kbhit():
                        ch = msvcrt.getch()
                        if ch == b'\x18':  # Ctrl+X
                            sys.stdout.write("\n[+] Sending CTRL signal\n")
                            sys.stdout.flush()
                            sock.sendall(b'__CTRL_C__')
                            buffer = ''
                        elif ch in (b'\r', b'\n'):  # Enter
                            sys.stdout.write('\n')
                            sys.stdout.flush()
                            if buffer.strip():
                                encrypted = encrypt_command(buffer)
                                sock.sendall(encrypted)
                                skip_first_line = True
                            buffer = ''
                        elif ch == b'\x08':  # Backspace
                            if buffer:
                                buffer = buffer[:-1]
                                sys.stdout.write('\b \b')
                                sys.stdout.flush()
                        elif ch == b'\xe0':
                            msvcrt.getch()  # Ignore arrow key prefix
                        else:
                            try:
                                decoded = ch.decode()
                                buffer += decoded
                                sys.stdout.write(decoded)
                                sys.stdout.flush()
                            except:
                                pass
            except KeyboardInterrupt:
                sys.stdout.write("\n[+] Disconnected.\n")
                sys.stdout.flush()
                sock.close()
        else:
            import tty, termios, select
            stdin_fd = sys.stdin.fileno()
            old_settings = termios.tcgetattr(stdin_fd)
            tty.setcbreak(stdin_fd)
            buffer = ''
            try:
                while True:
                    if select.select([sys.stdin], [], [], 0.1)[0]:
                        ch = sys.stdin.read(1)
                        if ch == '\x18':
                            sys.stdout.write("\n[+] Sending CTRL signal\n")
                            sys.stdout.flush()
                            sock.sendall(b'__CTRL_C__')
                            buffer = ''
                        elif ch in ('\r', '\n'):
                            sys.stdout.write('\n')
                            sys.stdout.flush()
                            if buffer.strip():
                                encrypted = encrypt_command(buffer)
                                sock.sendall(encrypted)
                                skip_first_line = True
                            buffer = ''
                        elif ch == '\x7f':
                            if buffer:
                                buffer = buffer[:-1]
                                sys.stdout.write('\b \b')
                                sys.stdout.flush()
                        else:
                            buffer += ch
                            sys.stdout.write(ch)
                            sys.stdout.flush()
            finally:
                termios.tcsetattr(stdin_fd, termios.TCSADRAIN, old_settings)

    host = relay_server
    port = relay_port
    _.pr(f"[+] Connecting to {host}:{port}...")

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        s.sendall(PIN.encode())
        sys.stdout.write(s.recv(1024).decode())
        sys.stdout.flush()

        threading.Thread(target=receive_output, args=(s,), daemon=True).start()
        interactive_input(s)




def AsymmetricKeys0():
    import os
    from cryptography.hazmat.primitives.asymmetric import rsa  # type: ignore
    from cryptography.hazmat.primitives import serialization   # type: ignore

    home_dir = os.path.expanduser('~/.rt')
    os.makedirs(home_dir, exist_ok=True)  # Ensure the directory exists

    private_path = os.path.join(home_dir, 'remote-terminal_private.pem')
    public_path = os.path.join(home_dir, 'remote-terminal_public.pem')

    private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    public_key = private_key.public_key()

    with open(private_path, "wb") as f:
        f.write(private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.TraditionalOpenSSL,
            encryption_algorithm=serialization.NoEncryption()
        ))

    with open(public_path, "wb") as f:
        f.write(public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        ))


def AsymmetricKeys():
    import os
    import random
    import requests
    from cryptography.hazmat.primitives.asymmetric import rsa  # type: ignore
    from cryptography.hazmat.primitives import serialization   # type: ignore

    # Set the upload URL
    upload_url = 'https://yourserver.example.com/upload'  # ← Update this with your server
    url = _v.yFig('remote_terminal', 'url')
    if url:
        upload_url = url


    # Create ~/.rt directory if it doesn't exist
    home_dir = os.path.expanduser('~/.rt')
    os.makedirs(home_dir, exist_ok=True)

    # File paths
    private_path = os.path.join(home_dir, 'remote-terminal_private.pem')
    public_path = os.path.join(home_dir, 'remote-terminal_public.pem')

    # Generate RSA key pair
    private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    public_key = private_key.public_key()

    # Save private key
    with open(private_path, "wb") as f:
        f.write(private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.TraditionalOpenSSL,
            encryption_algorithm=serialization.NoEncryption()
        ))

    # Save public key
    with open(public_path, "wb") as f:
        pub_bytes = public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )
        f.write(pub_bytes)

    # Generate a 5-digit code with dash after 2nd digit
    digits = ''.join(str(random.randint(0, 9)) for _ in range(5))
    code = digits[:2] + '-' + digits[2:]
    print(f"[+] Generated code: {code}")

    # Upload public key
    try:
        response = requests.post(
            f"{upload_url}?code={code}",
            data=pub_bytes,
            headers={'Content-Type': 'application/x-pem-file'}
        )
        response.raise_for_status()
        print("[+] Public key uploaded successfully.")
    except Exception as e:
        print(f"[!] Failed to upload public key: {e}")



def DownloadPublicKey():
    import os
    import requests

    # Prompt for PIN (e.g., 12-345)
    pin = input("Enter the 5-digit code (format: ##-###): ").strip()

    # Define download URL (modify as needed to match your server logic)
    download_url = f"https://yourserver.example.com/public"
    url = _v.yFig('remote_terminal', 'url')
    if url:
        download_url = url
    download_url += f"?code={pin}"
    # Output path
    public_path = os.path.expanduser('~/.rt/remote-terminal_public.pem')
    os.makedirs(os.path.dirname(public_path), exist_ok=True)

    # Attempt download
    try:
        response = requests.get(download_url)
        response.raise_for_status()
        with open(public_path, 'wb') as f:
            f.write(response.content)
        print("[+] Public key downloaded and saved.")
    except Exception as e:
        print(f"[!] Failed to download public key: {e}")



















































### secure_terminal_server.py (RSA + PTY + PIN handshake only, relay fix)
import os

def Server():
    import os, socket, pty, select, random, subprocess, threading
    from cryptography.hazmat.primitives import serialization, hashes  # type: ignore
    from cryptography.hazmat.primitives.asymmetric import padding  # type: ignore

    HOST = '127.0.0.1'

    def get_free_port():
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((HOST, 0))
            return s.getsockname()[1]

    PORT = get_free_port()
    relay_server = None
    relay = _v.yFig('remote_terminal', 'relay')
    if relay:
        relay_server = relay
    relay_port = random.randint(20000, 30000)
    private_path = os.path.expanduser('~/.rt/remote-terminal_private.pem')

    with open(private_path, "rb") as key_file:
        private_key = serialization.load_pem_private_key(key_file.read(), password=None)

    raw_pin = f"{random.randint(100000, 999999):06d}"
    PIN = f"{raw_pin[:3]}-{raw_pin[3:]}"
    _.pr(f"[+] SESSION PIN: {PIN}", c='yellow')

    def rsa_decrypt_command(encrypted_data):
        return private_key.decrypt(
            encrypted_data,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        ).decode()

    def run_terminal_session(conn):
        pid, fd = pty.fork()
        if pid == 0:
            os.execv('/bin/bash', ['bash', '-i', '-l'])
        else:
            pin_verified = False
            while True:
                rlist, _, _ = select.select([conn, fd], [], [])
                if conn in rlist:
                    try:
                        incoming = conn.recv(4096)
                        if not incoming:
                            break
                        if not pin_verified:
                            if incoming.decode().strip() == raw_pin:
                                conn.send(b'[+] PIN Verified\n')
                                pin_verified = True
                            else:
                                conn.send(b'[!] INVALID PIN\n')
                            continue
                        if incoming.strip() == b'__CTRL_C__':
                            os.write(fd, b'\x03')
                        else:
                            cmd = rsa_decrypt_command(incoming).strip() + '\n'
                            os.write(fd, cmd.encode())
                    except Exception as e:
                        conn.send(f'[ERROR] {e}\n'.encode())
                if fd in rlist:
                    try:
                        output = os.read(fd, 1024)
                        if not output:
                            break
                        conn.send(output)
                    except Exception:
                        break

    def start_server():
        if relay_server:
            cmd = [
                "ssh", "-o", "ExitOnForwardFailure=yes", "-fN",
                "-R", f"{relay_port}:localhost:{PORT}", relay_server
            ]
            try:
                subprocess.check_call(cmd)
                _.pr(f"[+] Relay active: {relay_server}:{relay_port}", c='green')
            except subprocess.CalledProcessError as e:
                _.pr(f"[!] SSH tunnel failed: {e}")
                return

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((HOST, PORT))
            s.listen(1)
            _.pr(f"[+] Ready on {HOST}:{PORT}", c='purple')
            conn, addr = s.accept()
            _.pr(f"[+] Connected: {addr}", c='purple')
            # _.pr()
            # _.pr(relay_port, h='orange')
            # _.pr(PIN, h='orange')
            # _.pr()
            with conn:
                run_terminal_session(conn)

    if __name__ == "__main__":
        start_server()


def Client():
    _.pr('CTRL+X  Behaves like CTRL+C to force quit remote commands\n\n', c='yellow')
    import socket
    import threading
    import sys
    import platform
    from cryptography.hazmat.primitives import serialization, hashes  # type: ignore
    from cryptography.hazmat.primitives.asymmetric import padding  # type: ignore

    relay_server = None
    relay = _v.yFig('remote_terminal', 'relay')
    if relay:
        relay_server = relay
    relay_port = int(input('Port: '))
    PIN = input("Enter PIN (e.g. 123-456): ").replace('-', '')

    public_path = os.path.expanduser('~/.rt/remote-terminal_public.pem')

    with open(public_path, "rb") as f:
        public_key = serialization.load_pem_public_key(f.read())

    def encrypt_command(command):
        return public_key.encrypt(
            command.encode(),
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )

    def receive_output(sock):
        global skip_first_line
        skip_first_line = False
        while True:
            try:
                data = sock.recv(1024)
                if data:
                    text = data.decode(errors='ignore')
                    if skip_first_line:
                        text = '\n'.join(text.split('\n')[1:])
                        skip_first_line = False
                    sys.stdout.write(text)
                    sys.stdout.flush()
            except Exception:
                break

    def interactive_input(sock):
        global skip_first_line
        if platform.system() == 'Windows':
            import msvcrt
            buffer = ''
            try:
                while True:
                    if msvcrt.kbhit():
                        ch = msvcrt.getch()
                        if ch == b'\x18':
                            sys.stdout.write("\n[+] Sending CTRL signal\n")
                            sys.stdout.flush()
                            sock.sendall(b'__CTRL_C__')
                            buffer = ''
                        elif ch in (b'\r', b'\n'):
                            sys.stdout.write('\n')
                            sys.stdout.flush()
                            if buffer.strip():
                                encrypted = encrypt_command(buffer)
                                sock.sendall(encrypted)
                                skip_first_line = True
                            buffer = ''
                        elif ch == b'\x08':
                            if buffer:
                                buffer = buffer[:-1]
                                sys.stdout.write('\b \b')
                                sys.stdout.flush()
                        elif ch == b'\xe0':
                            msvcrt.getch()
                        else:
                            try:
                                decoded = ch.decode()
                                buffer += decoded
                                sys.stdout.write(decoded)
                                sys.stdout.flush()
                            except:
                                pass
            except KeyboardInterrupt:
                sys.stdout.write("\n[+] Disconnected.\n")
                sys.stdout.flush()
                sock.close()
        else:
            import tty, termios, select
            stdin_fd = sys.stdin.fileno()
            old_settings = termios.tcgetattr(stdin_fd)
            tty.setraw(stdin_fd)
            buffer = ''
            try:
                while True:
                    if select.select([sys.stdin], [], [], 0.1)[0]:
                        ch = sys.stdin.read(1)
                        if ch == '\x18':
                            sys.stdout.write("\n[+] Sending CTRL signal\n")
                            sys.stdout.flush()
                            sock.sendall(b'__CTRL_C__')
                            buffer = ''
                        elif ch in ('\r', '\n'):
                            sys.stdout.write('\n')
                            sys.stdout.flush()
                            if buffer.strip():
                                encrypted = encrypt_command(buffer)
                                sock.sendall(encrypted)
                                skip_first_line = True
                            buffer = ''
                        elif ch == '\x7f':
                            if buffer:
                                buffer = buffer[:-1]
                                sys.stdout.write('\b \b')
                                sys.stdout.flush()
                        elif ch == '\t':
                            try:
                                prefix = buffer.strip().split()[-1] if buffer.strip() else ''
                                matches = [cmd for cmd in os.listdir('/bin') if cmd.startswith(prefix)]
                                if matches:
                                    completion = matches[0][len(prefix):]
                                    buffer += completion
                                    sys.stdout.write(completion)
                                    sys.stdout.flush()
                            except:
                                pass
                        else:
                            buffer += ch
                            sys.stdout.write(ch)
                            sys.stdout.flush()
            finally:
                termios.tcsetattr(stdin_fd, termios.TCSADRAIN, old_settings)

    host = relay_server
    port = relay_port
    _.pr(f"[+] Connecting to {host}:{port}...")

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        s.sendall(PIN.encode())
        sys.stdout.write(s.recv(1024).decode())
        sys.stdout.flush()

        threading.Thread(target=receive_output, args=(s,), daemon=True).start()
        interactive_input(s)























































def Client():
    _.pr('CTRL+X  Behaves like CTRL+C to force quit remote commands\n\n', c='yellow')
    import socket
    import threading
    import sys
    import platform
    import os
    from cryptography.hazmat.primitives import serialization, hashes  # type: ignore
    from cryptography.hazmat.primitives.asymmetric import padding  # type: ignore

    relay_server = None
    relay = _v.yFig('remote_terminal', 'relay')
    if relay:
        relay_server = relay
    relay_port = int(input('Port: '))
    PIN = input("Enter PIN (e.g. 123-456): ").replace('-', '')

    public_path = os.path.expanduser('~/.rt/remote-terminal_public.pem')

    with open(public_path, "rb") as f:
        public_key = serialization.load_pem_public_key(f.read())

    def encrypt_command(command):
        return public_key.encrypt(
            command.encode(),
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )

    def receive_output(sock):
        global skip_first_line
        skip_first_line = False
        while True:
            try:
                data = sock.recv(1024)
                if data:
                    text = data.decode(errors='ignore')
                    if skip_first_line:
                        text = '\n'.join(text.split('\n')[1:])
                        skip_first_line = False
                    sys.stdout.write(text)
                    sys.stdout.flush()
            except Exception:
                break

    def interactive_input(sock):
        global skip_first_line
        if platform.system() == 'Windows':
            import msvcrt
            buffer = ''
            try:
                while True:
                    if msvcrt.kbhit():
                        ch = msvcrt.getch()
                        if ch == b'\x18':  # Ctrl+X
                            sys.stdout.write("\n[+] Sending CTRL signal\n")
                            sys.stdout.flush()
                            sock.sendall(b'__CTRL_C__')
                            buffer = ''
                        elif ch in (b'\r', b'\n'):  # Enter
                            sys.stdout.write('\n')
                            sys.stdout.flush()
                            if buffer.strip():
                                encrypted = encrypt_command(buffer)
                                sock.sendall(encrypted)
                                skip_first_line = True
                            buffer = ''
                        elif ch == b'\x08':  # Backspace
                            if buffer:
                                buffer = buffer[:-1]
                                sys.stdout.write('\b \b')
                                sys.stdout.flush()
                        elif ch == b'\t':  # Tab key (no autocomplete on Windows)
                            pass
                        elif ch == b'\xe0':
                            msvcrt.getch()  # Swallow next key (arrow keys)
                        else:
                            try:
                                decoded = ch.decode()
                                buffer += decoded
                                sys.stdout.write(decoded)
                                sys.stdout.flush()
                            except:
                                pass
            except KeyboardInterrupt:
                sys.stdout.write("\n[+] Disconnected.\n")
                sys.stdout.flush()
                sock.close()
        else:
            import tty, termios, select
            stdin_fd = sys.stdin.fileno()
            old_settings = termios.tcgetattr(stdin_fd)
            tty.setraw(stdin_fd)
            buffer = ''
            try:
                while True:
                    if select.select([sys.stdin], [], [], 0.1)[0]:
                        ch = sys.stdin.read(1)
                        if ch == '\x18':
                            sys.stdout.write("\n[+] Sending CTRL signal\n")
                            sys.stdout.flush()
                            sock.sendall(b'__CTRL_C__')
                            buffer = ''
                        elif ch in ('\r', '\n'):
                            sys.stdout.write('\n')
                            sys.stdout.flush()
                            if buffer.strip():
                                encrypted = encrypt_command(buffer)
                                sock.sendall(encrypted)
                                skip_first_line = True
                            buffer = ''
                        elif ch == '\x7f':
                            if buffer:
                                buffer = buffer[:-1]
                                sys.stdout.write('\b \b')
                                sys.stdout.flush()
                        elif ch == '\t':
                            print('tab pressed')
                            try:
                                import readline
                                readline.insert_text(buffer)
                                readline.redisplay()
                            except:
                                pass
                        else:
                            buffer += ch
                            sys.stdout.write(ch)
                            sys.stdout.flush()
            finally:
                termios.tcsetattr(stdin_fd, termios.TCSADRAIN, old_settings)

    host = relay_server
    port = relay_port
    _.pr(f"[+] Connecting to {host}:{port}...")

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        s.sendall(PIN.encode())
        sys.stdout.write(s.recv(1024).decode())
        sys.stdout.flush()

        threading.Thread(target=receive_output, args=(s,), daemon=True).start()
        interactive_input(s)
























def action():
    if _.switches.isActive('AsymmetricKeys'):
        AsymmetricKeys()
    elif _.switches.isActive('Server'):
        Server()
    elif _.switches.isActive('Client'):
        Client()
    elif _.switches.isActive('DownloadPublicKey'):
        DownloadPublicKey()





'''
<?php
$storageDir = __DIR__ . '/public_keys';
if (!is_dir($storageDir)) mkdir($storageDir, 0755, true);

$code = isset($_GET['code']) ? preg_replace('/[^a-zA-Z0-9_\-]/', '', $_GET['code']) : null;

// ===== POST: Upload =====
if ($_SERVER['REQUEST_METHOD'] === 'POST' && $code) {
    $data = file_get_contents('php://input');
    if (!$data || trim($data) === '') {
        http_response_code(400);
        echo 'Empty upload';
        exit;
    }

    $path = "$storageDir/$code.pem";
    if (file_put_contents($path, $data) === false) {
        http_response_code(500);
        echo 'Failed to save file';
    } else {
        echo 'OK';
    }
    exit;
}

// ===== GET: Download =====
if ($_SERVER['REQUEST_METHOD'] === 'GET' && $code) {
    $path = "$storageDir/$code.pem";
    if (is_file($path)) {
        header('Content-Type: application/x-pem-file');
        header('Content-Disposition: inline; filename="remote-terminal_public.pem"');
        readfile($path);
    } else {
        http_response_code(404);
        echo 'NOT FOUND';
    }
    exit;
}

// ===== Fallback =====
http_response_code(400);
echo 'BAD REQUEST';


'''


########################################################################################
if __name__ == '__main__':
    action(); _.isExit(__file__)