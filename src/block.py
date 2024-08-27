from datetime import datetime
from uuid import uuid4
import base64
import json

from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import padding


class block:

    def __init__(self, data, prev_data, private_key, public_key) -> None:
        self.id = str(uuid4())
        self.time = str(datetime.now().timestamp())
        self.data = data
        self.link = self._get_hash(json.dumps(prev_data.get_dict()))
        self.author = self._key_conversion(public_key)
        self.nonce = self.proof_of_work(1)
        self.sign = self.get_sign(self.id + self.nonce + self.time + self.data + self.link + self.author , private_key)

    def _get_hash(self, data: str)-> str:
        digest = hashes.Hash(hashes.SHA256(), backend=default_backend())
        digest.update(data.encode('utf-8'))  # Encode the string to bytes
        return digest.finalize().hex()
    
    def _key_conversion(self, public_key) -> str:
        public_key_bytes = public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )
        return base64.b64encode(public_key_bytes).decode('utf-8')

    def get_sign(self, message: str, private_key) -> str:
        signature = private_key.sign(
            message.encode('utf-8'),  # Encode the string to bytes
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()), 
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256(),
        )
        return signature.hex()  # Convert the signature to a hexadecimal string

    def proof_of_work(self, difficulty):
        # Find a proof that satisfies the condition (e.g., hash starts with '00000')
        new_proof = 1
        while True:
            hash_operation = self._get_hash(self.id + self.time + self.link + self.author + str(new_proof) )
            if hash_operation[:difficulty] == "0"*difficulty:
                return str(new_proof)
            new_proof += 1
            
    def get_dict(self):
        return self.__dict__


if __name__ == "__main__":
    # Load the private key from a file
    with open("private_key.pem", "rb") as key_file:
        private_key = serialization.load_pem_private_key(
            key_file.read(),
            password=None,
        )   

    # Load the public key from a file
    with open("public_key.pem", "rb") as key_file:
        public_key = serialization.load_pem_public_key(
            key_file.read()
        )

    b = block("abc", "hi", private_key, public_key)
    print(b.get_dict())