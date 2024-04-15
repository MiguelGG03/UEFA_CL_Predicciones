import pandas as pd
import json

class DataInterface:
    def load_data(self, player_name, csv_files):
        raise NotImplementedError

class Csv2Json(DataInterface):
    def load_data(self, player_name, csv_files):
        player_data = {}
        for file in csv_files:
            df = pd.read_csv(file)
            # Suponiendo que existe una columna 'Player' que identifica al jugador
            player_info = df[df['Player'] == player_name].iloc[0].to_dict()
            for key, value in player_info.items():
                if key not in player_data:
                    player_data[key] = value
        return player_data

def save_data_to_json(data, filename):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)
        
def ruta(nombre):
    return r'docs\data\PlayerStats_22_23\{nombre}'.format(nombre=nombre)



"""
# Uso de las clases
adapter = Csv2Json()
player_name = "Lionel Messi"  # Ejemplo de nombre
csv_files = [ ruta("ucl_passing.csv"), ruta("ucl_player_playing_time.csv")]  # Lista de tus archivos CSV

player_data = adapter.load_data(player_name, csv_files)
save_data_to_json(player_data, '{player}.json'.format(player=player_name))
print("Datos exportados exitosamente.")
"""