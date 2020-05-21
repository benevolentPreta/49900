from blockchain import Blockchain
import os


def clear(): return os.system('cls')  # Clear screen for windows


clear()

# Initiate Blockchain
local_blockchain = Blockchain()

# Create 3 transactions
block_one_transactions = {
    "Folder Name": "CSCI 335",
    "File Name": "Assignment 1"
}

block_two_transactions = {
    "Folder Name": "CSCI 335",
    "File Name": "Assignment 2"
}

block_three_transactions = {
    "Folder Name": "CSCI 335",
    "File Name": "Notes"
}


fake_transactions = {
    "Folder Name": "CSCI 335",
    "File Name": "Fake File"
}


# # print With only genesis block
# print("\nNEW BLOCKCHAIN:")
# local_blockchain.print_blocks()

# Add 3 transactions to blockchain
local_blockchain.add_block(block_one_transactions)
local_blockchain.add_block(block_two_transactions)
local_blockchain.add_block(block_three_transactions)

# print after adding 3 transactions
print("\n\nBLOCKCHAIN AFTER 3 TRANSACTIONS:")
local_blockchain.print_blocks()


# Attempt to modify 2nd transaction (2 after genesis block)
local_blockchain.chain[2].transactions = fake_transactions

print("\n\nBLOCKCHAIN AFTER MODIFYING 2ND TRANSACTION:")
local_blockchain.print_blocks()

# Run verification
print("\n\n VERIFYING BLOCKCHAIN:")
local_blockchain.validate_chain()
print("\n")
