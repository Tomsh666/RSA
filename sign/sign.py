from Crypto.Hash import SHA256


def sign(file, n, d):
    with open(file, 'rb') as f:
        message = f.read()
    output_file = "sign.bin"
    hash_obj = SHA256.new(message)
    digest = int.from_bytes(hash_obj.digest(), byteorder='big')
    signature = pow(digest, d, n)
    with open(output_file, "wb") as f:
        f.write(signature.to_bytes((signature.bit_length() + 7) // 8, byteorder='big'))