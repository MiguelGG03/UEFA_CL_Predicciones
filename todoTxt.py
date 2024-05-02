import json 
import os


def data_json_to_list(equipo):
    arrive_directory = r'docs\data\txt\{equipo}.txt'.format(equipo=equipo)
    directory = r'docs\data\equipos_jugadores\{equipo}'.format(equipo=equipo)

    lista = []
    
    for filename in os.listdir(directory):
        if filename.endswith('.json'):
            file_path = os.path.join(directory, filename)
            print(file_path)
            with open(file_path, 'r') as file:
                data = json.load(file)
                lista.append(data)
        with open(arrive_directory, 'w') as file:
            file.write(json.dumps(lista, indent=4, sort_keys=True, default=str))
                
equipos = ['real_madrid','paris_saint_germain','borussia_dormund','bayern_munich']


for equipo in equipos:
    data_json_to_list(equipo)