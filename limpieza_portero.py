from csv_2_json import *

players = ['Thibaut Courtois']

csv_files = [ ruta("ucl_passing.csv"), ruta("ucl_player_playing_time.csv")]

for player_name in players:
    adapter = Csv2Json()
    player_name_ = player_name.replace(' ', '_')
    player_data = adapter.load_data(player_name, csv_files)
    save_data_to_json(player_data, r'docs\data\json\{player}.json'.format(player=player_name_))
    print("Datos exportados exitosamente en el archivo {player}.json".format(player = player_name_))
