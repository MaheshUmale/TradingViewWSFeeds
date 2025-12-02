#!/usr/bin/env python3
"""
Example of using the get_historical_data function
"""

import asyncio
from api import TradingView

async def main():
    async with TradingView() as tv:
        data = await tv.get_historical_data("BINANCE:BTCUSDT", "1", 100)
        print(data)

if __name__ == "__main__":
    asyncio.run(main())
