import json
import os

from helper_funczex import (
    gen_hash, 
    )

class Chain():
    def __init__(self, db_name="block_chain.jason") -> None:
        if os.path.exists(db_name):
            with open(db_name, 'r') as fp:
                self.db = json.load(fp)
                self.id = len(self.db) - 1
        else:
            self.db = {}
            self.id= 1
            self.db.update({self.id: {"data": "Genesis Block", "meta": "PY_DICT", "link": "0x0"}})

    def gen_block (self, data, meta) -> None:
        prev_hash = gen_hash(list(self.db.keys())[-1])
        return {self.id + 1: {"data": data, "meta": meta, "link": prev_hash}}    

    def add_block (self, block) -> None:
        self.id = self.id + 1
        return self.db.update(block)

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
            if data in self.db[str(i+1)]["data"]:
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
    