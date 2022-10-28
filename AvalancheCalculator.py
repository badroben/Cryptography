import hashlib

def avalancheCalculator(string1, string2): 
    # create the SHA-256 hash objects for both strings
    hash_object1 = hashlib.sha256(string1.encode())
    hash_object2 = hashlib.sha256(string2.encode())
    # calculate the hexadeciaml digest of the two hash objects
    hex_dig1 = hash_object1.hexdigest()
    hex_dig2 = hash_object2.hexdigest()
    # convert the hexadecimal digest into an int then to binary and remove the 0b at the start
    # and use zfill to fill up the strings so both would be of the same length
    bin_value1 = bin(int(hex_dig1, 16)).replace("0b", "" ).zfill(256)
    bin_value2 = bin(int(hex_dig2, 16)).replace("0b", "").zfill(256)
    avalancheNum = 0
    # at each iteration, check if the values of the strings do not match, and add one to avalancheNum
    for i in range(0, len(bin_value1)):
        if bin_value1[i] != bin_value2[i]:
            avalancheNum+=1 
    return avalancheNum