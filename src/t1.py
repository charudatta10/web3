import json
from block_v0 import block as b0
from block_v1 import block as b1
from block_v2 import block as b2

class GenesisBlock():
    def get_dict(self):
        return {"0":"Genesis Block"}
    
g0 = GenesisBlock()

# Test code block v0
t0 = b0("Ryunabi", g0, "private_key", "public_key")
t1 = b1("abc", t0)
t2 = b2("Ryunabi1", t1)
t3 = b0("abc1", t2, "private_key", "public_key")
t4 = b1("abc2", t3)
t5 = b2("Ryunabi2", t4)

blocks_data ={"0": t0.get_dict(),"1": t1.get_dict(),"2": t2.get_dict(),"3": t3.get_dict(),"4": t4.get_dict(),"5": t5.get_dict()}
print(blocks_data)
# Save to JSON file
with open("mixed_blocks.json", "w") as f:
    json.dump(blocks_data, f)






