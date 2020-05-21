import pandas as pd
import json
with open('test1.json', 'r') as f:
    value = json.load(f)


value = pd.DataFrame.from_dict(value['result'])
print(type(value))

value.to_csv(r'test2.csv', index=None)
