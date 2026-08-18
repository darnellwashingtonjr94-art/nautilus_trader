import os
from nautilus_trader.config import (
    LoggingConfig,
    TradingNodeConfig,
)

# Load sensitive RPC endpoints from environment variables
MONAD_RPC_URL = os.getenv("MONAD_RPC_URL", "https://testnet-rpc.monad.xyz")
MONAD_WS_URL = os.getenv("MONAD_WS_URL", "wss://testnet-rpc.monad.xyz/ws")

def get_node_config() -> TradingNodeConfig:
    """Builds and returns the Nautilus Trading Engine node configuration."""
    return TradingNodeConfig(
        trader_id="MONAD-HFT-01",
        logging=LoggingConfig(
            log_level="INFO",
            log_directory="logs",
            log_component_levels={"TradingNode": "INFO"},
        ),
        timeout_connection=10.0,
        timeout_reconciliation=5.0,
        timeout_portfolio=5.0,
    )
