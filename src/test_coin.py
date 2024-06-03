import json

from Crypto.PublicKey import RSA

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
from coin import chain, trxn, wallet, mine


def test_gen():
    c1 = chain()
    c1.view_chain()
    c1.block("block 1", "PY_DICT")
    c1.view_chain()
    gen_wallet()
    with open("pubkey1.pem", "rb") as f:
        key = RSA.importKey(f.read())
    t1 = trxn(c1.db)
    if t1.ver_trxn("wallet_creation", "", "", str(key.exportKey())):
        c1.block(str(key.exportKey()), "GEN_WALLET")
    c1.view_chain()
    if t1.ver_trxn("wallet_creation", "", "", str(key.exportKey())):
        c1.block(str(key.exportKey()), "GEN_WALLET")
    c1.view_chain()
    db_name = "block_chain.json"
    print(f"---Save Block chain ------")
    c1.save_chain(db_name)
    print(f"---Load Block chain ------")
    c1.load_chain(db_name)
    print(f"---Verify Block chain ------")
    c1.view_chain()


def test_load():
    c1 = chain()
    db_name = "block_chain.json"
    print(f"---Load Block chain ------")
    c1.load_chain(db_name)
    print(f"---Verify Block chain ------")
    #c1.view_chain()
    idx = c1.search_chain("block 1")
    #c1.block("block 1","PyBlock")
    for i in range(1000000):
        c1.block("abc","pytest")
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
    # test_gen()
    test_load()
    #test_cipher()
