import requests
# import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plot
from get_ftt_price import get_ftt_price

myapi = "EBXKT4PTN38SXXZXI2GPTUA9D5JEMAAHHB"
burn = "0x0000000000000000000000000000000000000000"
startblock = str(826112)
contract = "0x50d1c9771902476076ecfc8b2a83ad6b9355a4c9"

url = "https://api.etherscan.io/api?module=account&action=tokentx&contractaddress="+contract+"&address=" + burn + "&page=1&offset=100&sort=asc&apikey="+myapi
response = requests.get(url)
address_content = response.json()

# with open('test1.json', 'w') as outfile:
#    json.dump(address_content, outfile)
# with open('test1.json') as json_file:
#    address_content = json.load(json_file)


# filter json
value = pd.DataFrame.from_dict(address_content['result'])
# convert timestamp into date
df2 = value[['timeStamp', 'value']]
df2 = df2.drop(0, axis=0)
# create a new series inside the dataframe in order to
# operate division due to ethereum format for numbers
df2['new'] = 10**18
df2['value'] = df2['value'].astype(np.float64)
df2['Burn (FTT)'] = df2['value']/df2['new']
df2['Burn (FTT)'] = df2['Burn (FTT)'].astype(np.int)

df2 = df2.drop(columns="value")
df2 = df2.drop(columns="new")
df2['FTT-price'] = df2['timeStamp'].apply(get_ftt_price)
df2['timeStamp'] = pd.to_datetime(value['timeStamp'], unit='s')
df2['Burn (USD)'] = df2['FTT-price'] * df2['Burn (FTT)']

lines = df2.plot.line(x='timeStamp', y='Burn (USD)')
plot.show(block=True)
