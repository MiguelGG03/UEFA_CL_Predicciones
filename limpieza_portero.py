from csv_2_json import *

players = ['Thibaut Courtois','Marc-André ter Stegen','Manuel Neuer','Jan Oblak','Ederson','Gregor Kobel','Gianluigi Donnarumma']

csv_files = [ ruta_limpia("ucl_advanced_goalkeeping.csv"), ruta_limpia("ucl_goalkeeper.csv")]

for player_name in players:
    adapter = Csv2Json()
    player_name_ = player_name.replace(' ', '_')
    player_data = adapter.load_data(player_name, csv_files)
    save_data_to_json(player_data, r'docs\data\json\{player}.json'.format(player=player_name_))
    print("Datos exportados exitosamente en el archivo {player}.json".format(player = player_name_))