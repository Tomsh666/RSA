from Crypto.Hash import SHA256
from Crypto.Util import asn1

def verify(file, sign_file, n, e):
    with open(file, "rb") as file:
        message = file.read()
    with open(sign_file, "rb") as file:
        data = file.read()

    asn_seq1 = asn1.DerSequence()
    asn_seq1.decode(data)
    asn_set = asn1.DerSetOf()
    asn_set.decode(asn_seq1[0])
    asn_seq2 = asn1.DerSequence()
    asn_seq2.decode(asn_set[0])
    rsa_key = asn1.DerSequence()
    rsa_key.decode(asn_seq2[1])
    signature = asn1.DerSequence()
    signature.decode(asn_seq2[3])


    hash_obj = SHA256.new(message)
    digest = int.from_bytes(hash_obj.digest(), byteorder='big')
    if pow(signature[0], rsa_key[1], rsa_key[0]) == digest:
        print("Correct signature")
    else:
        print("Incorrect signature")
