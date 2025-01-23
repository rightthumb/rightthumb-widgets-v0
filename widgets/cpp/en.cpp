#include <iostream>
#include <openssl/evp.h>
#include <openssl/rand.h>
#include <openssl/err.h>
#include <vector>
#include <cstring>

void handleErrors() {
    ERR_print_errors_fp(stderr);
    abort();
}

std::vector<unsigned char> deriveKey(const std::string& passphrase, unsigned char* salt) {
    std::vector<unsigned char> key(32);
    if (!PKCS5_PBKDF2_HMAC(passphrase.c_str(), passphrase.length(), salt, 8, 10000, EVP_sha256(), 32, key.data())) {
        handleErrors();
    }
    return key;
}

std::vector<unsigned char> encrypt(const std::string& plaintext, const std::string& passphrase) {
    unsigned char salt[8];
    RAND_bytes(salt, 8);
    auto key = deriveKey(passphrase, salt);
    
    EVP_CIPHER_CTX* ctx = EVP_CIPHER_CTX_new();
    if (!ctx) handleErrors();
    
    std::vector<unsigned char> iv(16);
    RAND_bytes(iv.data(), iv.size());
    std::vector<unsigned char> ciphertext(8 + iv.size() + plaintext.size() + 16);
    
    std::copy(salt, salt + 8, ciphertext.begin());
    std::copy(iv.begin(), iv.end(), ciphertext.begin() + 8);
    
    if (1 != EVP_EncryptInit_ex(ctx, EVP_aes_256_cbc(), nullptr, key.data(), iv.data())) handleErrors();
    
    int len;
    if (1 != EVP_EncryptUpdate(ctx, ciphertext.data() + 8 + iv.size(), &len, (unsigned char*)plaintext.c_str(), plaintext.size())) handleErrors();
    
    int ciphertext_len = len;
    if (1 != EVP_EncryptFinal_ex(ctx, ciphertext.data() + 8 + iv.size() + len, &len)) handleErrors();
    ciphertext_len += len;
    
    ciphertext.resize(8 + iv.size() + ciphertext_len);
    EVP_CIPHER_CTX_free(ctx);
    
    return ciphertext;
}

std::string decrypt(const std::vector<unsigned char>& ciphertext, const std::string& passphrase) {
    unsigned char salt[8];
    std::copy(ciphertext.begin(), ciphertext.begin() + 8, salt);
    auto key = deriveKey(passphrase, salt);
    
    EVP_CIPHER_CTX* ctx = EVP_CIPHER_CTX_new();
    if (!ctx) handleErrors();
    
    std::vector<unsigned char> iv(16);
    std::copy(ciphertext.begin() + 8, ciphertext.begin() + 8 + iv.size(), iv.begin());
    std::vector<unsigned char> plaintext(ciphertext.size() - 8 - iv.size());
    
    if (1 != EVP_DecryptInit_ex(ctx, EVP_aes_256_cbc(), nullptr, key.data(), iv.data())) handleErrors();
    
    int len;
    if (1 != EVP_DecryptUpdate(ctx, plaintext.data(), &len, ciphertext.data() + 8 + iv.size(), ciphertext.size() - 8 - iv.size())) handleErrors();
    
    int plaintext_len = len;
    if (1 != EVP_DecryptFinal_ex(ctx, plaintext.data() + len, &len)) {
        EVP_CIPHER_CTX_free(ctx);
        return "[Decryption Failed]";
    }
    plaintext_len += len;
    
    plaintext.resize(plaintext_len);
    EVP_CIPHER_CTX_free(ctx);
    
    return std::string(plaintext.begin(), plaintext.end());
}

int main() {
    std::string passphrase, plaintext;
    std::cout << "Enter passphrase: ";
    std::getline(std::cin, passphrase);
    std::cout << "Enter text to encrypt: ";
    std::getline(std::cin, plaintext);
    
    auto ciphertext = encrypt(plaintext, passphrase);
    std::cout << "Encrypted Data (Hex): ";
    for (unsigned char c : ciphertext) std::cout << std::hex << (int)c;
    std::cout << std::endl;
    
    std::string decrypted_text = decrypt(ciphertext, passphrase);
    std::cout << "Decrypted Text: " << decrypted_text << std::endl;
    
    return 0;
}
