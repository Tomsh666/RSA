from Crypto.Util import Padding, asn1
from pyasn1.type import univ
from Crypto.Cipher import AES
import os
from pyasn1.codec.der import encoder


def add_asn1_header(n, e, encrypted_aes_key, iv, ciphertext):
    rsa_oid = univ.ObjectIdentifier('1.2.840.113549.1.1.1')
    rsa_encoded_oid = encoder.encode(rsa_oid)
    aes_oid = univ.ObjectIdentifier('2.16.840.1.101.3.4.1.42')
    aes_encoded_oid = encoder.encode(aes_oid)

    asn1_structure = asn1.DerSequence([
        asn1.DerSetOf({
            asn1.DerSequence([
                asn1.DerOctetString(rsa_encoded_oid),
                asn1.DerSequence([
                    asn1.DerInteger(n),
                    asn1.DerInteger(e),
                ]),
                asn1.DerSequence([]),
                asn1.DerSequence([
                    asn1.DerInteger(encrypted_aes_key)
                ]),
            ]),
        }),
        asn1.DerSequence([
            asn1.DerOctetString(aes_encoded_oid),
            asn1.DerInteger(len(ciphertext)),
        ])
    ])
    encrypted_data_with_header = asn1_structure.encode() + iv + ciphertext
    return encrypted_data_with_header


def encrypt(file, n, e, key):
    input_file = file
    output_file = "cipher_text.bin"
    with open(input_file, 'rb') as f:
        plain_text = f.read()

    # AES
    iv = os.urandom(AES.block_size)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    padded_text = Padding.pad(plain_text, AES.block_size)
    encrypted_text = cipher.encrypt(padded_text)

    aes_key = int.from_bytes(key, byteorder='big')
    encrypted_aes_key = pow(aes_key, e, n)
    encrypted_data_with_header = add_asn1_header(n, e, encrypted_aes_key, iv, encrypted_text)
    with open(output_file, 'wb') as f:
        f.write(encrypted_data_with_header)