import json
import os

from email.headerregistry import Address
import hashlib
import json 

from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from Crypto.Cipher import PKCS1_OAEP

from helper_funczex import (
    gen_hash, 
    gen_sign, 
    gen_cipher, 
    gen_plain, 
    ver_sign, 
    get_mnemo, 
    get_phase, 
    )


class Wallet():
    def __init__(self, user_name, mode="GEN") -> None:
        if mode == "LOAD":
            self.user_name = user_name
            with open(f"{self.user_name}_wallet.json", "rb") as f:
                tmp_wallet = json.load(f)
                self.address= tmp_wallet["address"]
                self.amt=tmp_wallet["amt"]
        else:
            self.user_name = user_name
            self.amt = 0
            self.address = self.gen_wallet()

    def gen_wallet(self):
        key = RSA.generate(2046)
        with open(f"{self.user_name}_privkey.pem", "wb") as f:
            f.write(key.exportKey("PEM"))
        with open(f"{self.user_name}_pubkey.pem", "wb") as f:
            f.write(key.publickey().exportKey("PEM"))
        return str(key.publickey().exportKey("PEM"))
    
    def ver_wallet(self):
        for i in range(len(db)):
            if  db[i+1]["meta"] == "wallet_creation":
                if db[i+1]["data"]["address"] == data["address"]:
                    return True
            else:
                continue
        return False
    
    def add_money(self, money):
        self.amt += money

    def get_balance(self):
        return self.amt
    
    def get_address(self):
        return self.address
    
    def get_user_name(self):
        return self.user_name
    
    def ver_amt(self):
        pass

    def get_wallet(self):
        return {"user": self.user_name,
                "amt": self.amt,
                "address": self.address}
        """
        b3 = c1.gen_block({"user": self.user_name,
                           "amt": self.amt,
                           "address": self.address}, 
                           "wallet_creation")
        if t1.ver_trxn(b3):
            c1.add_block(b3)
            print('wallet created')
        else:
            print("Could not create wallet as wallet already  exist")
        """
    def save_wallet(self):
        with open(f"{self.get_user_name()}_wallet.json",'w+') as fp:
            json.dump(self.gen_wallet(), fp, indent=4)
