from Crypto.Hash import SHA256


def verify(file, sign_file, n, e):
    with open(file, "rb") as file:
        message = file.read()
    with open(sign_file, "rb") as file:
        signature = file.read()
    hash_obj = SHA256.new(message)
    digest = int.from_bytes(hash_obj.digest(), byteorder='big')
    signature_int = int.from_bytes(signature, byteorder='big')
    if pow(signature_int, e, n) == digest:
        print("Correct signature")
    else:
        print("Incorrect signature")
