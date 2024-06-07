from email.headerregistry import Address
import hashlib
import json 

from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from Crypto.Cipher import PKCS1_OAEP


def gen_wallet(user_name):
    key = RSA.generate(2046)
    with open(f"{user_name}_privkey.pem", "wb") as f:
        f.write(key.exportKey("PEM"))
    with open(f"{user_name}_pubkey.pem", "wb") as f:
        f.write(key.publickey().exportKey("PEM"))
    return str(key.publickey().exportKey("PEM"))


def gen_hash(data):
    return hashlib.sha256(str(data).encode("utf-8")).hexdigest()


def gen_sign(message, key):
    hasher = SHA256.new(message)
    signer = PKCS1_v1_5.new(key)
    signature = signer.sign(hasher)
    return signature


def gen_cipher(key, plaintext):
    cipher = PKCS1_OAEP.new(key)
    ciphertext = cipher.encrypt(plaintext.encode("utf-8"))
    return ciphertext


def gen_plain(key, plaintext):
    cipher = PKCS1_OAEP.new(key)
    plaintext = cipher.decrypt(plaintext)
    return plaintext.decode("utf-8")


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


def ver_wallet(db, data):
    for i in range(len(db)):
        if  db[i+1]["meta"] == "wallet_creation":
            if db[i+1]["data"]["address"] == data["address"]:
                return True
        else:
            continue
    return False

def ver_wallet_amt(db, data):
    for i in range(len(db)):
        amt = 0
        if  db[i+1]["meta"] == "money":
            if db[i+1]["data"]["src"] == data["src"]:
                amt += data["amt"]
            elif db[i+1]["data"]["dest"] == data["dest"]: 
                amt -= data["amt"]  
        else:
            continue
    return amt