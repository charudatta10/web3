

class Trxn():  
    def __init__(self, src, dst, sub, sgn, box) -> None:
        self.src = src # source
        self.dst = dst # destination
        self.sub = sub  # subject / type
        self.sgn = sgn # signature 
        self.box = box # content amount 

class VM():
    def __init__(self, db, tn: Trxn) -> None:
        self.db = db
        self.tn = tn

    def txn_wallet_gen(self):
        print(self.tn.box)
        pass

    def txn_dao(self):
        pass

    def txn_nft(self):
        pass

    def txn_coin(self):
        pass

    def txn_token(self):
        pass

    def txn_smart_ctr(self):
        pass

if __name__ == "__main__":
    t1 = Trxn(1,2,3,4,5)
    v1 = VM(1,t1)
    v1.txn_wallet_gen()