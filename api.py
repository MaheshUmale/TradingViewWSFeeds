
from TradingView.client import Client
from TradingView.chart_session import ChartSession

import asyncio
from typing import Callable, Dict, Any
import pandas as pd

class TradingView:
    """
    Simplified interface for TradingView API
    """

    def __init__(self, debug: bool = True):
        self.client = Client(debug=debug)
        self.client.on_error(self._on_error)

    async def __aenter__(self):
        await self.client.connect()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        self.client.disconnect()

    def _on_error(self, *error):
        print(f"Error: {error}")

    async def live_data(self, symbol: str, timeframe: str, on_data: Callable[[Dict[str, Any]], None], chart_type: str = None, chart_inputs: Dict[str, Any] = None):
        """
        Subscribe to live data for a symbol and timeframe.
        """
        session = ChartSession(self.client)
        session.on_update(lambda data: on_data(data))

        options = {
            'timeframe': timeframe,
        }
        if chart_type:
            options['type'] = chart_type
            if chart_inputs:
                options['inputs'] = chart_inputs

        session.set_market(symbol, options)

        try:
            while True:
                await asyncio.sleep(1)
        except KeyboardInterrupt:
            pass
        finally:
            session.unsubscribe()

    async def get_historical_data(self, symbol: str, timeframe: str, n_bars: int, chart_type: str = None, chart_inputs: Dict[str, Any] = None) -> pd.DataFrame:
        """
        Download historical data for a symbol and timeframe.
        """
        session = ChartSession(self.client)

        data_event = asyncio.Event()

        def on_data(data):
            if len(data['periods']) >= n_bars:
                data_event.set()

        session.on_update(on_data)

        options = {
            'timeframe': timeframe,
            'range': n_bars,
        }
        if chart_type:
            options['type'] = chart_type
            if chart_inputs:
                options['inputs'] = chart_inputs

        session.set_market(symbol, options)

        try:
            await asyncio.wait_for(data_event.wait(), timeout=20)
        except asyncio.TimeoutError:
            print("Timeout waiting for data")
            return pd.DataFrame()

        df = pd.DataFrame(session.periods_list)
        df = df.sort_values(by='time').reset_index(drop=True)

        session.unsubscribe()

        return df
