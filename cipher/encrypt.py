from Crypto.Util import Padding, asn1
from Crypto.Cipher import AES
import os

# TODO: remake asn1 header
def add_asn1_header(ciphertext, iv, encrypted_aes_key):
    asn1_header = asn1.DerSequence([iv, encrypted_aes_key])
    asn1_header_bytes = asn1_header.encode()
    encrypted_data_with_header = asn1_header_bytes + iv + ciphertext
    return encrypted_data_with_header


def encrypt(file, n, e, key):
    input_file = file
    output_file = "output.bin"
    with open(input_file, 'rb') as f:
        plain_text = f.read()

    # AES
    iv = os.urandom(16)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    padded_text = Padding.pad(plain_text, AES.block_size)
    encrypted_text = cipher.encrypt(padded_text)

    aes_key = int.from_bytes(key, byteorder='big')
    c = pow(aes_key, e, n)
    encrypted_aes_key = c.to_bytes((n.bit_length() + 7) // 8, byteorder='big')

    encrypted_data_with_header = add_asn1_header(encrypted_text, iv, encrypted_aes_key)
    with open(output_file, 'wb') as f:
        f.write(encrypted_data_with_header)
