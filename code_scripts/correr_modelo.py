import pandas as pd
import numpy as np
import plotly.express as px
from PIL import Image
import cv2
import matplotlib.pyplot as plt
import matplotlib.ticker
import os
import csv
from Class_procesar_imagenes import procesar_imagenes



image_files = >>>>> image_path
procesar_imagenes(image_path)


## Buscar donde los CSV's fueron creados e importarlos
df_o = pd.read_csv('histograms_horizontal_ojos.csv', header=None).drop_duplicates()
df_b = pd.read_csv('histograms_horizontal_boca.csv', header=None).drop_duplicates()
df_v = pd.read_csv('histograms_vertical.csv', header=None).drop_duplicates()

## graficar las integrales de Ojos, boca y vertical
for df_ in [df_o,df_b,df_v]:
  x_values = range(len(df_.columns))
  for i, (_, row) in enumerate(df_.iterrows()):
      plt.scatter(x_values, row, label=f'Row {i}')
  plt.xticks(x_values, df_.columns)
  plt.ylim(0, 255)
  plt.legend()
  plt.show()



## Esta toma como cara-humana a cualquiera que caiga dentro del rango de los puntos.
listas_histograms = list(procesar_imagenes.procesar_new_img("/content/Jubilado_1.jpg"))

histograms_names = ["Vertical", "Hist_ojos","Hist_boca"]
tiks_1 = []
tiks_false_1 = []

for df_,list_nuew_img in zip([df_v,df_o,df_b],listas_histograms):
  tiks = []
  tiks_false = []
  n = 0
  f = 0
  for i,col in zip(list_nuew_img,list(df_.columns)):
    if df_[col].min() <= i <= df_[col].max():
      n = n+1
      tiks.append(n)
    else:
      f = f+1
      tiks_false.append(f)
  tiks_1.append(tiks)
  tiks_false_1.append(tiks_false)

poisibilidades = []
for list_nuew_img,i,z in zip(listas_histograms,range(len(tiks_1)),histograms_names):
  posibilidad = len(tiks_1[i])/len(list_nuew_img)
  poisibilidades.append(posibilidad)
  print(posibilidad*100,"% ","según: ",z)





 ## Esta toma como cara-humana a cualquiera que caiga dentro del rango min max del average de los puntos de la zona.
listas_histograms = list(procesar_imagenes.procesar_new_img("/content/Jubilado_1.jpg"))

histograms_names = ["Vertical", "Hist_ojos","Hist_boca"]
tiks_1 = []
tiks_false_1 = []

for df_,list_nuew_img in zip([df_v,df_o,df_b],listas_histograms):
  tiks = []
  tiks_false = []
  n = 0
  f = 0
  for i,col in zip(list_nuew_img,list(df_.columns)):
    average = df_[col].mean()
    diff_max_min = (df_[col].max() - df_[col].min())/2
    average_top = average + diff_max_min
    average_bottom = average - diff_max_min
    if average_bottom <= i <= average_top:
      n = n+1
      tiks.append(n)
    else:
      f = f+1
      tiks_false.append(f)
  tiks_1.append(tiks)
  tiks_false_1.append(tiks_false)

poisibilidades = []
for list_nuew_img,i,z in zip(listas_histograms,range(len(tiks_1)),histograms_names):
  posibilidad = len(tiks_1[i])/len(list_nuew_img)
  poisibilidades.append(posibilidad)
  print(posibilidad*100,"% ","según: ",z)

print(sum(poisibilidades)/len(poisibilidades)*100, "% de probabilidades que sea una cara humana")