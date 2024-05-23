import hashlib

db=[]

def get_hash(data):
    return hashlib.sha256(str(data).encode('utf-8')).hexdigest()

def get_sign():
    pass

def get_mnemo():
    pass

def get_phase():
    pass
 
def verify_add(data):
    for i in range(len(db)):
        if data in db[i]['data']:
            return True
        else:
            continue
    return False
    
class chain():
    def __init__(self) -> None:
        db.append({"data": "Genesis Block", "meta": "PY_DICT", "link": "0x0"})

    def block (self, data, meta) -> None:
        prev_hash = get_hash(db[-1])
        return db.append({"data": data, "meta": meta, "link": prev_hash})

    def view_block(self):
        for i in range(len(db)):
            print(db[i])

        

class trxn():
    def __init__(self, sender, receiver, data, meta) -> None:
        pass
    
    def create_txn(self, meta, dest, src, data):
        self.check_validity(meta, dest, src, data)
        return {"meta": meta, "to": dest, "from": src, "data": data}
    
    def check_validity(self, meta,  dest, src, data):
        match meta:
            case "wallet_creation": verify_add(data) # check if address exist search in data in block chain
                # and verify sender with digital signature
                
                
            case "money": """ verify sender, verify sender has money, verify reciter, do transection"""
class wallet():
    def __init__(self) -> None:
        pass

class mine():
    def __init__(self) -> None:
        pass


if __name__ == "__main__":
    c1 = chain()
    print(db)
    c1.view_block()
    print(db)
    c1.block("block 1", "PY_DICT")
    print(db)
    c1.view_block()
    print(db)
    c1.block("block 2", "PY_DICT")
    print(db)
    c1.view_block()
    print(db)
    
    print(db[0]['data'])
    print(verify_add('block 1'))