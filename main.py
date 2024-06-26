import os

from cipher import encrypt, decrypt
from sign import sign, verify
from Crypto.Util.number import getPrime, GCD, inverse


def main():
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
    print("1. Encrypt")
    print("2. Decrypt")
    print("3. Sign file")
    print("4. Verify signature")
    while True:
        choice = input("Select option: ")
        if choice == "1":
            aes_key = os.urandom(32)
            encrypt("plain_text.txt", n, e, aes_key)
            print("Done")
        elif choice == "2":
            decrypt("cipher_text.bin", n, d)
            print("Done")
        elif choice == "3":
            sign("plain_text.txt", n, e, d)
            print("Done")
        elif choice == "4":
            verify("plain_text.txt", "sign.bin", n, e)
            print("Done")
        else:
            print("Wrong choice")



if __name__ == "__main__":
    main()
