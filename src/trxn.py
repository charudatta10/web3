

class Trxn():  
    def __init__(self, block) -> None:
        self.block = block

    def create_trxn(self):
        pass
    def get_trxn(self):
        pass
    def add_trxn(self):
        pass

    def ver_wallet(self):
        """list_val = [value for self.block["address"] in db.["data"]["address"]]# check if address exist search in data in block chain
                    print("wallet does not exist!")
                    return True
                else:
                    print("wallet already exist!")
                    return False"""

    def ver_money(self):
        pass
        """block = t_block[len(self.db) + 1]
        print(block)
        match block['meta']:
            case "wallet_creation": 
                if(not wallet().ver_wallet(self.db, block['data'])): # check if address exist search in data in block chain
                    print("wallet does not exist!")
                    return True
                else:
                    print("wallet already exist!")
                    return False
                # and verify sender with digital signature        
            case "money": 
                if wallet().ver_wallet(self.db, block['data']['src']):
                    if wallet().ver_wallet(self.db, block['data']['dest']):
                        amt = wallet().ver_wallet_amt(self.db, block['data'])
                        return True if amt-block['data']['amt'] > 0 else False
                
                
                #verify sender, verify sender has money, verify receiver, do transaction"""