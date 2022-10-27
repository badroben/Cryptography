# Include any required modules 
import string

def buildTables(rotationNumber):  
    # The function should return 2 dictionaries.   
    # The dictionaries should keep the mapping of plaintext characters   
    # to ciphertext ones and vice versa
    plainToCipher = {}
    for i, char in enumerate(string.ascii_lowercase):
        if i+1+rotationNumber > len(string.ascii_lowercase):
            i = i - len(string.ascii_lowercase)
        for j, l in enumerate(string.ascii_lowercase):
            if i + rotationNumber == j:
                plainToCipher[char] = l
        
    cipherToPlain = {char: l for l, char in plainToCipher.items()}
    return (plainToCipher, cipherToPlain) 

def encrypt(plainText, plainToCipher):  
    # The function should encrypt the plaintext using the   
    # plainToCipher dictionary built by the function buildTables   
    encryptedText = ""
    for char in plainText:
        if char not in string.ascii_lowercase:
            encryptedText = encryptedText+char
        else: 
            for key in plainToCipher:
                if char == key:
                    encryptedText = encryptedText+plainToCipher[key]
    return encryptedText

def decrypt(cipherText, cipherToPlain):  
    # The function should decrypt the cipherText using the   
    # cipherToPlain dictionary built by the function buildTables   
    decryptedText = ""
    for char in cipherText:
        if char not in string.ascii_lowercase:
            decryptedText = decryptedText+char
        else: 
            for key in cipherToPlain:
                if char == key:
                    decryptedText = decryptedText+cipherToPlain[key]
    return decryptedText

# Main
if __name__ == "__main__":
    # “”” 1. Create 2 dictionaries using the buildTables function using a rotation number, e.g. 10 
    # 2. Create a string with a plaintext, e.g. “hello world!” 
    # 3. Encrypt the plaintext and print the ciphertext 
    # 4. Decrypt the ciphertext and print the plaintext “””
    plainToCipher, cipherToPlain = buildTables(10)
    print(encrypt("hello world!", plainToCipher))
    print(decrypt("rovvy gybvn!", cipherToPlain))