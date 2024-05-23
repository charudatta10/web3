import hashlib
import json

from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5

message = b'This message is from me, I promise.'

db=[]

def gen_wallet():
    key = RSA.generate(4096)
    with open('privkey1.pem', 'wb') as f:
        f.write(key.exportKey('PEM'))
    with open('pubkey1.pem', 'wb') as f:
        f.write(key.publickey().exportKey('PEM'))

def gen_hash(data):
    return hashlib.sha256(str(data).encode('utf-8')).hexdigest()

def gen_sign(message, key):
    hasher = SHA256.new(message)
    signer = PKCS1_v1_5.new(key)
    signature = signer.sign(hasher)
    return signature

def ver_sign(message, key, signature):
    hasher = SHA256.new(message)
    verifier = PKCS1_v1_5.new(key)
    if verifier.verify(hasher, signature):
        return True
    else:
        return False

def get_mnemo():
    pass

def get_phase():
    pass
 
def ver_wallet(data):
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
        prev_hash = gen_hash(db[-1])
        return db.append({"data": data, "meta": meta, "link": prev_hash})

    def view_block(self):
        for i in range(len(db)):
            for key,value in db[i].items():
                print(f"key: {key}\nvalue: {value}\n---------------")
            print("-------X-------")
    
    def save_chain(self):
        with open('block_chain.json', 'w') as fp:
            json.dump(db, fp, indent=4)

    def load_chain(self):
        with open('block_chain.json', 'r') as fp:
            db = json.load(fp)


class trxn():  
    
    def ver_trxn(self, meta,  dest, src, data):
        match meta:
            case "wallet_creation": 
                if(not ver_wallet(data)): # check if address exist search in data in block chain
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
    c1 = chain()
    c1.view_block()
    c1.block("block 1", "PY_DICT")
    c1.view_block()
    #gen_wallet()
    with open('pubkey1.pem', 'rb') as f:
        key = RSA.importKey(f.read())
        key1 = f.read()
    t1 = trxn()
    if t1.ver_trxn("wallet_creation", "", "",str(key.exportKey())):
        c1.block(str(key.exportKey()),"GEN_WALLET")
    c1.view_block()
    if t1.ver_trxn("wallet_creation", "", "",str(key.exportKey())):
        c1.block(str(key.exportKey()),"GEN_WALLET")
    c1.view_block()
    print(f"---Save Block chain ------")
    c1.save_chain()
    print(f"---Load Block chain ------")
    c1.load_chain()
    print(f"---Verify Block chain ------")
    c1.view_block()