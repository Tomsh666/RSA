from Crypto.Util import asn1
from Crypto.Cipher import AES

def decrypt(cipher_file, n, d):
    with open(cipher_file, 'rb') as file:
        asn_len = file.read(4)
        asn_len = int.from_bytes(asn_len[2:], byteorder='big')
    with open(cipher_file, 'rb') as file:
        asn_content = file.read(4 + asn_len)
        iv = file.read(AES.block_size)
        ciphertext = file.read()

    asn_seq1 = asn1.DerSequence()
    asn_seq1.decode(asn_content)
    asn_set = asn1.DerSetOf()
    asn_set.decode(asn_seq1[0])
    asn_seq2 = asn1.DerSequence()
    asn_seq2.decode(asn_set[0])
    encrypted_aes_key = asn1.DerSequence()
    encrypted_aes_key.decode(asn_seq2[3])

    aes_key = pow(encrypted_aes_key[0], d, n)
    aes_key_bytes = aes_key.to_bytes(32, byteorder='big')
    cipher = AES.new(aes_key_bytes, AES.MODE_CBC, iv)
    plaintext = cipher.decrypt(ciphertext)
    plaintext = plaintext[:-plaintext[-1]]
    with open('decrypted_file.bin', 'wb') as f:
        f.write(plaintext)
