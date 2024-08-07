import json
import os
import redis
from datetime import datetime
import hashlib




class block():

    def __init__(self, data) -> None:
        self.stamp= None 
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

class Chain():
    def __init__(self, db_name="block_chain.jason") -> None:
        self.db = {}
        self.rdb = redis.Redis(host='localhost', port=6379, db=0)
        if os.path.exists(db_name):
            with open(db_name, 'r') as fp:
                self.db = json.load(fp)
                self.id = len(self.db) - 1
        else:
            self.db['0'] = block("Genesis Block").get_dict()
            self.id = 0
            self.rdb.set(str(self.id), json.dumps(self.db['0']))

    def get_block(self, id): 
        return self.db[str(id)]
    
    def get_block_rdb(self, id): 
        return self.rdb.get(str(id))

    def add_block(self, data) -> None: #mine block
        b1= block(data) 
        b1.stamp = datetime.now().timestamp()
        b1.proof = b1.proof_of_work(self.get_block(self.id)['proof'])
        b1.link = b1.gen_hash(self.get_block(self.id))
        b1.sign = b1.gen_sign()
        self.id = self.id + 1
        self.db[str(self.id)]= b1.get_dict()
        self.rdb.set(str(self.id), json.dumps(b1.get_dict()))

    def view_chain(self):
        for key,value in self.db.items():
            print(f"key: {key}\nvalue: {value}\n---------------")
    
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
    def search_blocks_by_data(self, target_data):
        matching_blocks = []
        for block in self.chain:
            if block.data == target_data:
                matching_blocks.append(block)
        return matching_blocks

    def is_data_in_chain(self, target_data):
        for i in range(0,len(self.db)):
            block = self.db[str(i)]
            if block["data"] == target_data:
                return True
        return False

    def is_data_unique(self):
        data_set = set()
        for i in range(0,len(self.db)):
            block = self.db[str(i)]
            if block["data"] in data_set:
                return False
            data_set.add(block["data"])
        return True

    def is_chain_valid(self):
        # Check if the entire chain is valid
        for i in range(1, len(self.db)):
            current_block = self.db[str(i)]
            previous_block = self.db[str(i - 1)]
            b1= block(previous_block["data"])
            if current_block["link"] != b1.gen_hash(previous_block):
                return False
        return True

if __name__ == "__main__":
    #b1=block( 0, '1a')
    #print(b1.__dict__)
    c1= Chain(db_name="../data/coin2.json")
    a={"src": "bank", "dest": "ram", "amt": "1000", "type": "cash"}
    #c1.add_block(a)
    #a={"src": "ram", "dest": "sham", "amt": "1000", "type": "cash"}
    #c1.add_block(a)
    #c1.view_chain()
    #c1.save_chain(db_name="../data/coin2.json")
    print(f"Is chain valid? {c1.is_chain_valid()}")
    print(f"list all cash transaction {c1.search_chain("cash")}")
    print(f"Is data unique {c1.is_data_unique()}")
    print(f"Is data in chain {c1.is_data_in_chain(a)}")
    
    