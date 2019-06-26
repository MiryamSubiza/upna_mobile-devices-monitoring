# -*- coding: utf-8 -*-
"""
@author: Miryam Subiza
"""
from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from pymongo import MongoClient
import pandas as pd
import argparse

# Variables globales
hora_actual = datetime.now()

# Funciones
def getFechaHora(x):
    return (hora_actual - timedelta(hours=x)).strftime("%Y-%m-%dT%H:%M:%S.%fZ")

def getHora(x):
    return (hora_actual - timedelta(hours=x)).strftime("%H:%Mh")

def obtenerGrafico(df, idSensor):
    # Generar gráfico de barras
    fig, ax = plt.subplots()
    fig.set_size_inches(w=13.2,h=4.8) # 1320x480 (px)
    index = np.arange(len(df))
    rects1 = ax.bar(index, df['dispositivos'].tolist(), bar_width,
                    alpha=opacity, color=colors,
                    error_kw=error_config)
    # Añadir número de dispositivos encima de cada barra
    for i, v in enumerate(df['dispositivos'].tolist()):
        if plt.ylim()[1] >= 0.1:
            ax.text(i, v + plt.ylim()[1]/140, str(v), color=colors[i], ha='center')
        else:
            ax.text(i, v + 0.001, str(v), color=colors[i], ha='center')
    
    ax.set_ylim(bottom=0)
    ax.set_title(u'Número de móviles por hora ('+ datetime.now().strftime('%d/%m/%Y - %H:%Mh') +')')        
    ax.set_xticks(index)
    ax.set_xticklabels(df['hora'].tolist())
    if df['dispositivos'].max() <= 4:
        ax.set_yticks(np.arange(df['dispositivos'].max()+1))
    
    fig.tight_layout()
    
    # Guardar gráfico en una imagen
    if idSensor:
        plt.savefig('lth_upna_barplot_' + str(c.split("/")[-1]) + '.png')
    else:
        plt.savefig('lth_upna_barplot.png')

# FIN FUNCIONES
        

# Leer argumentos recibidos por parámetro al ejecutar el script (credenciales BBDD)
parser = argparse.ArgumentParser()
parser.add_argument('--u', help='filename help') # Username
parser.add_argument('--p', help='filename help') # Password
args = parser.parse_args()
if not args.u or not args.p:
    print("Para ejecutar el script: python lth_upna_barplot.py --u=USERNAME --p=PASSWORD")
    exit()

# Cargar, de la BBDD, los datos capturados
client = MongoClient("mongodb://"+args.u+":"+args.p+"@localhost:27017/lth_upna")
db = client["lth_upna"]

# Inicialización de variables comunes para todos los gráficos a generar
df = pd.DataFrame(columns=['hora', 'dispositivos'])
bar_width = 0.35
opacity = 0.8
error_config = {'ecolor': '0.3'}
colors = ['#727272', '#F1595F', '#79C36A', '#599AD3', '#F9A65A', '#9E66AB', '#CD7058', '#D77FB3']

# Guardar fecha actual, con minutos a 0, para mostrar en el gráfico (HH:00)
if hora_actual.minute > 0:
    hora_actual = hora_actual + timedelta(hours=1)
    hora_actual = hora_actual.replace(minute=0)

df_all = pd.DataFrame(columns=['hora', 'dispositivos'])

for c in db.list_collection_names():
    if 'lth_/imsi_sensor/' in c and db[c].find({}).count() != 0:
        df = df.iloc[0:0]
        # Consultar número de dispositivos capturados cada hora en las últimas 8 horas
        for i in reversed(range(1,9)):
            cursor = db[c].find({
                'observation_time': {
                    '$gt': getFechaHora(i), 
                    '$lt': getFechaHora(i-1)
                }
            }, {'entityId': True, '_id': False}).distinct('entityId')
            df = df.append({
                'hora': getHora(i) + ' - ' + getHora(i-1), 
                'dispositivos': len(cursor)
            }, ignore_index=True)            
        df_all = df_all.append(df, sort=False)
        
        obtenerGrafico(df, c.split("/")[-1])

# TODOS LOS SENSORES
df_all = df_all.groupby('hora', sort=False)['dispositivos'].sum().to_frame().reset_index()
obtenerGrafico(df_all, None)