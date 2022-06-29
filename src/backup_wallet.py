from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
import uuid

#private key generation
print("Generating Private key")
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
)

#public key generation
print("Generating Public key")
public_key = private_key.public_key()

#message
print("Generating message")
message = b"encrypted data"

#encrypt
print("Encrypting")
ciphertext = public_key.encrypt(
    message,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

#decrypt
print("Decrypting")
plaintext = private_key.decrypt(
    ciphertext,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

#verify encryption
print(f"verification {plaintext == message}")


#save keys
print("save keys")
from cryptography.hazmat.primitives import serialization

pem = private_key.private_bytes(
   encoding=serialization.Encoding.PEM,
   format=serialization.PrivateFormat.PKCS8,
   encryption_algorithm=serialization.BestAvailableEncryption(b'mypassword')
)
with open("key.pem","wb") as key_file:
    key_file.write(pem)

#load key
print("load keys")
with open("key.pem", "rb") as key_file:
    private_key1 = serialization.load_pem_private_key(
        key_file.read(),
        password=b'mypassword',
    )


#digital signature
print("sign digitally")
from cryptography.hazmat.primitives.asymmetric import utils
chosen_hash = hashes.SHA256()
hasher = hashes.Hash(chosen_hash)
hasher.update(b"data & ")
hasher.update(b"more data")
digest = hasher.finalize()
sig = private_key.sign(
    digest,
    padding.PSS(
        mgf=padding.MGF1(hashes.SHA256()),
        salt_length=padding.PSS.MAX_LENGTH
    ),
    utils.Prehashed(chosen_hash)
)

#verify digital signature
print("verify sign")
hasher = hashes.Hash(chosen_hash)
hasher.update(b"data & ")
hasher.update(b"more data")
digest = hasher.finalize()
public_key.verify(
    sig,
    digest,
    padding.PSS(
        mgf=padding.MGF1(hashes.SHA256()),
        salt_length=padding.PSS.MAX_LENGTH
    ),
    utils.Prehashed(chosen_hash)
)
