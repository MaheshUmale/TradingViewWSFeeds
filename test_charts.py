
import asyncio
from api import TradingView

async def main():
    """
    Test script for verifying chart type implementations
    """
    async with TradingView(debug=True) as tv:
        # Define chart types and their specific inputs
        chart_types_to_test = {
            'Range': {'inputs': {'range': 1}},
        }

        # Symbol and timeframe for testing
        symbol = "BINANCE:BTCUSDT"
        timeframe = "1D"
        n_bars = 10

        # Test each chart type
        for chart_type, options in chart_types_to_test.items():
            print(f"--- Testing {chart_type} ---")
            try:
                # Get historical data with the specified chart type
                df = await tv.get_historical_data(
                    symbol,
                    timeframe,
                    n_bars,
                    chart_type=chart_type,
                    chart_inputs=options.get('inputs', {})
                )

                # Verify that data is received
                if df is not None and not df.empty:
                    print(f"Successfully received data for {chart_type}")
                    print(df.head())
                else:
                    print(f"Failed to receive data for {chart_type}")

            except Exception as e:
                print(f"An error occurred while testing {chart_type}: {e}")

            print("-" * (len(chart_type) + 12))

if __name__ == "__main__":
    asyncio.run(main())
