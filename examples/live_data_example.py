#!/usr/bin/env python3
"""
Example of using the live_data function
"""

import asyncio
from api import TradingView

async def main():
    def on_data(data):
        print(data)

    async with TradingView() as tv:
        await tv.live_data("BINANCE:BTCUSDT", "1", on_data)

if __name__ == "__main__":
    asyncio.run(main())
