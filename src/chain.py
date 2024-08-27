import json
from cryptography.hazmat.primitives import serialization
from block_v0 import block

class GenesisBlock():
    def get_dict(self):
        return {"0":"Genesis Block"}

class chain:
    def __init__(self) -> None:
        self.length = 0
        self.chain = {}

    def load_chain(self, file_name):
        with open(file_name, "r") as f:
            self.chain = json.load(f)
        self.length = len(self.chain)


    def ver_link(self, block_no):
        return self.chain[block_no - 1]._get_hash(json.dumps(b0.get_dict()))==self.chain[block_no].link
        

    


c = chain()
c.load_chain("blocks.json")
print(c.length)








