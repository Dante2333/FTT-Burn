import requests
import pandas as pd
from converterday import convtoday


def get_ftt_price(date):
    start_time = str(convtoday(date))
    date2 = int(start_time) + 24*60*60
    end_time = str(date2)
    base = 'https://ftx.com/api'
    symbol = "FTT/USD"
    params = "/markets/"+symbol+"/candles?resolution=86400&limit=1"
    params2 = "&start_time=" + start_time+"&end_time="+end_time
    response = requests.get(base+params+params2)
    address_response = response.json()
    df = pd.DataFrame.from_dict(address_response['result'])
    df['price'] = (df['high']+df['low']+df['close']+df['open'])/4
    return(df['price'])
