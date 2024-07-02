import datetime
import hashlib
import json
import sqlite3
import redis

class Block:
    def __init__(self, index, timestamp, previous_hash, proof, data):
        self.index = index
        self.timestamp = timestamp
        self.previous_hash = previous_hash
        self.proof = proof
        self.data = data
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_string = json.dumps(
            {
                "index": self.index,
                "timestamp": str(self.timestamp),
                "previous_hash": self.previous_hash,
                "proof": self.proof,
                "data": self.data,
            },
            sort_keys=True,
        ).encode()
        return hashlib.sha256(block_string).hexdigest()


class Blockchain:
    def __init__(self):
        self.chain = []
        self.create_genesis_block()
        # Connect to Redis
        self.db = redis.Redis(host='localhost', port=6379, db=0)
        self.db.save(100,1)
        self.db.set("hello","world")
        print(self.db.get("hello"))
        # Connect to the SQLite database
        #self.conn = sqlite3.connect("bitcoin_blockchain.db")
        #self.cursor = self.conn.cursor()
        #self.create_table()
        # Load existing blocks from the database
        #self.load_chain_from_db()

    def create_genesis_block(self):
        # Create the first block (genesis block)
        genesis_block = Block(
            index=0,
            timestamp=datetime.datetime.now(),
            previous_hash="0",
            proof=1,
            data="Genesis Block",
        )
        self.chain.append(genesis_block)

    def create_block(self, proof, data):
        # Create a new block and add it to the chain
        previous_block = self.chain[-1]
        new_block = Block(
            index=len(self.chain),
            timestamp=datetime.datetime.now(),
            previous_hash=previous_block.hash,
            proof=proof,
            data=data,
        )
        self.chain.append(new_block)
        print("hi")
        self.db.set(len(self.chain), str(new_block))
        # Save the block to the database
        #self.cursor.execute(
        #    """
        #    INSERT INTO blockchain (index, timestamp, previous_hash, proof, data, hash)
        #    VALUES (?, ?, ?, ?, ?, ?)
        #""",
        #    (
        #        new_block.index,
        #        str(new_block.timestamp),
        #        new_block.previous_hash,
        #        new_block.proof,
        #        new_block.data,
        #        new_block.hash,
        #    ),
        #)
        #self.conn.commit()

    def proof_of_work(self, previous_proof):
        # Find a proof that satisfies the condition (e.g., hash starts with '00000')
        new_proof = 1
        while True:
            hash_operation = hashlib.sha256(
                str(new_proof**2 - previous_proof**2).encode()
            ).hexdigest()
            if hash_operation[:5] == "00000":
                return new_proof
            new_proof += 1

    def is_chain_valid(self):
        # Check if the entire chain is valid
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]
            if current_block.previous_hash != previous_block.hash:
                return False
        return True

    def save_chain_to_json(self, filename="blockchain.json"):
        with open(filename, "w") as json_file:
            json.dump([block.__dict__ for block in self.chain], json_file, indent=4)
        print(f"Blockchain saved to {filename}")

    def create_table(self):
        # Create a table to store blocks
        self.cursor.execute(
            """CREATE TABLE IF NOT EXISTS blockchain (
              index INTEGER PRIMARY KEY,
              timestamp TEXT,
              previous_hash TEXT,
              proof INTEGER,
              data TEXT,
              hash TEXT)"""
        )
        self.conn.commit()

    def load_chain_from_db(self):
        #self.cursor.execute("SELECT * FROM blockchain ORDER BY index")
        #rows = self.cursor.fetchall()
        #for row in rows:
        #    block = Block(
        #        index=row[0],
        #        timestamp=row[1],
        #        previous_hash=row[2],
        #        proof=row[3],
        #        data=row[4],
        #    )
        #    self.chain.append(block)
        pass

    def search_blocks_by_data(self, target_data):
        matching_blocks = []
        for block in self.chain:
            if block.data == target_data:
                matching_blocks.append(block)
        return matching_blocks

    def is_data_in_chain(self, target_data):
        for block in self.chain:
            if block.data == target_data:
                return True
        return False

    def is_data_unique(self, target_data):
        data_set = set()
        for block in self.chain:
            if block.data in data_set:
                return False
            data_set.add(block.data)
        return True

    def mine_block(self, data):
        previous_block = self.chain[-1]
        proof = self.proof_of_work(previous_block.proof)
        new_block = Block(
            index=len(self.chain),
            timestamp=datetime.datetime.now(),
            previous_hash=previous_block.hash,
            proof=proof,
            data=data,
        )
        self.chain.append(new_block)


# Example usage:
if __name__ == "__main__":
    my_blockchain = Blockchain()
    proof = my_blockchain.proof_of_work(my_blockchain.chain[-1].proof)
    my_blockchain.create_block(proof=proof, data="Some transaction data")
    print("Blockchain is valid:", my_blockchain.is_chain_valid())
    # Example usage:
    my_blockchain.create_block(proof=123, data="Some transaction data")
    my_blockchain.save_chain_to_json()
    my_blockchain.create_block(proof=456, data="Another transaction data")
    # Example usage:
    print("Loaded blockchain from database:")
    for block in my_blockchain.chain:
        print(f"Block {block.index}: {block.data}")
    # Example usage:
    # Assuming you have added some blocks to the chain
    data_to_check = 'Some transaction data'  # Replace with the data you want to check
    print(f"Data '{data_to_check}' exists in the blockchain:", my_blockchain.is_data_in_chain(data_to_check))
    print(f"Data '{data_to_check}' is unique in the blockchain:", my_blockchain.is_data_unique(data_to_check))
    # Example Usage
    my_blockchain.mine_block(data='Some transaction data')
    print("Blockchain is valid:", my_blockchain.is_chain_valid())
