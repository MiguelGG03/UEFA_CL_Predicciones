from csv_2_json import *

players = ['Toni Kroos','Luka Modrić','Federico Valverde',
           'Marco Verratti','Leandro Paredes','Danilo Pereira',
           'Joshua Kimmich','Leon Goretzka','Jamal Musiala',
           'Jude Bellingham','Marco Reus','Emre Can',]

csv_files = [ ruta_limpia("ucl_standard_stats.csv"), ruta_limpia("ucl_miscellanous.csv"), ruta_limpia("ucl_player_playing_time.csv"), ruta_limpia("ucl_possession.csv"),
            ruta_limpia("ucl_passing.csv")]

for player_name in players:
    adapter = Csv2Json()
    player_name_ = player_name.replace(' ', '_')
    player_data = adapter.load_data(player_name, csv_files)
    save_data_to_json(player_data, r'docs\data\json\{player}.json'.format(player=player_name_))
    print("Datos exportados exitosamente en el archivo {player}.json".format(player = player_name_))
