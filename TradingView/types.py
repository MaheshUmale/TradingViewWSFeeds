
from typing import Dict, List, Any, Literal, TypedDict

TimeFrame = Literal['1', '5', '15', '30', '45', '60', '120', '180', '240', '1D', '1W', '1M']
MarketSymbol = str
ChartType = Literal['HeikinAshi', 'Renko', 'LineBreak', 'Kagi', 'PointAndFigure', 'Range']
ChartInputs = Dict[str, Any]

class ChartOptions(TypedDict, total=False):
    adjustment: Literal['splits', 'dividends']
    session: Literal['regular', 'extended']
    currency: str
    type: ChartType
    inputs: ChartInputs
    range: int
    to: int
    backadjustment: bool
    timeframe: TimeFrame

class PricePeriod(TypedDict):
    time: int
    open: float
    close: float
    max: float
    min: float
    volume: float

class MarketInfos(TypedDict, total=False):
    series_id: str
    # Add other fields as needed

CHART_TYPES: Dict[ChartType, str] = {
    'HeikinAshi': 'BarSetHeikenAshi@tv-basicstudies-60!',
    'Renko': 'BarSetRenko@tv-prostudies-40!',
    'LineBreak': 'BarSetPriceBreak@tv-prostudies-34!',
    'Kagi': 'BarSetKagi@tv-prostudies-34!',
    'PointAndFigure': 'BarSetPnF@tv-prostudies-34!',
    'Range': 'BarSetRange@tv-basicstudies-72!',
}
