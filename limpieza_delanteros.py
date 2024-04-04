import pandas as pd
import os

defenders = pd.read_csv(r'.\docs\data\PlayerStats_22_23\defensive_actions.csv')
# Atleti
# Real Madrid
defensas_23_24 = ["José María Giménez","Nahuel Molina","Mario Hermoso","Stefan Savić"
                  "Éder Militão","Dani Carvajal","Ferland Mendy","Antonio Rüdiger"]

#Equipos

equipos = ["Atletico Madrid", "Real Madrid","Barcelona","Manchester City","Arsenal",]


# Si el portero no está en la lista de defensas, se elimina esa fila
defenders = defenders[defenders['Player'].isin(defensas_23_24)]
# crear carpeta, si existe pasar
os.makedirs(r'.\docs\data\clear', exist_ok=True)
defenders.to_csv(r'.\docs\data\clear\defensive_actions.csv', index=False)