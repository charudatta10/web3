import random
import logging

logging.basicConfig(level=logging.ERROR)

from Crypto.PublicKey import RSA

from helper_funczex import (
    gen_cipher,
    gen_plain,
)
from coin import Mine
from trxn import Trxn
from chain import Chain
from wallet import Wallet




def test_chain():
    c1 = Chain() # create chain
    for i in range(10):
        c1.add_block(f"block {i} TEST") # create first block
    db_name = "coin1.json" # save block chain
    c1.save_chain(db_name)
    c2 = Chain("coin1.json")
    print(c2.search_chain("block 3 TEST"))
    c2.view_chain()

def test_wallet():
    w0 = Wallet("user1") # create wallet
    w0.add_money(100)
    w1 = Wallet("user2")
    w0.get_wallet() # add wallet
    w0.save_wallet()
   
def test_coin():
    pass

def test_trxn():
    t1 = Trxn() # create transaction
    temp_txn={"src":'gov', "dest":'bank', "amt":1000}
    bt = c1.gen_block(str(temp_txn),"money")
    c1.add_block(bt)

    t1 = trxn(c1.db)
    for i in range(10):
        my_user_list = [c1.db['2']['data'], c1.db['3']['data'], c1.db['4']['data'],c1.db['5']['data']]
        get_sender = random.choice(my_user_list)
        get_receiver = random.choice(my_user_list)
        get_money = random.randint(1, 100)
        temp_txn={"src":get_sender, "dest":get_receiver, "amt":get_money}
        bt = c1.gen_block(temp_txn,"money")
        if t1.ver_trxn(bt):
            c1.add_block(bt)
        else:
            print("Transaction failed")
    c1.save_chain(db_name)
    t1 = c1.get_block(idx)
    for i in range(len(idx)):
        print(f"Block number: {idx[i]}\nBlocK: {t1[i]}\n-----------------")


def test_cipher():
    with open("pubkey1.pem", "rb") as f:
        pubkey = RSA.importKey(f.read())
    with open("privkey1.pem", "rb") as f:
        privkey = RSA.importKey(f.read())
    plain_text = "hi there"
    cipher_text = gen_cipher(pubkey, plain_text)
    print(cipher_text)
    print(gen_plain(privkey, cipher_text))


if __name__ == "__main__":
    test_chain()
    #test_wallet()
    #test_trxn()
    #test_coin()
    #test_cipher()
