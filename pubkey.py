from two1.lib.bitcoin.crypto import PublicKey
from two1.lib.wallet import Wallet
from two1.lib.bitcoin.utils import bytes_to_str

wallet = Wallet()
pubkey = wallet.get_payout_public_key()
compressed = pubkey.compressed_bytes
str = bytes_to_str(pubkey.compressed_bytes).upper()

print("Payout public key: %s" % (str))



