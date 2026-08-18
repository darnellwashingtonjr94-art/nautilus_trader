import asyncio
import json
import logging
import os
import websockets

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("MonadFeed")

WS_URL = os.getenv("MONAD_WS_URL", "wss://testnet-rpc.monad.xyz/ws")

async def subscribe_new_heads():
    """Connects to Monad WebSocket and subscribes to incoming block headers."""
    async with websockets.connect(WS_URL) as ws:
        subscribe_msg = {
            "jsonrpc": "2.0",
            "id": 1,
            "method": "eth_subscribe",
            "params": ["newHeads"],
        }
        await ws.send(json.dumps(subscribe_msg))
        logger.info("Subscribed to Monad newHeads feed...")

        while True:
            try:
                message = await ws.recv()
                data = json.loads(message)
                if "params" in data:
                    block_num = int(data["params"]["result"]["number"], 16)
                    logger.info(f" New Monad Block: {block_num}")
            except websockets.ConnectionClosed:
                logger.warning("WebSocket connection closed. Reconnecting...")
                break

if __name__ == "__main__":
    asyncio.run(subscribe_new_heads())
