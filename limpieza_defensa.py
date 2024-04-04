import pandas as pd
import os

defenders = pd.read_csv(r'.\docs\data\PlayerStats_22_23\defensive_actions.csv')
# Atleti
# Real Madrid
equipos = ['Real Madrid','Atletico','Paris S-G','Manchester City']


# Si el portero no está en la lista de defensas, se elimina esa fila
defenders = defenders[defenders['Player'].isin(equipos)]
# crear carpeta, si existe pasar
os.makedirs(r'.\docs\data\clear', exist_ok=True)
defenders.to_csv(r'.\docs\data\clear\defensive_actions.csv', index=False)