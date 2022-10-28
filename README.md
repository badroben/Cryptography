# Cryptography
A few programs that cover a few aspects about [Cryptography](https://en.wikipedia.org/wiki/Cryptography)

# CalculateSHA256.py
This program calculates the [SHA256](https://www.n-able.com/blog/sha-256-encryption) value of a given string and converts the hex value to its binary representation. It also contains a brute-forcer function to break the SHA256 hexdigest.

# PasswordBasedKey.py
This program creates a key on a given password, it asks the user to input a password and it verifies it against the calculated key. 

# SymmetricCipher.py
Created a [symmetric](https://en.wikipedia.org/wiki/Symmetric-key_algorithm) cipher using the [AES](https://en.wikipedia.org/wiki/Advanced_Encryption_Standard) algorithm. The code encrypts(convert plaintext to ciphertext) and decrypts (convert ciphertext to plaintext)

# mine.py
This program is a cryptocurrency miner, given the [SHA256](https://www.n-able.com/blog/sha-256-encryption) hash that contains all the information of a block except for the [nonce](https://en.wikipedia.org/wiki/Cryptographic_nonce) value. 

# Asymmetric.py
The code uses [RSA](https://en.wikipedia.org/wiki/RSA_(cryptosystem)) algorithm to encrypt a user-provided message and decrypts it using the private key generated.

# Signature.py
The code uses Mario's public key and sent [signature](https://cloud.google.com/kms/docs/digital-signatures) to check if the message has been sent by Mario or not.

# main.py
The program encrypts a message/plaintext using a mapped dictionary to create a ciphertext and it decrypts the ciphertext and prints the plaintext. 

# AffineCipher.py
This code implements the encryption function of an [Affine Cipher](https://en.wikipedia.org/wiki/Affine_cipher).

# AvalancheCalculator.py
Hash functions are one-way functions. We know that a single change in the input of a string may create a large change in its hash value. 
This is known also as the [avalanche property](https://en.wikipedia.org/wiki/Avalanche_effect). 
The program calculates and returns the avalanche number between two strings. 

# CiphertextFinder.py
Given a few variables (messageA and its ciphertext using AES-CTR)
Consider the following scenario:
I am a hacker! messageA and its ciphertext are both known to me. I also know that the same key and IV are used in all subsequent messages. 
messageB = b"I'll give you 100 and that's my last offer." is such a subsequent message. 
The program calculates the ciphertext of messageB.

# DiffieHellman.py
The [Diffie Hellman key exchange](https://en.wikipedia.org/wiki/Diffie%E2%80%93Hellman_key_exchange) protocol is an [asymmetric](https://cryptography.io/en/latest/hazmat/primitives/asymmetric/dh/) scheme. The purpose of the algorithm is to enable two users to securely exchange a key that can then be used for subsequent symmetric encryption of messages.
Given the Diffie-Hellman parameters and a public key, the function returns my public key and the calculated derived key in bytes. 
