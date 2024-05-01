from csv_2_json import *

players = ['Antonio Rüdiger','Éder Militão','Dani Carvajal','Ferland Mendy',
           'Marquinhos','Presnel Kimpembe','Achraf Hakimi','Nuno Mendes',
           'Dayot Upamecano','Matthijs de Ligt', 'Alphonso Davies', 'Benjamin Pavard',
           'Mats Hummels','Nico Schlotterbeck','Raphaël Guerreiro','Niklas Süle']

csv_files = [ ruta_limpia("ucl_standard_stats.csv"), ruta_limpia("ucl_miscellanous.csv"), ruta_limpia("ucl_player_playing_time.csv"), ruta_limpia("ucl_possession.csv"),
            ruta_limpia("ucl_defensive_actions.csv")]

for player_name in players:
    adapter = Csv2Json()
    player_name_ = player_name.replace(' ', '_')
    player_data = adapter.load_data(player_name, csv_files)
    save_data_to_json(player_data, r'docs\data\json\{player}.json'.format(player=player_name_))
    print("Datos exportados exitosamente en el archivo {player}.json".format(player = player_name_))
