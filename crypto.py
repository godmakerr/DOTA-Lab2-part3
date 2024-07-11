from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes
import os

with open('pic_original.bmp', 'rb') as f:
    original_data = f.read()

key = get_random_bytes(16)
iv = get_random_bytes(16)

cipher_ecb = AES.new(key, AES.MODE_ECB)
encrypted_ecb = cipher_ecb.encrypt(pad(original_data, AES.block_size))

cipher_cbc = AES.new(key, AES.MODE_CBC, iv)
encrypted_cbc = cipher_cbc.encrypt(pad(original_data, AES.block_size))

with open('encrypted_ecb.bmp', 'wb') as f:
    f.write(encrypted_ecb)

with open('encrypted_cbc.bmp', 'wb') as f:
    f.write(encrypted_cbc)

