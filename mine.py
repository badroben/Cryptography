import hashlib

def mine(hash_value, difficulty):
    assert difficulty >= 1
    prefix = "0" * difficulty
    hash = bytes(hash_value, 'ascii')
    for nonce_value in range(100000):
        block_hash = hashlib.sha256(hash + bytes(nonce_value)).hexdigest()
        print(nonce_value)
        if block_hash.startswith(prefix):
            print("New block found!")
            return block_hash, nonce_value
    return "nothing", 100000
# Main code to check the functions
if __name__ == "__main__":
    print("Running: ")
    hash = "000000b9015ce2a08b61216ba5a0778545bf4ddd7ceb7bbd85dd8062b29a9140bf"
    block_hash, nonce = mine(hash, 4)
    print("After {} iterations found nonce: {}".format(nonce, block_hash))