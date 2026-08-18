import asyncio
from nautilus_trader.config import TradingNodeConfig
from nautilus_trader.live.node import TradingNode

async def main():
    # Initialize the basic node configuration
    config = TradingNodeConfig(
        data_clients={},
        exec_clients={},
        timeout_connection=10.0,
        timeout_reconciliation=5.0,
        timeout_portfolio=5.0,
    )
    
    # Instantiate the trading node
    node = TradingNode(config=config)
    
    print("Nautilus Trading Engine initialized successfully.")
    
    # Start the node
    await node.start()
    print("Node is running. Ready to attach Monad data feeds.")
    
    # Keep alive for demonstration
    await asyncio.sleep(5)
    
    # Graceful shutdown
    await node.stop()
    print("Node stopped.")

if __name__ == "__main__":
    asyncio.run(main())
