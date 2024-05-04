from Crypto.Util.number import getPrime, GCD, inverse
from Crypto.Util import Padding
from Crypto.Cipher import AES
import os
from dotenv import load_dotenv


def encrypt():
    load_dotenv()
    input_file = os.getenv('INPUT_FILE')
    output_file = os.getenv('OUTPUT_FILE')
    with open(input_file, 'r') as f:
        plain_text = f.read()
    p = getPrime(1024)
    q = getPrime(1024)
    n = p * q
    phi = (p - 1) * (q - 1)

    e = 2
    while e < phi:
        if GCD(e, phi) == 1:
            break
        else:
            e += 1
    d = inverse(e, phi)

    # AES
    key = os.urandom(32)
    iv = os.urandom(16)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    padded_text = Padding.pad(plain_text.encode('utf-8'), AES.block_size)
    encrypted_text = cipher.encrypt(padded_text)
    with open(output_file, 'wb') as f:
        f.write(iv + encrypted_text)

    aes_key = int.from_bytes(key, byteorder='big')
    c = pow(aes_key, e, n)
    encrypted_aes_key = c.to_bytes((n.bit_length() + 7) // 8, byteorder='big')
    print(encrypted_aes_key)
