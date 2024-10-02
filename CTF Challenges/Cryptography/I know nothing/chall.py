from Crypto.Cipher import AES
from Crypto.Util.Padding import pad,unpad
import binascii

KEY = b"****************"
IV = b"****************"
pt = "The flag is:flag************. Key is a word in the vulnweb homepage and padded with null bytes."

cipher = AES.new(KEY,AES.MODE_CBC,IV)
ct = binascii.hexlify(cipher.encrypt(pad(pt.encode(),AES.block_size))).decode()
print("Cipher text:",ct)

# OUTPUT
# Cipher text: 2f6ad3e882c6b300d78675f62d689aa6664647b664b71ed1f6416660ee277e6a8783edd0efcb7a42fdaa5c868858390c6f772e9aff9d3acf1c7b82abf97b7a79d5515d133db79d96ba639066f45c9c735b58b55211e137c453ec1707a0b50efb

