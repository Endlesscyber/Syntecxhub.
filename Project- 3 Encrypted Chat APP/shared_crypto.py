from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
import os
import base64

# 32-byte key (AES-256)
SECRET_KEY = b"12345678901234567890123456789012"

def encrypt(message: str):
    iv = os.urandom(16)

    cipher = Cipher(algorithms.AES(SECRET_KEY), modes.CBC(iv))
    encryptor = cipher.encryptor()

    padder = padding.PKCS7(128).padder()
    padded_data = padder.update(message.encode()) + padder.finalize()

    ct = encryptor.update(padded_data) + encryptor.finalize()

    return base64.b64encode(iv + ct).decode()

def decrypt(enc_message: str):
    raw = base64.b64decode(enc_message)

    iv = raw[:16]
    ct = raw[16:]

    cipher = Cipher(algorithms.AES(SECRET_KEY), modes.CBC(iv))
    decryptor = cipher.decryptor()

    padded = decryptor.update(ct) + decryptor.finalize()

    unpadder = padding.PKCS7(128).unpadder()
    data = unpadder.update(padded) + unpadder.finalize()

    return data.decode()