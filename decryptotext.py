from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from Crypto.Random import get_random_bytes

key = b'`DE\x92\xda\xbbn\x05\xc8c\x9e\xc1\xbd\xe7\xf1\xab'
iv = b'\xddN\x81\xe8\xce\x0bNQ\x7f\x9f\xc2s\x99\x92s8'

def decrypt_aes(mode, ciphertext, key, iv=None):
    if mode == AES.MODE_ECB:
        cipher = AES.new(key, mode)
    else:
        cipher = AES.new(key, mode, iv)
    decrypted_text = unpad(cipher.decrypt(ciphertext), AES.block_size)
    return decrypted_text

with open('corrupted_ecb.bin', 'rb') as f:
    corrupted_ecb = f.read()

with open('corrupted_cbc.bin', 'rb') as f:
    corrupted_cbc = f.read()

with open('corrupted_cfb.bin', 'rb') as f:
    corrupted_cfb = f.read()

with open('corrupted_ofb.bin', 'rb') as f:
    corrupted_ofb = f.read()

try:
    decrypted_ecb = decrypt_aes(AES.MODE_ECB, corrupted_ecb, key)
except Exception as e:
    decrypted_ecb = str(e)

try:
    decrypted_cbc = decrypt_aes(AES.MODE_CBC, corrupted_cbc, key, iv)
except Exception as e:
    decrypted_cbc = str(e)

try:
    decrypted_cfb = decrypt_aes(AES.MODE_CFB, corrupted_cfb, key, iv)
except Exception as e:
    decrypted_cfb = str(e)

try:
    decrypted_ofb = decrypt_aes(AES.MODE_OFB, corrupted_ofb, key, iv)
except Exception as e:
    decrypted_ofb = str(e)

print("Decrypted ECB:", decrypted_ecb)
print("Decrypted CBC:", decrypted_cbc)
print("Decrypted CFB:", decrypted_cfb)
print("Decrypted OFB:", decrypted_ofb)

