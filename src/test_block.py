import json
from block_v0 import block as b0
from block_v1 import block as b1
from block_v2 import block as b2


class GenesisBlock:
    def get_dict(self):
        return {"0": "Genesis Block"}


g0 = GenesisBlock()

# Test code block v0
t0 = b0("Ryunabi", g0, "private_key", "public_key")
print(t0.get_dict())
t1 = b0("abc", t0, "private_key", "public_key")
print(t1.get_dict())
print(t0._get_hash(json.dumps(t0.get_dict())) == t1.link)
blocks = {}
blocks_data = {}
blocks["0"] = b0("Ryunabi", g0, "private_key", "public_key")
blocks_data["0"] = blocks["0"].get_dict()
for i in range(1, 10):
    blocks[str(i)] = b0(f"abc{i}", blocks[str(i - 1)], "private_key", "public_key")
    blocks_data[str(i)] = blocks[str(i)].get_dict()

# Save to JSON file
with open("blocks_v0.json", "w") as f:
    json.dump(blocks_data, f)

# Test code block v1
t0 = b1("Ryunabi", g0)
print(t0.get_dict())
t1 = b1("abc", t0)
print(t1.get_dict())
print(t0._get_hash(json.dumps(t0.get_dict())) == t1.link)
blocks = {}
blocks_data = {}
blocks["0"] = b1("Ryunabi", g0)
blocks_data["0"] = blocks["0"].get_dict()
for i in range(1, 10):
    blocks[str(i)] = b1(f"abc{i}", blocks[str(i - 1)])
    blocks_data[str(i)] = blocks[str(i)].get_dict()

# Save to JSON file
with open("blocks_v1.json", "w") as f:
    json.dump(blocks_data, f)

# Test code block v2
t0 = b2("Ryunabi", g0)
print(t0.get_dict())
t1 = b2("abc", t0)
print(t1.get_dict())
print(t0._get_hash(json.dumps(t0.get_dict())) == t1.link)
blocks = {}
blocks_data = {}
blocks["0"] = b2("Ryunabi", g0)
blocks_data["0"] = blocks["0"].get_dict()
for i in range(1, 10):
    blocks[str(i)] = b2(f"abc{i}", blocks[str(i - 1)])
    blocks_data[str(i)] = blocks[str(i)].get_dict()

# Save to JSON file
with open("blocks_v2.json", "w") as f:
    json.dump(blocks_data, f)
