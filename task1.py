# Include any required modules
import hashlib
import string
import itertools
def HexBinSHA256(stringToConvert):
    # The function should calculate wthe SHA256 value of stringToConvert
    # and convert the hex value to its binary representation
    # TODO
    hash_object = hashlib.sha256(stringToConvert)
    hex_dig = hash_object.hexdigest()

    return (hex_dig, bin(int(hex_dig, base=16)))
    
def SHA256Brute_forcer(hex_value):
    print("Brute-forcing started...")
    for character in itertools.product(string.ascii_lowercase, repeat=5):
        text = "".join(character)
        print(text)
        if hashlib.sha256(text.encode()).hexdigest() == hex_value:
            return text
    
# Main
if __name__ == "__main__":
    hex_value, binary_value = HexBinSHA256(b"hello world!")
    print("Hexadecimal: "+hex_value)
    print("Binary: "+binary_value.strip("0b"))
    hex_to_brute_force = "94f94c9c97bfa92bd267f70e2abd266b069428c282f30ad521d486a069918925"
    print("The string is: "+SHA256Brute_forcer(hex_to_brute_force))