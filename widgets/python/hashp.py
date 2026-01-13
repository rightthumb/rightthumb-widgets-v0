import hashlib
import getpass

def hash_text(text: str):
    md5 = hashlib.md5(text.encode('utf-8')).hexdigest()
    sha1 = hashlib.sha1(text.encode('utf-8')).hexdigest()
    return md5, sha1

def main():
    secret = getpass.getpass("Enter text to hash: ")
    md5, sha1 = hash_text(secret)

    print("\nResults:")
    print(f"MD5 :  {md5}")
    print(f"SHA1:  {sha1}")

if __name__ == "__main__":
    main()
