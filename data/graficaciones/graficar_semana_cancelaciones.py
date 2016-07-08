#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from math import log
import os

def readFile(File, data_1, data_2, cancelation_code):

  vuelosPorSemana = [0 for i in range(0, 48)]

  with open(File, 'r') as file_:
    for line in file_:
      currentline = line.split(",")
      dia = int(currentline[2])
      mes = int(currentline[1]) - 1

      if (1 <= dia <= 7):
        semana = 0
      elif (8 <= dia <= 15):
        semana = 1
      elif (16 <= dia <= 23):
        semana = 2
      elif (24 <= dia <= 31):
        semana = 3

      if (currentline[21] != 'NA'):
        vuelosPorSemana[semana+mes*4] += 1 # Cuento la cantidad de datos por mes

      if (currentline[21] == '1'):
        data_1[semana+mes*4] += 1 # Cuento la cantidad de datos por mes

      if currentline[22] == cancelation_code:
        data_2[semana+mes*4] += 1  # Sumo todos los datos del mes

  for i in range(0, 48):
    if data_1[i] != 0:
      data_2[i] /= float(data_1[i])

  for i in range(0, 48):
    if vuelosPorSemana[i] != 0:
      data_1[i] /= float(vuelosPorSemana[i])

def graficarSemanaCancelaciones(directory, airport, cancelation_code):

# Instancio los arreglos para los datos

  cancelaciones_1998 = [0 for i in range(0,48)]
  cancelaciones_filtro_1998 = [0 for i in range(0,48)]

  cancelaciones_1999 = [0 for i in range(0,48)]
  cancelaciones_filtro_1999 = [0 for i in range(0,48)]

  cancelaciones_2000 = [0 for i in range(0,48)]
  cancelaciones_filtro_2000 = [0 for i in range(0,48)]

  cancelaciones_2001 = [0 for i in range(0,48)]
  cancelaciones_filtro_2001 = [0 for i in range(0,48)]

  cancelaciones_2002 = [0 for i in range(0,48)]
  cancelaciones_filtro_2002 = [0 for i in range(0,48)]

  cancelaciones_2003 = [0 for i in range(0,48)]
  cancelaciones_filtro_2003 = [0 for i in range(0,48)]

  cancelaciones_2004 = [0 for i in range(0,48)]
  cancelaciones_filtro_2004 = [0 for i in range(0,48)]

  cancelaciones_2005 = [0 for i in range(0,48)]
  cancelaciones_filtro_2005 = [0 for i in range(0,48)]

  cancelaciones_2006 = [0 for i in range(0,48)]
  cancelaciones_filtro_2006 = [0 for i in range(0,48)]

  cancelaciones_2007 = [0 for i in range(0,48)]
  cancelaciones_filtro_2007 = [0 for i in range(0,48)]

  cancelaciones_2008 = [0 for i in range(0,48)]
  cancelaciones_filtro_2008 = [0 for i in range(0,48)]

  file_out = directory + '/' + airport

  readFile(file_out + '1998.csv', cancelaciones_1998, cancelaciones_filtro_1998, cancelation_code)
  readFile(file_out + '1999.csv', cancelaciones_1999, cancelaciones_filtro_1999, cancelation_code)
  readFile(file_out + '2000.csv', cancelaciones_2000, cancelaciones_filtro_2000, cancelation_code)
  readFile(file_out + '2001.csv', cancelaciones_2001, cancelaciones_filtro_2001, cancelation_code)
  readFile(file_out + '2002.csv', cancelaciones_2002, cancelaciones_filtro_2002, cancelation_code)
  readFile(file_out + '2003.csv', cancelaciones_2003, cancelaciones_filtro_2003, cancelation_code)
  readFile(file_out + '2004.csv', cancelaciones_2004, cancelaciones_filtro_2004, cancelation_code)
  readFile(file_out + '2005.csv', cancelaciones_2005, cancelaciones_filtro_2005, cancelation_code)
  readFile(file_out + '2006.csv', cancelaciones_2006, cancelaciones_filtro_2006, cancelation_code)
  readFile(file_out + '2007.csv', cancelaciones_2007, cancelaciones_filtro_2007, cancelation_code)
  readFile(file_out + '2008.csv', cancelaciones_2008, cancelaciones_filtro_2008, cancelation_code)

  #years = 11
  years = 5
  x = []
  y = []

  len_x = years * 12 * 2

  for i in range (1,len_x+1):
    x.append(i)

  len_y = (years) * 12 * 2

  for i in range (1,len_y+1):
    y.append(i)

  cancelaciones = cancelaciones_2004 + cancelaciones_2005 + cancelaciones_2006 + cancelaciones_2007 + cancelaciones_2008
  cancelaciones_filtro = cancelaciones_filtro_2004 + cancelaciones_filtro_2005 + cancelaciones_filtro_2006 + cancelaciones_filtro_2007 + cancelaciones_filtro_2008

  canc = [(cancelaciones[2*i] + cancelaciones[2*i+1]) / 2.0 for i in range(0, len(cancelaciones)/2)]
  canc_filtro = [(cancelaciones_filtro[2*i] + cancelaciones_filtro[2*i+1]) / 2.0 for i in range(0, len(cancelaciones_filtro)/2)]

  if not os.path.exists(directory + '/graficos'):
    os.mkdir(directory + '/graficos')

  opacity = 0.4

# Debería haber cantidad de años-1 
  for i in range(1, years):
    plt.axvline(x=12*2*i, linewidth=2, color='k')

  plt.plot(x, canc, 'ro', 
           alpha=opacity,
           linestyle='-',
           color='b',
           label=u"Cancelaciones por quincena")

  plt.xlabel(u"Quincenas")
  plt.ylabel(u"Cantidad de cancelaciones")
  plt.xticks([12+12*i*2 for i in range(0,5)],['2004', '2005', '2006', '2007', '2008'],fontsize=10)
  plt.legend()
  plt.savefig(directory + '/graficos/grafico_cancelaciones_quincena')
  plt.show()

  if cancelation_code != '':
    lab = ''
    fig = ''
    if cancelation_code == 'A':
      lab = "Cancelaciones de carrier por quincena"
      fig = directory + '/graficos/grafico_cancelaciones_carrier_quincena'

    if cancelation_code == 'B':
      lab = "Cancelaciones de clima por quincena"
      fig = directory + '/graficos/grafico_cancelaciones_clima_quincena'

    if cancelation_code == 'C':
      lab = "Cancelaciones de NAS por quincena"
      fig = directory + '/graficos/grafico_cancelaciones_NAS_quincena'

    if cancelation_code == 'D':
      lab = "Cancelaciones de seguridad por quincena"
      fig = directory + '/graficos/grafico_cancelaciones_seguridad_quincena'

    for i in range(1, years):
      plt.axvline(x=12*2*i, linewidth=2, color='k')

    plt.plot(y, canc_filtro, 'ro', 
             alpha=opacity,
             linestyle='-',
             color='b',
             label=lab)

    plt.xlabel(u"Quincenas")
    plt.ylabel(u"Cantidad de cancelaciones")
    plt.xticks([12+12*i*2 for i in range(0,5)],['2004', '2005', '2006', '2007', '2008'],fontsize=10)
    plt.legend()
    plt.savefig(fig)
    plt.show()


if __name__ == "__main__":
  main()
