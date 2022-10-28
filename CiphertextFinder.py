from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os 

def findCiphertext():
    messageA = b"I'll give you 500 and that's my last offer."
    messageB = b"I'll give you 100 and that's my last offer."
    cipherTextA = b"\xef@\x92<$J\xb2\x8c\xbc\xabl'\x016\xd2{W-8\xcas\x83*\xa1\xef)\xc0\xda\x7fe\xab\xb1\x94\x7fJ\x98\xc8\xeei|'t\xb4"
    # Construct an AES-CTR Cipher object with the key and
    # randomly generated initialisation vector 
    key = os.urandom(32)
    iv = os.urandom(16)
    cipher1 = Cipher(algorithms.AES(key), modes.CTR(iv), backend=default_backend())
    cipher2 = Cipher(algorithms.AES(key), modes.CTR(iv), backend=default_backend())
    # encrypt both the messages 
    encryptor1 = cipher1.encryptor()
    encryptor2 = cipher2.encryptor()
    cipherText1 = encryptor1.update(messageA) + encryptor1.finalize()
    cipherText2 = encryptor2.update(messageB) + encryptor2.finalize()
    # convert each ciphered text into binary 
    cipherTextInBin1 = ''.join('{:08b}'.format(x) for x in bytearray(cipherText1))
    cipherTextInBin2 = ''.join('{:08b}'.format(x) for x in bytearray(cipherText2))
    # compare the binary values of both strings to find the element where they differ
    for i in range(0, len(cipherTextInBin1)):
        if cipherTextInBin1[i] != cipherTextInBin2[i]:
            break
    # convert the cipher provided to binary
    cipherA = ''.join('{:08b}'.format(x) for x in bytearray(cipherTextA))
    # cipher of message B will be the same as the message A except at the point where they differ
    # one will have 0 and the other will have 1 or vice versa.
    cipherB = list(cipherA)
    if cipherA[i] == "0":
        cipherB[i] = "1"
    else:
        cipherB[i] = "0"
    cipherB = "".join(cipherB)
    # convert from binary to bytes
    cipherB = bytes([int(cipherB[j:j+8], 2) for j in range(0, len(cipherB), 8)])
    return cipherB

# Main
if __name__ == "__main__":
    print(findCiphertext())