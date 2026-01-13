#!/usr/bin/env python3

import sys
import argparse
import base64
import os
import hashlib
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

def md5_to_32bytes(password: str) -> bytes:
	"""
	Rust app logic: MD5 the password (16 bytes),
	then pad to a 32-byte key by adding 16 zeros.
	"""
	md5_hash = hashlib.md5(password.encode("utf-8")).digest()  # 16 bytes
	return md5_hash + b"\x00" * 16  # total 32 bytes

def encrypt(plaintext: str, key: bytes) -> str:
	"""
	Encrypt plaintext with AES-256-GCM:
	1. Generate 12-byte random nonce
	2. Encrypt plaintext as UTF-8
	3. Prepend nonce to ciphertext
	4. Base64-encode
	Returns base64 string
	"""
	aesgcm = AESGCM(key)
	nonce = os.urandom(12)  # 12-byte GCM nonce
	ciphertext = aesgcm.encrypt(nonce, plaintext.encode("utf-8"), None)
	# Prepend nonce, then base64
	combined = nonce + ciphertext
	return base64.b64encode(combined).decode("utf-8")

def decrypt(ciphertext_b64: str, key: bytes) -> str:
	"""
	Decrypt a base64-encoded string:
	1. Base64-decode
	2. First 12 bytes are the nonce
	3. Remainder is ciphertext
	4. Decrypt
	Returns UTF-8 plaintext
	"""
	combined = base64.b64decode(ciphertext_b64)
	if len(combined) < 12:
		raise ValueError("Ciphertext too short (Base64).")
	nonce = combined[:12]
	ciphertext = combined[12:]
	aesgcm = AESGCM(key)
	plaintext_bytes = aesgcm.decrypt(nonce, ciphertext, None)
	return plaintext_bytes.decode("utf-8")

def decrypt_raw(ciphertext_raw: bytes, key: bytes) -> str:
	"""
	Decrypt raw AES-GCM bytes (nonce + ciphertext).
	1. First 12 bytes are the nonce
	2. Remainder is ciphertext
	3. Decrypt
	Returns UTF-8 plaintext
	"""
	if len(ciphertext_raw) < 12:
		raise ValueError("Ciphertext too short (raw).")
	nonce = ciphertext_raw[:12]
	ciphertext = ciphertext_raw[12:]
	aesgcm = AESGCM(key)
	plaintext_bytes = aesgcm.decrypt(nonce, ciphertext, None)
	return plaintext_bytes.decode("utf-8")

def main():
	if len(sys.argv) > 1 and sys.argv[1] == "cry":
		sys.argv.pop(1)    
	parser = argparse.ArgumentParser(
		description="AES-256-GCM with MD5-based key, compatible with the Rust cryptor app."
	)
	parser.add_argument("-p", "--password", required=True, help="Encryption/Decryption password")
	parser.add_argument("-e", "--encrypt", nargs="?", const="", metavar="TEXT", 
						help="Encrypt the given TEXT (if no TEXT, read from stdin)")
	parser.add_argument("-d", "--decrypt", nargs="?", const="", metavar="TEXT",
						help="Decrypt the given BASE64 string (if no TEXT, read from stdin)")
	parser.add_argument("-enFi", help="Encrypt contents of a file")
	parser.add_argument("-deFi", help="Decrypt contents of a file (Base64 or raw bytes)")
	parser.add_argument("-o", "--output", help="Output file (otherwise prints to stdout)")

	args = parser.parse_args()

	# Derive key (same as Rust)
	key = md5_to_32bytes(args.password)

	# Decide mode:
	mode_count = sum([
		1 if args.encrypt is not None else 0,
		1 if args.decrypt is not None else 0,
		1 if args.encrypt_file else 0,
		1 if args.decrypt_file else 0
	])
	if mode_count == 0:
		print("You must specify an encryption or decryption action.")
		sys.exit(1)
	if mode_count > 1:
		print("Please specify only one action at a time.")
		sys.exit(1)

	# ---------------
	# ENCRYPT STRING
	# ---------------
	if args.encrypt is not None:
		if args.encrypt == "":
			# If user typed "-e" without text, read plaintext from stdin
			plaintext = sys.stdin.read()
		else:
			plaintext = args.encrypt

		encrypted_b64 = encrypt(plaintext, key)
		if args.output:
			with open(args.output, "wb") as fout:
				fout.write(encrypted_b64)

		else:
			print(encrypted_b64)
		return

	# ---------------
	# DECRYPT STRING
	# ---------------
	if args.decrypt is not None:
		if args.decrypt == "":
			# read base64 from stdin
			ciphertext_b64 = sys.stdin.read()
		else:
			ciphertext_b64 = args.decrypt

		try:
			decrypted = decrypt(ciphertext_b64, key)
			if args.output:
				with open(args.output, "w", encoding="utf-8") as f:
					f.write(decrypted)
			else:
				print(decrypted)
		except Exception as e:
			print("Decryption error:", e)
		return

	# -----------------
	# ENCRYPT A FILE
	# -----------------
	if args.encrypt_file:
		try:
			with open(args.encrypt_file, "rb") as f:
				data = f.read()
			# Convert data to a UTF-8 string
			plaintext = data.decode("utf-8", errors="replace")

			encrypted_b64 = encrypt(plaintext, key)
			if args.output:
				with open(args.output, "w", encoding="utf-8") as fout:
					fout.write(encrypted_b64)
			else:
				print(encrypted_b64)
		except Exception as e:
			print(f"Error encrypting file '{args.encrypt_file}':", e)
		return

	# -----------------
	# DECRYPT A FILE
	# -----------------
	if args.decrypt_file:
		try:
			with open(args.decrypt_file, "rb") as f:
				data = f.read()

			# We'll guess base64 if it looks like base64
			is_b64 = all((c in b"ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=\n\r") 
						for c in data)

			try:
				if is_b64:
					# Decrypt as base64
					ciphertext_b64 = data.decode("utf-8", errors="ignore").replace("\n", "").replace("\r", "")
					decrypted = decrypt(ciphertext_b64, key)
				else:
					# Decrypt raw AES-GCM bytes
					decrypted = decrypt_raw(data, key)
			except Exception as e:
				print(f"Decryption error: {e}")
				return

			if args.output:
				with open(args.output, "wb") as fout:
					fout.write(decrypted.encode("utf-8"))

			else:
				print(decrypted)

		except Exception as e:
			print(f"Error decrypting file '{args.decrypt_file}':", e)
		return

if __name__ == "__main__":
	main()