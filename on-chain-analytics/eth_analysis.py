from etherscan import Etherscan
import os 

ETHERSCAN_KEY = os.getenv("VAR")

eth = Etherscan(ETHERSCAN_KEY) # key in quotation marks

latest_price = eth.get_eth_last_price()
