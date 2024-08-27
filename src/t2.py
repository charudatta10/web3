import json
from block_v0 import block as b0
from block_v1 import block as b1
from block_v2 import block as b2

class GenesisBlock():
    def get_dict(self):
        return {"0":"Genesis Block"}
    
g0 = GenesisBlock()

# Test code block v0
blocks = {}
blocks_data = {}
blocks['0'] = b0("Ryunabi", g0, "private_key", "public_key")
blocks_data['0']= blocks['0'].get_dict()
for i in range(1,10):
    blocks[str(i)]= b0(f"abc{i}", blocks[str(i-1)], "private_key", "public_key")
    blocks_data[str(i)] = blocks[str(i)].get_dict()
    #print(blocks['0']._get_hash(json.dumps(blocks[str(i-1)].get_dict()))==blocks[str(i)].link)
    print(blocks['0']._get_hash(json.dumps(blocks_data[str(i-1)]))==blocks_data[str(i)]['link'])

# Save to JSON file
with open("blocks_v0.json", "w") as f:
    json.dump(blocks_data, f)