import hashlib
import json
from time import time

    # creat a blockchain class
class Blockchain(object):
    def __init__(self):
        self.chain=[]
        self.pending_transactions=[]
        self.new_block(previous_hash="The Time 20/03/2021 ", proof=100)

    # write a function to build new blocks
    def new_block(self, proof , previous_hash=None):
        block={
            'index': len(self.chain) + 1 ,
            'timestamp': time() ,
            'transactions': self.pending_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1]),
        }
        self.pending_transactions=[]
        self.chain.append(block)
        return block
    #functions to creat new transactions & get the last block
    @property
    def last_block(self):
        return self.chain[-1]
    def new_transaction(self, sender , recipient , amount):
        transaction={
            'amount': amount,
            'sender': sender,
            'recipient': recipient,
        }
        self.pending_transactions.append(transaction)
        return self.last_block['index']+1

    #  write a function to HASH our blocks
    def hash(self, block):
        strin_objects=json.dumps(block, sort_keys=True)
        block_string=strin_objects.encode()
        raw_hash=hashlib.sha256(block_string)
        hex_hash=raw_hash.hexdigest()

        return hex_hash


# create new blockchains and send some money
blockchain=Blockchain()
t1=blockchain.new_transaction("0.043", "Elin" , "Nani")
t2=blockchain.new_transaction("454.02" , "Nani" , "Elin")
t3=blockchain.new_transaction("1.003" , "Sinatra" , "Micheal")
blockchain.new_block(12345)

t4=blockchain.new_transaction("3 BTC", "Alice" , "Zara")
t5=blockchain.new_transaction("1 BTC" , "Joe" , "Kiel")
t6=blockchain.new_transaction("10 BTC" , "joe" , "Alice")
blockchain.new_block(4090)

print("Blockchain:" , blockchain.chain)
