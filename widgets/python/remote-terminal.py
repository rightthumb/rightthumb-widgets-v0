import _rightThumb._construct as __;appDBA=__.clearFocus(__name__,__file__);__.appReg=appDBA;import _rightThumb._base3 as _; # type: ignore
def focus(parentApp='', childApp='', reg=True): global appDBA; f = __.appName(appDBA, parentApp, childApp); return f if reg else f
fieldSet=_.l.vars(focus(),__name__,__file__,appDBA);_.load();_v=__.imp('_rightThumb._vars')

def sw():
    pass
    _.switches.register( 'Files', '-f,-fi,-file,-files','file.txt', isData='glob,name,data,clean', description='Files', isRequired=False )
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


### secure_terminal_server.py (RSA + PTY + PIN handshake only, relay fix)
import sys
if '-srv' in sys.argv:
    import os, socket, pty, select, random, time, subprocess, threading
    from cryptography.hazmat.primitives import serialization, hashes
    from cryptography.hazmat.primitives.asymmetric import padding

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

    with open("private.pem", "rb") as key_file:
        private_key = serialization.load_pem_private_key(key_file.read(), password=None)

    raw_pin = f"{random.randint(100000, 999999):06d}"
    PIN = f"{raw_pin[:3]}-{raw_pin[3:]}"
    print(f"[+] SESSION PIN: {PIN}")

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
                print(f"[+] Relay active: {relay_server}:{relay_port}")
            except subprocess.CalledProcessError as e:
                print(f"[!] SSH tunnel failed: {e}")
                return

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((HOST, PORT))
            s.listen(1)
            print(f"[+] Connected: {addr}")
            print(f"[+] Ready on {HOST}:{PORT}")
            conn, addr = s.accept()
            with conn:
                run_terminal_session(conn)

    if __name__ == "__main__":
        start_server()

if '-client' in sys.argv:
    import socket
    import threading
    import sys
    import platform
    from cryptography.hazmat.primitives import serialization, hashes
    from cryptography.hazmat.primitives.asymmetric import padding

    relay_server = None
    relay = _v.yFig('remote_terminal', 'relay')
    if relay:
        relay_server = relay
    relay_port = int(input('Port: '))
    PIN = input("Enter PIN (e.g. 123-456): ").replace('-', '')

    with open("public.pem", "rb") as f:
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
        while True:
            try:
                data = sock.recv(1024)
                if data:
                    print(data.decode(errors='ignore'), end='', flush=True)
            except Exception:
                break

    def interactive_input(sock):
        buffer = ''
        if platform.system() == 'Windows':
            import msvcrt
            while True:
                if msvcrt.kbhit():
                    char = msvcrt.getch()
                    if char == b'\x18':  # Ctrl+X
                        print("\n[+] Sending CTRL signal")
                        sock.sendall(b'__CTRL_C__')
                        buffer = ''
                        continue
                    elif char in (b'\r', b'\n'):
                        print()
                        if buffer.strip():
                            encrypted = encrypt_command(buffer.strip())
                            sock.sendall(encrypted)
                        buffer = ''
                    elif char == b'\x08':  # Backspace
                        if buffer:
                            buffer = buffer[:-1]
                            sys.stdout.write('\b \b')
                            sys.stdout.flush()
                    else:
                        try:
                            decoded = char.decode()
                            buffer += decoded
                            sys.stdout.write(decoded)
                            sys.stdout.flush()
                        except:
                            pass
        else:
            import tty, termios, select
            stdin_fd = sys.stdin.fileno()
            old_settings = termios.tcgetattr(stdin_fd)
            tty.setcbreak(stdin_fd)
            try:
                while True:
                    if select.select([sys.stdin], [], [], 0.1)[0]:
                        ch = sys.stdin.read(1)
                        if ch == '\x18':  # Ctrl+X
                            print("\n[+] Sending CTRL signal")
                            sock.sendall(b'__CTRL_C__')
                            buffer = ''
                        elif ch in ('\r', '\n'):
                            print()
                            if buffer.strip():
                                encrypted = encrypt_command(buffer.strip())
                                sock.sendall(encrypted)
                            buffer = ''
                        elif ch == '\x7f':  # Backspace
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
    print(f"[+] Connecting to {host}:{port}...")

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        s.sendall(PIN.encode())
        print(s.recv(1024).decode())

        threading.Thread(target=receive_output, args=(s,), daemon=True).start()
        interactive_input(s)




def action():
    pass

########################################################################################
if __name__ == '__main__':
    action(); _.isExit(__file__)