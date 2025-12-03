# TradingView WebSocket API

This Python library provides a simplified interface for interacting with the TradingView WebSocket API, allowing you to fetch both live and historical market data for regular and specialized chart types, including RangeBars.

## Features

- **Live Data Streaming**: Subscribe to real-time data for any symbol and timeframe.
- **Historical Data**: Download historical data as a pandas DataFrame.
- **Regular and RangeBar Charts**: Fetch data for both regular and RangeBar charts.
- **Asynchronous**: Built with `asyncio` for efficient, non-blocking I/O.

## Installation

To install the library, you can use `pip`:

```bash
pip install -r requirements.txt
```

## Usage

### Getting Historical Data

You can download historical data for a symbol and timeframe using the `get_historical_data` method. The method returns a pandas DataFrame.

#### Regular Chart

```python
import asyncio
from api import TradingView

async def main():
    async with TradingView() as tv:
        df = await tv.get_historical_data('BINANCE:BTCUSDT', '1D', 100)
        print(df)

if __name__ == '__main__':
    asyncio.run(main())
```

#### RangeBar Chart

To get data for a RangeBar chart, specify the `chart_type` and `chart_inputs`.

```python
import asyncio
from api import TradingView

async def main():
    async with TradingView() as tv:
        df = await tv.get_historical_data(
            'BINANCE:BTCUSDT',
            '1D',
            100,
            chart_type='Range',
            chart_inputs={'range': '1000'}
        )
        print(df)

if __name__ == '__main__':
    asyncio.run(main())
```

### Getting Live Data

You can subscribe to live data for a symbol and timeframe using the `live_data` method. The method takes a callback function that will be called with each data update.

#### Regular Chart

```python
import asyncio
from api import TradingView

def on_data(data):
    print(data)

async def main():
    async with TradingView() as tv:
        await tv.live_data('BINANCE:BTCUSDT', '1D', on_data)

if __name__ == '__main__':
    asyncio.run(main())
```

#### RangeBar Chart

To get live data for a RangeBar chart, specify the `chart_type` and `chart_inputs`.

```python
import asyncio
from api import TradingView

def on_data(data):
    print(data)

async def main():
    async with TradingView() as tv:
        await tv.live_data(
            'BINANCE:BTCUSDT',
            '1D',
            on_data,
            chart_type='Range',
            chart_inputs={'range': '1000'}
        )

if __name__ == '__main__':
    asyncio.run(main())
```
