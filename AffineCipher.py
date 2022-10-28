import string 

def encryptAffine(plainText, a, b):
    # define a dictionary that stores the upper case characters with their corresponding numbers.
    charToNum = {}
    cipherText = ""
    for i, char in enumerate(string.ascii_uppercase):
        charToNum[char] = i
    # define a dictionary to allow mapping from a number to a character. 
    numToChar = {num:char for char, num in charToNum.items()}
    # for each character in the plain text apply the affine algorithm on it
    for char in plainText:
        # if the character is not uppercase then leave it the same
        if char not in string.ascii_uppercase:
            cipherText = cipherText+char
        else: 
            # x is the number corresponding to the current character in the string 
            x = charToNum[char]
            # perform the function to encrypt the characters
            result = (a * x + b) % 26
            # retrieve the corresponding char to the result
            cipheredChar = numToChar[result]
            # concatenate the char to the string
            cipherText = cipherText + cipheredChar
    return cipherText