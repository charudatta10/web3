import json
import os

from helper_funczex import (
    gen_wallet, 
    gen_hash, 
    gen_sign, 
    gen_cipher, 
    gen_plain, 
    ver_sign, 
    get_mnemo, 
    get_phase, 
    ver_wallet,
    )


class chain():
    def __init__(self, db_name="block_chain.jason") -> None:
        if os.path.exists(db_name):
            with open(db_name, 'r') as fp:
                self.db = json.load(fp)
                self.id = len(self.db) - 1
        else:
            self.db = {}
            self.id=0
            self.db.update({self.id: {"data": "Genesis Block", "meta": "PY_DICT", "link": "0x0"}})

        

    def block (self, data, meta) -> None:
        prev_hash = gen_hash(list(self.db.keys())[-1])
        self.id = self.id + 1
        return self.db.update({self.id: {"data": data, "meta": meta, "link": prev_hash}})

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
    
    def get_block(self, idx):
        return [self.db[str(i)]  for i in idx]
    
    def crud_create():
        """
        1. validate data source, transaction
        2. add entry
        3. validate authenticate, authorize chain
        """
    def crud_read():
        """
        1. search for block
        2. search for data in block
        3. search number of instances of data
        4. perform search operation
        5. query generator or query language 
        6. operation on queried data
        """
    def crud_update():
        """
        not allowed
        """
    def crud_delete():
        """
        not allowed
        """




class trxn():  
    def __init__(self, db) -> None:
        self.db = db
    
    def ver_trxn(self, meta,  dest, src, data):
        match meta:
            case "wallet_creation": 
                if(not ver_wallet(self.db, data)): # check if address exist search in data in block chain
                    print("wallet needs to be created")
                    return True
                else:
                    print("wallet already exist")
                    return False
                # and verify sender with digital signature        
            case "money": """ verify sender, verify sender has money, verify reciter, do transection"""


class wallet():
    def __init__(self) -> None:
        pass


class mine():
    def __init__(self) -> None:
        pass







if __name__ == "__main__":
    print("coin")
