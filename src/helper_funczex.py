from email.headerregistry import Address
import hashlib
import json 

from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from Crypto.Cipher import PKCS1_OAEP

from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import padding



def gen_hash(data):
    return hashlib.sha256(str(data).encode("utf-8")).hexdigest()


def gen_sign(message, key):
    hasher = SHA256.new(message)
    signer = PKCS1_v1_5.new(key)
    signature = signer.sign(hasher)
    return signature


def gen_cipher(key, plaintext):
    cipher = PKCS1_OAEP.new(key)
    ciphertext = cipher.encrypt(plaintext.encode("utf-8"))
    return ciphertext


def gen_plain(key, plaintext):
    cipher = PKCS1_OAEP.new(key)
    plaintext = cipher.decrypt(plaintext)
    return plaintext.decode("utf-8")


def ver_sign(message, key, signature):
    hasher = SHA256.new(message)
    verifier = PKCS1_v1_5.new(key)
    if verifier.verify(hasher, signature):
        return True
    else:
        return False


def get_mnemo():
    pass


def get_phase():
    pass


# Generate private key
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
)

# Generate public key
public_key = private_key.public_key()

# Save the private key to a file
with open("private_key.pem", "wb") as f:
    f.write(
        private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption(),
        )
    )

# Save the public key to a file
with open("public_key.pem", "wb") as f:
    f.write(
        public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo,
        )
    )


message = b"Hello, this is a secret message!"

# Sign the message
signature = private_key.sign(
    message,
    padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH),
    hashes.SHA256(),
)

# Save the signature to a file
with open("signature.bin", "wb") as f:
    f.write(signature)

# Load the public key
with open("public_key.pem", "rb") as f:
    public_key = serialization.load_pem_public_key(f.read())

# Verify the signature
try:
    public_key.verify(
        signature,
        message,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256(),
    )
    print("Signature is valid.")
except:
    print("Signature is invalid.")


digest = hashes.Hash(hashes.SHA256(), backend=default_backend())
digest.update(b"Hello World")
hex_dig = digest.finalize().hex()
print(hex_dig)

# Load the private key from a file
with open("private_key.pem", "rb") as key_file:
    loaded_private_key = serialization.load_pem_private_key(
        key_file.read(),
        password=None,
    )

# Load the public key from a file
with open("public_key.pem", "rb") as key_file:
    loaded_public_key = serialization.load_pem_public_key(
        key_file.read()
    )