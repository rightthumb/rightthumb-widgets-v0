@echo off
C:\Users\Scott\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\LocalCache\local-packages\Python311\Scripts\cython.exe %*

goto :eof

encryption.pyx

# cython: language_level=3
from cryptography.fernet import Fernet

key = Fernet.generate_key()
cipher = Fernet(key)

def encrypt(data: str) -> bytes:
    return cipher.encrypt(data.encode())



cython --embed -o encryption.c encryption.pyx

gcc -shared -fPIC -o encryption.so encryption.c $(python3-config --cflags --ldflags)