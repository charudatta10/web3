import json
from cryptography.hazmat.primitives import serialization
from block_v0 import block as b0
from block_v1 import block as b1
from block_v2 import block as b2


class GenesisBlock:
    def get_dict(self):
        return {"0": "Genesis Block"}


g0 = GenesisBlock()
block = b0("Test", g0, "private_key", "public_key")


class chain:
    def __init__(self) -> None:
        self.length = 0
        self.chain = {}

    def load_chain(self, file_name):
        with open(file_name, "r") as f:
            self.chain = json.load(f)
        self.length = len(self.chain)

    def ver_block(self):
        return False

    def ver_chain(self):
        return False

    def ver_link(self):
        for block_no in range(1, self.length):
            if (
                block._get_hash(json.dumps(self.chain[str(block_no - 1)]))
                == self.chain[str(block_no)]["link"]
            ):
                continue
            else:
                return False
        return True


c = chain()
c.load_chain("blocks_v0.json")
print(c.__dict__)
print(c.ver_link())
