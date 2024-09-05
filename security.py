from Crypto.Cipher import AES
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

def encrypt_data(data):
    # Encrypt data using AES-256
    key = b'Sixteen byte key'
    cipher = AES.new(key, AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(data.encode('utf-8'))
    return ciphertext

def decrypt_data(ciphertext):
    key = b'Sixteen byte key'
    cipher = AES.new(key, AES.MODE_EAX)
    data = cipher.decrypt(ciphertext)
    return data.decode('utf-8')

def rsa_encrypt_data(data, public_key):
    # Encrypt data using RSA-2048
    cipher_rsa = PKCS1_OAEP.new(RSA.import_key(public_key))
    encrypted = cipher_rsa.encrypt(data.encode('utf-8'))
    return encrypted
