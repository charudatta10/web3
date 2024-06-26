import json
import os
from datetime import datetime
from helper_funczex import (
    gen_hash, 
    )

def gen_sign():
    pass


class block():

    def __init__(self, proof, data) -> None:
        self.stamp= datetime.now().timestamp()
        self.proof= proof
        self.link= None
        self.sign= gen_sign()
        self.data= data

    

class Chain():
    def __init__(self, db_name="block_chain.jason") -> None:
        self.db = {}
        if os.path.exists(db_name):
            with open(db_name, 'r') as fp:
                self.db = json.load(fp)
                self.id = len(self.db) - 1
        else:
            self.db['0'] = block(0, "Genesis Block").__dict__
            self.id = 0

    def get_block(self, id): # return previous block
        return self.db[str(id)]

    def add_block(self, data) -> None:
        b1= block(0, data) 
        b1.link = gen_hash(self.get_block(self.id))
        self.id = self.id + 1
        self.db[str(self.id)]= b1.__dict__

    def view_chain(self):
        for i in range(len(self.db)):
            for key,value in self.db.items():
                print(f"key: {key}\nvalue: {value}\n---------------")
            print(f"-------{i}-------")
    
    def save_chain(self, db_name):
        with open(db_name, 'w') as fp:
            json.dump(self.db, fp, indent=4)


    def search_chain(self, data):
        block_num = []
        for i in range(len(self.db)):
            if data in self.db[str(i)]["data"]:
                block_num.append(i)
            else:
                continue
        return False if block_num == [] else block_num 
       
        """
        1. search for block
        2. search for data in block
        3. search number of instances of data
        4. perform search operation
        5. query generator or query language 
        6. operation on queried data
        """

if __name__ == "__main__":
    #b1=block( 0, '1a')
    #print(b1.__dict__)
    c1= Chain(db_name="coin2.json")
    c1.view_chain()
    c1.add_block("abc")
    c1.view_chain()
    c1.add_block("123")
    c1.view_chain()
    c1.save_chain(db_name="coin2.json")
    