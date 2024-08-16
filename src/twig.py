import json
import os
import redis
from datetime import datetime
import hashlib
from leaf import leaf

# Everything is 
# 1. fundamental element of chain

class twig():

    def __init__(self, data) -> None:
        self.time= datetime.now().timestamp()
        self.proof= None
        self.link= None
        self.sign= None
        self.data= data

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
        return {"stamp": str(self.stamp),
                "proof": str(self.proof),
                "link": str(self.link),
                "sign": str(self.sign),
                "data": str(self.data)}