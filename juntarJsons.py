import json
from csv_2_json import save_data_to_json
from jsonComposite import merge_json_files

# Usar la función

PATH_EQUIPOS_JUGADORES = r'docs\data\equipos_jugadores'

PATH_EQUIPOS = r''

merge_json_files(PATH_EQUIPOS+r'\real_madrid', 'output.json')
