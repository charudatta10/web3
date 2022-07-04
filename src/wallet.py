from cryptography.hazmat.primitives.asymmetric import rsa
import uuid


class wallet:
    def __init__(self):
        self.private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048,
        )
        self.public_key = self.private_key.public_key()
        self.address = uuid.uuid1()
        self.seed = "place holder"

    def save_keys(self):
        pass


if __name__ == "__main__":
    w = wallet()
    print(
        f"Private Key : {w.private_key}\nPublic Key : {w.public_key}\nAddress : {w.address}\nSeed : {w.seed}"
    )
