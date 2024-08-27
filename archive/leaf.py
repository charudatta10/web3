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
        return 1 # check if signature is valid and authentic and registered and return signature

    def get_dict(self):
        return self.__dict__