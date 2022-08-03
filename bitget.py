from datetime import datetime
import time


BITGET_API_ROOT = "https://api.bitget.com"
CANDLESTICK_API = "/api/mix/v1/market/candles"
timestep_dict = {
    '1min':60,
    '5min': 300,
    '15min': 900,
    '30min': 1800,
    '1hour': 3600,
    '4hour': 14400,
    '12hour': 43200,
    '1day': 86400,
    '1week': 604800,
}
timestep = timestep_dict['15min']
start_time_string = '2019-07-11 09:00:00'
start_time = datetime.datetime.strptime(start_time_string, '%Y-%m-%d %H:%M:%S')
end_time_string = '20-07-11 09:00:00'
end_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
QUERY = \
    BITGET_API_ROOT + \
    CANDLESTICK_API + \
    f"?symbol=BTCUSDT_UMCBL&granularity={timestep}&startTime={start_time}&endTime={end_time}"