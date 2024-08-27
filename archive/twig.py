from datetime import datetime
import hashlib
from archive.leaf import leaf

# is special leaf which aggregates other leafs an and added back link and proof of concepts
# 1. fundamental element of chain

class twig(leaf):

    def __init__(self, data) -> None:
        super().__init__(data)
        previous_proof,  previous_data = 1,2 # get from previous block
        self.data= {'proof': str(self.proof_of_work(previous_proof)),
        'link': self.gen_hash(previous_data), 
        'data': data}

    def gen_hash(self, data):
        return hashlib.sha256(str(data).encode("utf-8")).hexdigest()

    def proof_of_work(self, previous_proof):
        # Find a proof that satisfies the condition (e.g., hash starts with '00000')
        new_proof = 1
        while True:
            hash_operation = hashlib.sha256(
                str(new_proof**2 - int(previous_proof)**2).encode()
            ).hexdigest()
            if hash_operation[:5] == "00000":
                return new_proof
            new_proof += 1

    def gen_sign(self):
        return 0

    def get_dict(self):
        return self.__dict__
    

if __name__ == "__main__":
    t1 = twig("hi")
    print(t1.get_dict())