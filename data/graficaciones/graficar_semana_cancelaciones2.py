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

def graficarSemanaCancelaciones2(directory_1, directory_2, airport_1, airport_2, cancelation_code):

# Instancio los arreglos para los datos

  cancelaciones1_1998 = [0 for i in range(0,48)]
  cancelaciones1_filtro_1998 = [0 for i in range(0,48)]

  cancelaciones1_1999 = [0 for i in range(0,48)]
  cancelaciones1_filtro_1999 = [0 for i in range(0,48)]

  cancelaciones1_2000 = [0 for i in range(0,48)]
  cancelaciones1_filtro_2000 = [0 for i in range(0,48)]

  cancelaciones1_2001 = [0 for i in range(0,48)]
  cancelaciones1_filtro_2001 = [0 for i in range(0,48)]

  cancelaciones1_2002 = [0 for i in range(0,48)]
  cancelaciones1_filtro_2002 = [0 for i in range(0,48)]

  cancelaciones1_2003 = [0 for i in range(0,48)]
  cancelaciones1_filtro_2003 = [0 for i in range(0,48)]

  cancelaciones1_2004 = [0 for i in range(0,48)]
  cancelaciones1_filtro_2004 = [0 for i in range(0,48)]

  cancelaciones1_2005 = [0 for i in range(0,48)]
  cancelaciones1_filtro_2005 = [0 for i in range(0,48)]

  cancelaciones1_2006 = [0 for i in range(0,48)]
  cancelaciones1_filtro_2006 = [0 for i in range(0,48)]

  cancelaciones1_2007 = [0 for i in range(0,48)]
  cancelaciones1_filtro_2007 = [0 for i in range(0,48)]

  cancelaciones1_2008 = [0 for i in range(0,48)]
  cancelaciones1_filtro_2008 = [0 for i in range(0,48)]

  file_out1 = directory_1 + '/' + airport_1

  readFile(file_out1 + '1998.csv', cancelaciones1_1998, cancelaciones1_filtro_1998, cancelation_code)
  readFile(file_out1 + '1999.csv', cancelaciones1_1999, cancelaciones1_filtro_1999, cancelation_code)
  readFile(file_out1 + '2000.csv', cancelaciones1_2000, cancelaciones1_filtro_2000, cancelation_code)
  readFile(file_out1 + '2001.csv', cancelaciones1_2001, cancelaciones1_filtro_2001, cancelation_code)
  readFile(file_out1 + '2002.csv', cancelaciones1_2002, cancelaciones1_filtro_2002, cancelation_code)
  readFile(file_out1 + '2003.csv', cancelaciones1_2003, cancelaciones1_filtro_2003, cancelation_code)
  readFile(file_out1 + '2004.csv', cancelaciones1_2004, cancelaciones1_filtro_2004, cancelation_code)
  readFile(file_out1 + '2005.csv', cancelaciones1_2005, cancelaciones1_filtro_2005, cancelation_code)
  readFile(file_out1 + '2006.csv', cancelaciones1_2006, cancelaciones1_filtro_2006, cancelation_code)
  readFile(file_out1 + '2007.csv', cancelaciones1_2007, cancelaciones1_filtro_2007, cancelation_code)
  readFile(file_out1 + '2008.csv', cancelaciones1_2008, cancelaciones1_filtro_2008, cancelation_code)

  years = 11
  x_1 = []
  y_1 = []

  len_x = years * 12 * 4

  for i in range (1,len_x+1):
    x_1.append(i*2)

  len_y = (years-3) * 12 * 4

  for i in range (1,len_y+1):
    y_1.append(i*2)

  cancelaciones1 = cancelaciones1_1998 + cancelaciones1_1999 + cancelaciones1_2000 + cancelaciones1_2001 + cancelaciones1_2002 + cancelaciones1_2003 + cancelaciones1_2004 + cancelaciones1_2005 + cancelaciones1_2006 + cancelaciones1_2007 + cancelaciones1_2008
  cancelaciones1_filtro = cancelaciones1_filtro_2001 + cancelaciones1_filtro_2002 + cancelaciones1_filtro_2003 + cancelaciones1_filtro_2004 + cancelaciones1_filtro_2005 + cancelaciones1_filtro_2006 + cancelaciones1_filtro_2007 + cancelaciones1_filtro_2008


  if not os.path.exists(directory_1 + '/graficos'):
    os.mkdir(directory_1 + '/graficos')


  cancelaciones2_1998 = [0 for i in range(0,48)]
  cancelaciones2_filtro_1998 = [0 for i in range(0,48)]

  cancelaciones2_1999 = [0 for i in range(0,48)]
  cancelaciones2_filtro_1999 = [0 for i in range(0,48)]

  cancelaciones2_2000 = [0 for i in range(0,48)]
  cancelaciones2_filtro_2000 = [0 for i in range(0,48)]

  cancelaciones2_2001 = [0 for i in range(0,48)]
  cancelaciones2_filtro_2001 = [0 for i in range(0,48)]

  cancelaciones2_2002 = [0 for i in range(0,48)]
  cancelaciones2_filtro_2002 = [0 for i in range(0,48)]

  cancelaciones2_2003 = [0 for i in range(0,48)]
  cancelaciones2_filtro_2003 = [0 for i in range(0,48)]

  cancelaciones2_2004 = [0 for i in range(0,48)]
  cancelaciones2_filtro_2004 = [0 for i in range(0,48)]

  cancelaciones2_2005 = [0 for i in range(0,48)]
  cancelaciones2_filtro_2005 = [0 for i in range(0,48)]

  cancelaciones2_2006 = [0 for i in range(0,48)]
  cancelaciones2_filtro_2006 = [0 for i in range(0,48)]

  cancelaciones2_2007 = [0 for i in range(0,48)]
  cancelaciones2_filtro_2007 = [0 for i in range(0,48)]

  cancelaciones2_2008 = [0 for i in range(0,48)]
  cancelaciones2_filtro_2008 = [0 for i in range(0,48)]

  file_out2 = directory_2 + '/' + airport_2

  readFile(file_out2 + '1998.csv', cancelaciones2_1998, cancelaciones2_filtro_1998, cancelation_code)
  readFile(file_out2 + '1999.csv', cancelaciones2_1999, cancelaciones2_filtro_1999, cancelation_code)
  readFile(file_out2 + '2000.csv', cancelaciones2_2000, cancelaciones2_filtro_2000, cancelation_code)
  readFile(file_out2 + '2001.csv', cancelaciones2_2001, cancelaciones2_filtro_2001, cancelation_code)
  readFile(file_out2 + '2002.csv', cancelaciones2_2002, cancelaciones2_filtro_2002, cancelation_code)
  readFile(file_out2 + '2003.csv', cancelaciones2_2003, cancelaciones2_filtro_2003, cancelation_code)
  readFile(file_out2 + '2004.csv', cancelaciones2_2004, cancelaciones2_filtro_2004, cancelation_code)
  readFile(file_out2 + '2005.csv', cancelaciones2_2005, cancelaciones2_filtro_2005, cancelation_code)
  readFile(file_out2 + '2006.csv', cancelaciones2_2006, cancelaciones2_filtro_2006, cancelation_code)
  readFile(file_out2 + '2007.csv', cancelaciones2_2007, cancelaciones2_filtro_2007, cancelation_code)
  readFile(file_out2 + '2008.csv', cancelaciones2_2008, cancelaciones2_filtro_2008, cancelation_code)

  x_2 = []
  y_2 = []

  len_x = years * 12 * 4

  for i in range (1,len_x+1):
    x_2.append(i*2)

  len_y = (years-3) * 12 * 4

  for i in range (1,len_y+1):
    y_2.append(i*2)

  cancelaciones2 = cancelaciones2_1998 + cancelaciones2_1999 + cancelaciones2_2000 + cancelaciones2_2001 + cancelaciones2_2002 + cancelaciones2_2003 + cancelaciones2_2004 + cancelaciones2_2005 + cancelaciones2_2006 + cancelaciones2_2007 + cancelaciones2_2008
  cancelaciones2_filtro = cancelaciones2_filtro_2001 + cancelaciones2_filtro_2002 + cancelaciones2_filtro_2003 + cancelaciones2_filtro_2004 + cancelaciones2_filtro_2005 + cancelaciones2_filtro_2006 + cancelaciones2_filtro_2007 + cancelaciones2_filtro_2008


  if not os.path.exists(directory_2 + '/graficos'):
    os.mkdir(directory_2 + '/graficos')


  opacity = 0.4

# Debería haber cantidad de años-1 
  for i in range(1, years):
    plt.axvline(x=12*4*i, linewidth=2, color='k')

  plt.plot(x_1, cancelaciones1, 'ro', 
           alpha=opacity,
           linestyle='-',
           color='b',
           label=u"Cancelaciones por semana " + airport_1)

  plt.plot(x_2, cancelaciones2, 'ro', 
           alpha=opacity,
           linestyle='-',
           color='r',
           label=u"Cancelaciones por semana " + airport_2)

  plt.xlabel(u"Semanas")
  plt.ylabel(u"Cantidad de cancelaciones")
  plt.xticks([24+12*i*4 for i in range(0,11)],['1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008'],fontsize=10)
  plt.legend()
  plt.savefig(directory_2 + '/graficos/grafico_cancelaciones1_semana')
  plt.show()

  if cancelation_code != '':
    lab = ''
    fig = ''
    if cancelation_code == 'A':
      lab = "Cancelaciones de carrier por semana"
      fig = directory_2 + '/graficos/grafico_cancelaciones1_carrier_semana'

    if cancelation_code == 'B':
      lab = "Cancelaciones de clima por semana"
      fig = directory_2 + '/graficos/grafico_cancelaciones1_clima_semana'

    if cancelation_code == 'C':
      lab = "Cancelaciones de NAS por semana"
      fig = directory_2 + '/graficos/grafico_cancelaciones1_NAS_semana'

    if cancelation_code == 'D':
      lab = "Cancelaciones de seguridad por semana"
      fig = directory_2 + '/graficos/grafico_cancelaciones1_seguridad_semana'

    for i in range(1, years-3):
      plt.axvline(x=12*4*i, linewidth=2, color='k')

    plt.plot(y_1, cancelaciones1_filtro, 'ro', 
             alpha=opacity,
             linestyle='-',
             color='b',
             label=lab)

    plt.plot(y_2, cancelaciones2_filtro, 'ro', 
             alpha=opacity,
             linestyle='-',
             color='b',
             label=lab)

    plt.xlabel(u"Semanas")
    plt.ylabel(u"Cantidad de cancelaciones")
    plt.xticks([24+12*i*4 for i in range(0,8)],['2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008'],fontsize=10)
    plt.legend()
    plt.savefig(fig)
    plt.show()


if __name__ == "__main__":
  main()
