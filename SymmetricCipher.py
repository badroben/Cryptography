# Include any required modules
import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

def encrypt(key, plainText):
    # Generate an initialisation vector
    iv = os.urandom(16)
    # Construct an AES-CTR Cipher object with the given key and
    # randomly generated initialisation vector
    cipher = Cipher(algorithms.AES(key), modes.CTR(iv))
    encryptor = cipher.encryptor()
    cipherText = encryptor.update(plainText) + encryptor.finalize()
    return (cipherText, iv)

def decrypt(key, cipherText, iv):
    # Construct an AES-CTR Cipher object with the given key and
    # iv to decrypt
    cipher = Cipher(algorithms.AES(key), modes.CTR(iv))
    decryptor = cipher.decryptor()
    plainText = decryptor.update(cipherText) + decryptor.finalize()
    return (plainText)

# Main
if __name__ == "__main__":
    # 1. Create a key for AES and a plaintext
    key = os.urandom(32)
    plainText = b"I'll give you 500 and thta's my last offer."
    # 2. Encrypt the plaintext and print the result
    cipherText, iv = encrypt(key, plainText)
    print(cipherText)
    # 3. Decrypt the ciphertext and print the result
    print(decrypt(key, cipherText, iv))