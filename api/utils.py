from web3 import Web3
import requests
import os
from datetime import datetime

POLYGON_RPC = "https://polygon-rpc.com"
POLYGONSCAN_API_KEY = os.getenv("POLYGONSCAN_API_KEY")
web3 = Web3(Web3.HTTPProvider(POLYGON_RPC))

DEFAULT_TOKEN_ADDRESS = "0x1a9b54a3075119f1546c52ca0940551a6ce5d2d0"

ERC20_ABI = [
    {
        "constant": True,
        "inputs": [{"name": "_owner", "type": "address"}],
        "name": "balanceOf",
        "outputs": [{"name": "balance", "type": "uint256"}],
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [],
        "name": "decimals",
        "outputs": [{"name": "", "type": "uint8"}],
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [],
        "name": "symbol",
        "outputs": [{"name": "", "type": "string"}],
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [],
        "name": "name",
        "outputs": [{"name": "", "type": "string"}],
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [],
        "name": "totalSupply",
        "outputs": [{"name": "", "type": "uint256"}],
        "type": "function"
    }
]

def get_token_contract(token_address=DEFAULT_TOKEN_ADDRESS):
    return web3.eth.contract(address=Web3.to_checksum_address(token_address), abi=ERC20_ABI)

def get_balance(user_address, token_address=DEFAULT_TOKEN_ADDRESS):
    token = get_token_contract(token_address)
    decimals = token.functions.decimals().call()
    raw_balance = token.functions.balanceOf(Web3.to_checksum_address(user_address)).call()
    return raw_balance / (10 ** decimals)

def get_balance_batch(address_list, token_address=DEFAULT_TOKEN_ADDRESS):
    token = get_token_contract(token_address)
    decimals = token.functions.decimals().call()
    return [
        token.functions.balanceOf(Web3.to_checksum_address(addr)).call() / (10 ** decimals)
        for addr in address_list
    ]

def get_token_info(token_address=DEFAULT_TOKEN_ADDRESS):
    token = get_token_contract(token_address)
    return {
        "symbol": token.functions.symbol().call(),
        "name": token.functions.name().call(),
        "totalSupply": token.functions.totalSupply().call()
    }

def get_top_holders(top_n=10, token_address=DEFAULT_TOKEN_ADDRESS):
    fake_data = [
        ("0x0000000000000000000000000000000000000001", 10000000000000000),
        ("0x0000000000000000000000000000000000000002", 5000000000000000),
        ("0x0000000000000000000000000000000000000003", 2000000000000000),
    ]
    return fake_data[:top_n]


def get_last_tx_date(address, token_address=DEFAULT_TOKEN_ADDRESS):
    url = f"https://api.polygonscan.com/api?module=account&action=tokentx&address={address}&contractaddress={token_address}&sort=desc&apikey={POLYGONSCAN_API_KEY}"
    resp = requests.get(url).json()
    txs = resp.get("result", [])
    if not txs:
        return None
    timestamp = int(txs[0]["timeStamp"])
    return datetime.utcfromtimestamp(timestamp).isoformat()

def get_top_with_last_tx(top_n=10, token_address=DEFAULT_TOKEN_ADDRESS):
    top_holders = get_top_holders(top_n, token_address)
    result = []
    for addr, bal in top_holders:
        last_tx = get_last_tx_date(addr, token_address)
        result.append((addr, bal, last_tx))
    return result
