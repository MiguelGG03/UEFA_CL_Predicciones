import pandas as pd

data = pd.read_json('docs/data/equipos/real_madrid.json').to_dict('records')[1]

print(data["Player"])
