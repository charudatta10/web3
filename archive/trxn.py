

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
        # 1. generate wallet
        # 2. generate wallet transaction
        # 3. verify wallet unique 
        # 4. add transaction to block
        # 5. add block to chain
        pass

    def txn_dao(self):
        pass

    def txn_nft(self):
        # 1. generate nft
        # 2. generate nft transaction
        # 3. verify nft unique 
        # 4. add transaction to block
        # 5. add block to chain
        # 6. NFT use:
        # 6.1. search if nft exist 
        # 6.2. if exist increase hit count of nft state
        # 6.3. create money transaction from hit count to owner of NFT
        # 6.4. execute transaction
        # 6.5. add transaction to block
        # 6.6. add block to chain
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