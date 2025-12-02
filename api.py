"""
TradingView API - Simplified entry point for the library
"""

from TradingView.client import Client
from TradingView.chart_session import ChartSession

import asyncio
from typing import Callable, Dict, Any
import pandas as pd

class TradingView:
    """
    Simplified interface for TradingView API
    """

    def __init__(self, debug: bool = False):
        self.client = Client(debug=debug)
        self.client.on_error(self._on_error)

    async def __aenter__(self):
        await self.client.connect()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        self.client.disconnect()

    def _on_error(self, error):
        print(f"Error: {error}")

    async def live_data(self, symbol: str, timeframe: str, on_data: Callable[[Dict[str, Any]], None]):
        """
        Subscribe to live data for a symbol and timeframe.
        """
        session = ChartSession(self.client)
        session.on_update(lambda data: on_data(data))
        session.subscribe(symbol, timeframe=timeframe)

        try:
            while True:
                await asyncio.sleep(1)
        except KeyboardInterrupt:
            pass
        finally:
            session.unsubscribe()

    async def get_historical_data(self, symbol: str, timeframe: str, n_bars: int) -> pd.DataFrame:
        """
        Download historical data for a symbol and timeframe.
        """
        session = ChartSession(self.client)

        data_event = asyncio.Event()

        def on_data(data):
            if len(data['periods']) >= n_bars:
                data_event.set()

        session.on_update(on_data)
        session.subscribe(symbol, timeframe=timeframe, range_count=n_bars)

        await data_event.wait()

        df = pd.DataFrame(session.periods_list)
        df = df.sort_values(by='time').reset_index(drop=True)

        session.unsubscribe()

        return df
