import pandas as pd
import os

df = pd.read_csv(r'.\docs\data\PlayerStats_22_23\ucl_defensive_actions.csv')
# Atleti
# Real Madrid
equipos = ['Real Madrid','Atletico','Paris S-G','Manchester City']


# Si el portero no está en la lista de defensas, se elimina esa fila
df = df[df['Club'].isin(equipos)]
# crear carpeta, si existe pasar
os.makedirs(r'.\docs\data\clear\defenders', exist_ok=True)
df.to_csv(r'.\docs\data\clear\defensive_actions.csv', index=False)