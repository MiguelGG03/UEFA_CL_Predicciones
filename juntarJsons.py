import json
from jsonComposite import merge_json_files

# Usar la función

PATH_EQUIPOS_JUGADORES = r'docs\data\equipos_jugadores'

PATH_EQUIPOS = r'docs\data\equipos'

merge_json_files(PATH_EQUIPOS_JUGADORES+r'\real_madrid', PATH_EQUIPOS+r'real_madrid.json')
merge_json_files(PATH_EQUIPOS_JUGADORES+r'\bayer_munich', PATH_EQUIPOS+r'bayer_munich.json')
merge_json_files(PATH_EQUIPOS_JUGADORES+r'\borussia_dormund', PATH_EQUIPOS+r'borussia_dormund.json')
merge_json_files(PATH_EQUIPOS_JUGADORES+r'\paris_saint_germain', PATH_EQUIPOS+r'paris_saint_germain.json')
