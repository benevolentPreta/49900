from blockchain import Blockchain


local_blockchain = Blockchain()


def add_block_from_file():
    with open('fat.txt', 'r') as FAT:
        data = FAT.read()
        local_blockchain.add_block(data)


# save blockchain to file
def saveBlockchain():
    file = open('blockchain.txt', 'w')
    for i in range(len(local_blockchain.chain)):
        current_block = local_blockchain.chain[i]
        file.write(str(current_block.time_stamp))
        file.write('\n')
        file.write(str(current_block.transactions))
        file.write('\n')
        file.write(str(current_block.generate_hash))
        file.write('\n')
        file.write(str(current_block.previous_hash))
        file.write('\n===\n')


# print blockchain after adding new transaction
local_blockchain.print_blocks()
