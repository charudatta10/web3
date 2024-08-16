import json
import os
import redis
from datetime import datetime
from uuid import uuid4



# Everything is leaf
# 1. fundamental element 

class leaf():

    def __init__(self, data) -> None:
        self.id= uuid4()
        self.sign= None
        self.type= None
        self.time= datetime.now().timestamp()
        self.data= data

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