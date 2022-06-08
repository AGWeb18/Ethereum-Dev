from mailbox import ExternalClashError
from etherscan import Etherscan
import os
import json
import requests 
import pandas as pd

ETHERSCAN_KEY = os.getenv("VAR")
eth = Etherscan(ETHERSCAN_KEY) # key in quotation marks


get_log_call = "https://api.etherscan.io/api?module=logs&action=getLogs&fromBlock=379224&toBlock=400000&address=0x33990122638b9132ca29c723bdf037f1a891a70c&topic0=0xf63780e752c6a54a94fc52715dbc5518a3b4c3c2833d301a204226548a2a8545&topic0_1_opr=and&topic1=0x72657075746174696f6e00000000000000000000000000000000000000000000&apikey={}""".format(ETHERSCAN_KEY)

response = requests.get(get_log_call).json()

df = pd.DataFrame(response['result'])
tx_hash = df["transactionHash"].values