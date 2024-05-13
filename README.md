RSA Encryption and Signature Program

This program implements RSA encryption and decryption, as well as electronic signature generation and verification using the RSA algorithm. The program uses the AES-256 symmetric algorithm in CBC mode for file encryption, and the SHA256 hash algorithm for electronic signature generation.

Functionality
a) Encryption and Decryption:
The program performs file encryption and decryption using the RSA algorithm. In encryption mode, the program accepts a message file (of any format), an RSA public key, and a symmetric algorithm key; it returns an encrypted file with a header that conforms to the ASN.1 notation described in Appendix A. The file encryption is performed using the AES-256 symmetric algorithm in CBC mode. The AES encryption key (32 bytes) must be represented as a number for RSA encryption, with the byte order being MSB. Any unused leading digits (bytes) of the number should be considered zero. In decryption mode, the program accepts an encrypted file and an RSA private key; it returns the decrypted message.

b) Electronic Signature Generation and Verification:
The program also performs electronic signature generation and verification using the RSA algorithm. The SHA256 hash algorithm is recommended for electronic signature implementation. Since the hash value computed by SHA-256 may be longer than the RSA modulus, the program should compare the value of h(m) (mod n) with the signature s of the message m during signature verification. In signature generation mode, the program accepts a file to be signed and an RSA signing key; it returns a separate signature file. In signature verification mode, the program accepts a message and a signature file; it returns the result "Signature accepted" or "Signature is invalid".
