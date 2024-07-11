from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

plaintext = b"This is a sample text for encryption mode test. It should be at least 64 bytes long."

assert len(plaintext) >= 64

key = b'`DE\x92\xda\xbbn\x05\xc8c\x9e\xc1\xbd\xe7\xf1\xab'
iv = b'\xddN\x81\xe8\xce\x0bNQ\x7f\x9f\xc2s\x99\x92s8'

def encrypt_aes(mode, plaintext, key, iv=None):
    if mode == AES.MODE_ECB:
        cipher = AES.new(key, mode)
    else:
        cipher = AES.new(key, mode, iv)
    ciphertext = cipher.encrypt(pad(plaintext, AES.block_size))
    return ciphertext

ciphertext_ecb = encrypt_aes(AES.MODE_ECB, plaintext, key)
ciphertext_cbc = encrypt_aes(AES.MODE_CBC, plaintext, key, iv)
ciphertext_cfb = encrypt_aes(AES.MODE_CFB, plaintext, key, iv)
ciphertext_ofb = encrypt_aes(AES.MODE_OFB, plaintext, key, iv)

with open('ciphertext_ecb.bin', 'wb') as f:
    f.write(ciphertext_ecb)

with open('ciphertext_cbc.bin', 'wb') as f:
    f.write(ciphertext_cbc)

with open('ciphertext_cfb.bin', 'wb') as f:
    f.write(ciphertext_cfb)

with open('ciphertext_ofb.bin', 'wb') as f:
    f.write(ciphertext_ofb)


