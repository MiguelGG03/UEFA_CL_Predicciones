import pandas as pd
import os

goolkeeping = pd.read_csv(r'.\docs\data\PlayerStats_22_23\ucl_advanced_goalkeeping.csv')
porteros_23_24 = ["Gianluigi Donnarumma", "Marc-André ter Stegen", "Jan Oblak", "Andriy Lunin", "Manuel Neuer", "Gregor Kobel", "Ederson"]


# Si el portero no está en la lista de porteros, se elimina esa fila
goolkeeping = goolkeeping[goolkeeping['Player'].isin(porteros_23_24)]
# crear carpeta, si existe pasar
os.makedirs(r'.\docs\data\clear', exist_ok=True)
goolkeeping.to_csv(r'.\docs\data\clear\ucl_advanced_goalkeeping.csv', index=False)