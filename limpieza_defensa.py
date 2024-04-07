import pandas as pd
import os

def no_ucl_in_name(nombre_archivo:str):
    nombre_final = nombre_archivo.split('_')
    nombre_final.remove('ucl')
    nombre_final = '_'.join(nombre_final)
    return nombre_final


def limpieza(nombre_archivo:str):
    df = pd.read_csv(r'.\docs\data\PlayerStats_22_23\{}.csv'.format(nombre_archivo))

    equipos = ['Real Madrid','Atletico','Paris S-G','Manchester City','Arsenal','Dortmund','Barcelona','Bayern Munich']


    df = df[df['Club'].isin(equipos)]

    nombre_final = no_ucl_in_name(nombre_archivo)

    os.makedirs(r'.\docs\data\clear\defenders', exist_ok=True)
    
    df.to_csv(r'.\docs\data\clear\defenders\{}.csv'.format(nombre_final), index=False)

limpieza(input('Nombre del archivo: '))
