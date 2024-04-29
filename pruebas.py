import pandas as pd

print(pd.read_json('docs/data/equipos/real_madrid.json').to_dict('records')[0])

