import json
from cryptography.hazmat.primitives import serialization
from block import block
# Load the private key from a file
with open("private_key.pem", "rb") as key_file:
    private_key = serialization.load_pem_private_key(
        key_file.read(),
        password=None,
    )   

# Load the public key from a file
with open("public_key.pem", "rb") as key_file:
    public_key = serialization.load_pem_public_key(
        key_file.read()
    )

class GenesisBlock():
    def get_dict(self):
        return {"0":"Genesis Block"}
    
g0 = GenesisBlock()

b0 = block("Ryunabi", g0, private_key, public_key)
print(b0.get_dict())
b1 = block("abc", b0, private_key, public_key)
print(b1.get_dict())
print(b0._get_hash(json.dumps(b0.get_dict()))==b1.link)
blocks = {}
blocks_data = {}
blocks['0'] = block("Ryunabi", g0, private_key, public_key)
blocks_data['0']= blocks['0'].get_dict()
for i in range(1,10):
    blocks[str(i)]= block(f"abc{i}", blocks[str(i-1)], private_key, public_key)
    blocks_data[str(i)] = blocks[str(i)].get_dict()
# Convert blocks to a list of dictionaries
#blocks_data = [{
#    "data": block.data,
#    "previous_hash": block.previous_hash,
#    "author": block.author
#} for block in blocks]

# Save to JSON file
with open("blocks.json", "w") as f:
    json.dump(blocks_data, f)


