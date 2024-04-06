import pandas as pd
import os

df = pd.read_csv(r'.\docs\data\PlayerStats_22_23\ucl_shooting.csv')

equipos = ['Real Madrid','Atletico','Paris S-G','Manchester City','Arsenal','Dortmund','Barcelona','Bayern Munich']


df = df[df['Club'].isin(equipos)]
# crear carpeta, si existe pasar
os.makedirs(r'.\docs\data\clear\strikers', exist_ok=True)
df.to_csv(r'.\docs\data\clear\strikers\shooting.csv', index=False)