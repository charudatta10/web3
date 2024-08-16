from datetime import datetime
from uuid import uuid4



# Everything is leaf
# 1. fundamental element of tree

class leaf():

    def __init__(self, data) -> None:
        self.id= str(uuid4())
        self.sign= str(self.get_sign())
        self.type= "Wallet_Gen"
        self.time= str(datetime.now().timestamp())
        self.data= data

    def get_sign(self):
        return 0

    def get_dict(self):
        return {"stamp": str(self.stamp),
                "proof": str(self.proof),
                "link": str(self.link),
                "sign": str(self.sign),
                "data": str(self.data)}