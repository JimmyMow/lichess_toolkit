#!/usr/bin/env python3
import json
import os

# import from the 21 Developer Library
from two1.commands.config import Config
from two1.lib.wallet import Wallet
from two1.lib.bitrequests import BitTransferRequests
import two1.lib.bitcoin as bitcoin
from two1.lib.wallet import Wallet

wallet = Wallet()

address = input("Please enter the address of your script")
amount = int(input("Please enter the amount of satoshis you'd like to pay"))

if address and amount:
   deposit_tx_obj = wallet.send_to(address, 25000, False, 5000, [])
   deposit_tx = deposit_tx_obj[0]['txn']
   deposit_tx_id = deposit_tx_obj[0]['txid']
   deposit_utxo_index = deposit_tx.output_index_for_address(address)

   print("--------------------")
   print("Please copy the deposit and the deposit index for later use. You can paste the deposit ID into block explorer if you want to track your transaction.")
   print("--------------------")
   print("Deposit: {}\n".format(deposit_tx.to_hex()))
   print("Deposit index: {}\n".format(deposit_utxo_index))
   print("Deposit ID: {}\n".format(deposit_tx_id))
else:
   print("You must provide an address")
