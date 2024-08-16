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
        self.sign= self.get_sign()
        self.type= "Wallet_Gen"
        self.time= datetime.now().timestamp()
        self.data= data

    def gen_sign(self):
        return 0

    def get_dict(self):
        return {"stamp": str(self.stamp),
                "proof": str(self.proof),
                "link": str(self.link),
                "sign": str(self.sign),
                "data": str(self.data)}