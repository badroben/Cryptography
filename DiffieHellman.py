from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import dh
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.primitives.serialization import Encoding, PublicFormat, load_pem_parameters, load_pem_public_key, load_pem_private_key 
from dhCheck import dhCheckCorrectness

def Diffie_Hellman():
    data = b'-----BEGIN DH PARAMETERS-----\nMEYCQQDP+dSNnBRy4jbHTvr0YcEk0bMzisMy+p/k9VYCb+gPNU/OSDkmEX62YKTc\nj1QrAo8+f3du/bjdfVKfv71LWtxjAgEC\n-----END DH PARAMETERS-----\n' 
    publicKey = b'-----BEGIN PUBLIC KEY-----\nMIGaMFMGCSqGSIb3DQEDATBGAkEAz/nUjZwUcuI2x0769GHBJNGzM4rDMvqf5PVW\nAm/oDzVPzkg5JhF+tmCk3I9UKwKPPn93bv243X1Sn7+9S1rcYwIBAgNDAAJAYyRw\n2K7KvbqudRx9DQtKH/tAQjDtDMIw7hFWYslMFnE/t44wArXQ/wuo0NPhFL4b63R8\nJZA7cF7tP+CAj3WHFA==\n-----END PUBLIC KEY-----\n'
    # deserialize parameters from PEM encoded data provided
    parameters = load_pem_parameters(data)
    # generate my private key
    myPrivateKey = parameters.generate_private_key()
    # calculate my public key
    myPublicKey = myPrivateKey.public_key()
    # deserialize a public key from the PEM encoded key provided 
    yourPublicKey = load_pem_public_key(publicKey)
    sharedKey = myPrivateKey.exchange(yourPublicKey)
    # perform key derivation 
    hkdf = HKDF(
        algorithm=hashes.SHA256(),
        length=32,
        salt=None, 
        info=b'handshake data',
    )
    key = hkdf.derive(sharedKey)
    # convert my public key to a PEM encoded format
    myPublicKey = myPublicKey.public_bytes(Encoding.PEM, PublicFormat.SubjectPublicKeyInfo)
    return myPublicKey, key