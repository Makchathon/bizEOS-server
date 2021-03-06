DEFAULT_EOS_API_ENDPOINT = 'https://api.tokenika.io'


WALLET_OPEN = '/v1/wallet/open'
WALLET_UNLOCK = 'v1/wallet/unlock'  # ["default","PW5Jrjd3cnRwBf7ffHa8rxQaHk1KqToAkdZdGC814cuvbr2jyzG8Z"]
WALLET_LOCK = 'v1/wallet/lock'
WALLET_SIGN_TRANSACTION = 'v1/wallet/sign_transaction'
WALLET_GET_PUBLIC_KEYS = 'v1/wallet/get_public_keys'  # < [K1, K2, K3]

CHAIN_GET_INFO = 'v1/chain/get_info'
CHAIN_GET_BLOCK = 'v1/chain/get_block'
CHAIN_PUSH_TRANSACTION = 'v1/chain/push_transaction'
CHAIN_PUSH_TRANSACTIONS = 'v1/chain/push_transactions'
CHAIN_ABI_JSON_TO_BIN = 'v1/chain/abi_json_to_bin'
CHAIN_GET_REQUIRED_KEYS = 'v1/chain/get_required_keys'
# > {'transaction: tr, 'available_keys': [K1, K2, K3]}
# < {"required_keys":["EOS8DckpYhRu9rfkTxfNioG8LLjM1yfoQjc858RjXxFBkNBkaZxM7"]}


HISTORY_GET_ACTIONS = 'v1/history/get_actions'
HISTORY_GET_TRANSACTION = 'v1/history/get_transaction'
