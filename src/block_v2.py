import json

from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend


class block:
    """
    Minimalist block implementation with just connecting link and data.
    """

    def __init__(self, data, prev_data) -> None:
        self.data = data
        self.link = self._get_hash(json.dumps(prev_data.get_dict()))

    def _get_hash(self, data: str) -> str:
        digest = hashes.Hash(hashes.SHA256(), backend=default_backend())
        digest.update(data.encode("utf-8"))  # Encode the string to bytes
        return digest.finalize().hex()

    def get_dict(self):
        return self.__dict__


if __name__ == "__main__":

    b = block("abc", "hi")
    print(b.get_dict())
