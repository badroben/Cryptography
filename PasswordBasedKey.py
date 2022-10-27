# Include any required modules
import os
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt
salt = os.urandom(16)
def create(salt, password):
    kdf = Scrypt(salt, length=32, n=2**14, r=8, p=1)
    key = kdf.derive(password)
    return key

def verify(salt, password, key):
    kdf = Scrypt(salt, length=32, n=2**14, r=8, p=1)
    #"Success." if verification is successful
    # and "Invalid password” otherwise.
    try:
        kdf.verify(password, key)
        print("Success!!!")
    except: 
        print("Invalid Password!")

# Main code to check the functions
if __name__ == "__main__":
    # 1. You should use the create function on a password of your choice
    # and calculate it's key.
    password = b"hello world"
    key = create(salt, password)
    print(key)
    # 2. Ask a user to input a password.
    user_guess = input("Please input a password!: ")
    user_guess = bytes(user_guess, 'utf-8')
    # 3. Use the verify function to verify the given password against the
    # calculated key.
    verify(salt, user_guess, key)