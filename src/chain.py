from block import block, genesys_block 

class chain:
    
    def __init__(self):
        self.chain=[]
        self.chain.append(genesys_block())
        self.id = 0


    def add_block(self, trxn):
        self.id = self.id + 1
        self.chain.append(block(trxn = trxn, prev_block = self.chain[self.id - 1]))

    def __str__(self):
        txt = f"ID : Gensys\n"
        for i in range(1,len(self.chain)):
            txt += f"\nID : {self.chain[i].meta.uuid}\nHash : {self.chain[i].meta.hash}\nLink : {self.chain[i].meta.link}\n"
        return txt

if __name__ == "__main__":
    c1 = chain()
    c1.add_block("GAN1")
    c1.add_block("GAN2")
    print(c1)

