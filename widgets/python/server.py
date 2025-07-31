import socket
import win32clipboard as cb
import win32con
import io
from PIL import Image
import base64

def start_server(port=9009):
    s = socket.socket()
    s.bind(('0.0.0.0', port))
    s.listen(1)
    print(f"[Server] Listening on port {port}")
    while True:
        conn, addr = s.accept()
        data = conn.recv(1024 * 1024)
        if not data:
            continue
        handle_received_clipboard(data)
        conn.close()

def handle_received_clipboard(data):
    kind, payload = data.decode(errors='ignore').split(':', 1)

    cb.OpenClipboard()
    cb.EmptyClipboard()

    if kind == 'text':
        cb.SetClipboardText(payload)
        print("[Server] Received TEXT")

    elif kind == 'file':
        import ctypes, ctypes.wintypes
        DROPFILES = ctypes.create_string_buffer(payload.encode())
        cb.SetClipboardData(win32con.CF_HDROP, DROPFILES)
        print("[Server] Received FILE")

    elif kind == 'image':
        img_bytes = base64.b64decode(payload)
        img = Image.open(io.BytesIO(img_bytes))
        output = io.BytesIO()
        img.convert("RGB").save(output, "BMP")
        bmp_data = output.getvalue()[14:]  # strip BMP header
        cb.SetClipboardData(win32con.CF_DIB, bmp_data)
        print("[Server] Received IMAGE")

    cb.CloseClipboard()
