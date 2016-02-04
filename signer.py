from two1.lib.bitcoin.crypto import PublicKey
from two1.lib.bitcoin.txn import Transaction
from two1.lib.wallet import Wallet
from two1.lib.bitcoin.script import Script
from two1.lib.blockchain.twentyone_provider import TwentyOneProvider
import two1.lib.bitcoin as bitcoin

provider = TwentyOneProvider()
wallet = Wallet()

pubkey = input("Please enter the public key that was used to create the script")
tx_hex = input("Please enter the transaction hex")
server_pubkey = input("Please enter server pub key")
white_pubkey = input("Please enter white pub key")
black_pubkey = input("Please enter black pub key")


their_pubkey = PublicKey.from_bytes(pubkey)
tx = Transaction.from_hex(tx_hex)

private_key = wallet.get_private_for_public(their_pubkey)
public_keys = [PublicKey.from_bytes(server_pubkey).compressed_bytes, PublicKey.from_bytes(white_pubkey).compressed_bytes, PublicKey.from_bytes(black_pubkey).compressed_bytes]
redeem_script = Script.build_multisig_redeem(2, public_keys)

for i, inp in enumerate(tx.inputs):
   tx.sign_input(i, bitcoin.Transaction.SIG_HASH_ALL, private_key, redeem_script)

txid = provider.broadcast_transaction(tx.to_hex())

print("Transaction ID: {}".format(txid))

