import pandas as pd
from config import PLANTILLA_REAL_MADRID

data = pd.read_json('docs/data/equipos/real_madrid.json').to_dict('records')[1]

for name in PLANTILLA_REAL_MADRID:
    print(name)
    print(data[name])
    print('---')
