import argparse
from Crypto import Cipher
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
from base64 import b64decode, b64encode

def general_random_key():
    key = get_random_bytes(16)
    key = b64encode(key).decode('utf8')
    return key

def aes_cbc_encrypt(key, message):
    key = b64decode(key)
    message = bytes(message, 'utf8')
    cipher = AES.new(key, AES.MODE_CBC)
    cipher_bytes = cipher.encrypt(pad(message, AES.block_size))
    iv = b64encode(cipher.iv).decode('utf8') 
    ct = b64encode(cipher_bytes).decode('utf8')
    return iv, ct

def aes_cbc_decrypt(key, iv, cipher_text):
    key = b64decode(key)
    iv = b64decode(iv)
    ct = b64decode(cipher_text)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    pt = unpad(cipher.decrypt(ct), AES.block_size)
    return pt

def aes_ctr_encrypt(key, message):
    key = b64decode(key)
    message = bytes(message, 'utf8')
    cipher = AES.new(key, AES.MODE_CTR)
    ct_bytes = cipher.encrypt(message)
    nonce = b64encode(cipher.nonce).decode('utf8')
    ct = b64encode(ct_bytes).decode('utf8')
    return nonce, ct

def aes_ctr_decrypt(key, nonce, cipher_text):
    key = b64decode(key)
    nonce = b64decode(nonce)
    ct = b64decode(cipher_text)
    cipher = AES.new(key, AES.MODE_CTR, nonce= nonce)
    pt = cipher.decrypt(ct)
    return pt

def main():
    parser = argparse.ArgumentParser(description= 'AES with CBC mode and CTR mode.')
    parser.add_argument('-m', '--mode', type=str, choices=['cbc', 'ctr', 'key'],
            help='Choices mode for AES function.')
    parser.add_argument('-s', '--selection', type=str, choices=['e', 'd'],
    help='Encrypt or Decrypt.')
    parser.add_argument('-k', '--key', dest='key', action='store', help='Key of AES function.')
    parser.add_argument('-iv', '--iv', dest='iv', action='store', help='Iv uses in CBC mode.')
    parser.add_argument('-n', '--nonce', dest='nonce', action='store', help='Nonce uses in CTR mode.')
    parser.add_argument('-t', '--text', dest='message', action='store', help='Plain text or Cipher text')
    AES = parser.parse_args()

    if AES.mode == 'key':
        key = general_random_key()
        print(f"Key general random: {key}")
    if AES.mode == 'cbc':
        print("CBC mode >>")
        if AES.selection == 'e':
            print("Encrypt...\n")
            iv , cipher_text = aes_cbc_encrypt(AES.key, AES.message)
            print(f"Iv: {iv}")
            print(f"Cipher text: {cipher_text}\n")
        if AES.selection == 'd':
            print("Decrypt...\n")
            plain_text = aes_cbc_decrypt(AES.key, AES.iv, AES.message)
            plain_text = str(plain_text, 'utf8')
            print(f"Plain text: {plain_text}\n")
    if AES.mode == 'ctr':
        print("CTR mode >>")
        if AES.selection == 'e':
            print("Encrypt...\n")
            nonce , cipher_text = aes_ctr_encrypt(AES.key, AES.message)
            print(f"Nonce: {nonce}")
            print(f"Cipher text: {cipher_text}\n")
        if AES.selection == 'd':
            print("Decrypt...\n")
            plain_text = aes_ctr_decrypt(AES.key, AES.nonce, AES.message)
            plain_text = str(plain_text, 'utf8')
            print(f"Plain text: {plain_text}\n")

if __name__ == "__main__":
    main()