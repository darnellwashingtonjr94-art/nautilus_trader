import asyncio
import logging
from config import get_node_config
from nautilus_trader.live.node import TradingNode

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("MonadHFTMain")

async def run_node():
    logger.info("Starting Monad-HFT-Node engine...")
    
    # Initialize Nautilus Node
    config = get_node_config()
    node = TradingNode(config=config)

    try:
        await node.start()
        logger.info("Engine running. Press Ctrl+C to stop.")
        
        # Keep loop running for live execution
        while node.is_running:
            await asyncio.sleep(1)
            
    except KeyboardInterrupt:
        logger.info("Shutdown signal received.")
    finally:
        await node.stop()
        logger.info("Node shut down successfully.")

if __name__ == "__main__":
    asyncio.run(run_node())
