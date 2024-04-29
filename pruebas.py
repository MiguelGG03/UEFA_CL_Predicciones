import os

directory = r'docs\data\equipos_jugadores\real_madrid'

for filename in os.listdir(directory):
        if filename.endswith('.json'):
            file_path = os.path.join(directory, filename)
            print(file_path)