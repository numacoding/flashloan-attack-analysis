import web3

class EthAnalyzer:
    def __init__(self, infura_id):
        # Connect to the Ethereum network using Infura
        w3 = web3.Web3(web3.HTTPProvider('https://mainnet.infura.io/v3/{infura_id}'))

    def get_balance_from_transaction_parties(self, tx_hash):
        # Retrieve the transaction data from the Ethereum network
        tx = w3.eth.get_transaction(tx_hash)

        # Identify the sender and receiver addresses from the transaction data
        sender = tx['from']

        #Get the address from the 'creates' field if the transaction is a creation contract
        #If not, get it from the 'to' field
        if tx['to'] is None:
            receiver = tx['creates']
        else:
            receiver = tx['to']
            
        block_number = tx['blockNumber']
        previous_block = block_number -1


        # I make this try-except in case that the address has no previous values
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

        sender_balance = sender_balance_1 - sender_balance_0
        receiver_balance = receiver_balance_1 - receiver_balance_0

        balances_json = {
            'sender_balance': sender_balance,
            'receiver_balance': receiver_balance
        }

        return balances_json
