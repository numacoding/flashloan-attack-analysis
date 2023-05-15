import web3

# Connect to the Ethereum network using Infura
w3 = web3.Web3(web3.HTTPProvider('https://mainnet.infura.io/v3/36f53c5087d342a18cc9c768213ac6d7'))

# Define the transaction hash to analyze
tx_hash = '0x6200bf5c43c214caa1177c3676293442059b4f39eb5dbae6cfd4e6ad16305668'

# Retrieve the transaction data from the Ethereum network
tx = w3.eth.get_transaction(tx_hash)


# Identify the sender and receiver addresses from the transaction data
sender = tx['from']

#Get the address from the 'creates' field if the transaction is a creation contract
#If not, get it from the 'to' field
if tx['to'] is None:
    contract_address = tx['creates']
else:
    contract_address = tx['to']
    
block_number = tx['blockNumber']
previous_block = block_number -1


# Retrieve the current balance of the sender and receiver addresses
try:
    sender_balance_0 = w3.eth.get_balance(sender, block_identifier=previous_block)
except:
    sender_balance = 0
    
sender_balance_1 = w3.eth.get_balance(sender, block_identifier=block_number)

try:
    receiver_balance_0 = w3.eth.get_balance(receiver, block_identifier=previous_block)
except:
    receiver_balance_0 = 0

receiver_balance_1 = w3.eth.get_balance(receiver, block_identifier=block_number)

print(sender_balance_1-sender_balance_0, (receiver_balance_1-receiver_balance_0))

#print(w3.eth.get_transaction_receipt(tx_hash))