from Crypto.Hash import SHA256
from Crypto.Util import asn1
from pyasn1.type import univ
from pyasn1.codec.der import encoder


def add_asn1(n, e, signature):
    rsa_sha256_oid = univ.ObjectIdentifier('1.2.840.113549.1.1.11')
    rsa_sha256_encoded_oid = encoder.encode(rsa_sha256_oid)

    asn1_structure = asn1.DerSequence([
        asn1.DerSetOf({
            asn1.DerSequence([
                asn1.DerOctetString(rsa_sha256_encoded_oid),
                asn1.DerSequence([
                    asn1.DerInteger(n),
                    asn1.DerInteger(e),
                ]),
                asn1.DerSequence([]),
                asn1.DerSequence([
                    asn1.DerInteger(signature)
                ]),
            ]),
        }),
        asn1.DerSequence([])
    ])
    encrypted_data = asn1_structure.encode()
    return encrypted_data


def sign(file, n, e, d):
    with open(file, 'rb') as f:
        message = f.read()
    output_file = "sign.bin"
    hash_obj = SHA256.new(message)
    digest = int.from_bytes(hash_obj.digest(), byteorder='big')
    signature = pow(digest, d, n)
    data = add_asn1(n, e, signature)
    with open(output_file, "wb") as f:
        f.write(data)