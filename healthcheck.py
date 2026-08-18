import sys
import time
from web3 import Web3

RPC_URL = "https://testnet-rpc.monad.xyz"

def check_health():
    w3 = Web3(Web3.HTTPProvider(RPC_URL))
    
    start_time = time.time()
    is_connected = w3.is_connected()
    latency = (time.time() - start_time) * 1000

    if not is_connected:
        print("[FAIL] Cannot connect to Monad RPC.")
        sys.exit(1)

    block_number = w3.eth.block_number
    print(f"[OK] Connected to Monad | Latest Block: {block_number} | Latency: {latency:.2f}ms")
    
    if latency > 500:
        print("[WARN] High latency detected on RPC endpoint.")
        sys.exit(1)

    sys.exit(0)

if __name__ == "__main__":
    check_health()
