from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes
from rsa import PrivateKey, PublicKey 

def encryptMessage(plainText, publicKey):
    # create the cipher text from the public key
    cipherText = publicKey.encrypt(plainText, padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    ))
    print(cipherText)
    return cipherText

def decryptMessage(cipherText, privateKey):
# create the cipher text from the public key
    cipherText = privateKey.decrypt(cipherText, padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    ))
    return plainText

if __name__ == "__main__":
    # generate the pair of keys to use for encryption. 
    PrivateKey = rsa.generate_private_key(public_exponent=65537,key_size=1024)
    PublicKey = PrivateKey.public_key()
    plainText = input("Please enter the text to encrypt: ")
    plainText = bytes(plainText, 'utf-8')
    cipherText = encryptMessage(plainText, PublicKey)
    print(decryptMessage(cipherText, PrivateKey))