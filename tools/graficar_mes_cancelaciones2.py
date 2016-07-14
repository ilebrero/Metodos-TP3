#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from math import log
import os

def readFile(File, data_1, data_2, cancelation_code):

  vuelosPorMes = [0 for i in range(0, 12)]

  with open(File, 'r') as file_:
    for line in file_:
      currentline = line.split(",")
      mes = int(currentline[1]) - 1

      if (currentline[21] != 'NA'):
        vuelosPorMes[mes] += 1 

      if (currentline[21] == '1'):

        data_1[mes] += 1 # Cuento la cantidad de datos por mes

      if (currentline[22] == cancelation_code):

        data_2[mes] += 1
      
  for i in range(0, 12):
    if data_1[i] != 0:
      data_2[i] /= float(data_1[i])

  for i in range(0, 12):
    if vuelosPorMes[i] != 0:
      data_1[i] /= float(vuelosPorMes[i])


def graficarMesCancelaciones(directory_1, directory_2, airport_1, airport_2, cancelation_code):

# Instancio los arreglos para los datos

  cancelaciones1_1998 = [0 for i in range(0,12)]
  cancelaciones1_filtro_1998 = [0 for i in range(0,12)]

  cancelaciones1_1999 = [0 for i in range(0,12)]
  cancelaciones1_filtro_1999 = [0 for i in range(0,12)]

  cancelaciones1_2000 = [0 for i in range(0,12)]
  cancelaciones1_filtro_2000 = [0 for i in range(0,12)]

  cancelaciones1_2001 = [0 for i in range(0,12)]
  cancelaciones1_filtro_2001 = [0 for i in range(0,12)]

  cancelaciones1_2002 = [0 for i in range(0,12)]
  cancelaciones1_filtro_2002 = [0 for i in range(0,12)]

  cancelaciones1_2003 = [0 for i in range(0,12)]
  cancelaciones1_filtro_2003 = [0 for i in range(0,12)]

  cancelaciones1_2004 = [0 for i in range(0,12)]
  cancelaciones1_filtro_2004 = [0 for i in range(0,12)]

  cancelaciones1_2005 = [0 for i in range(0,12)]
  cancelaciones1_filtro_2005 = [0 for i in range(0,12)]

  cancelaciones1_2006 = [0 for i in range(0,12)]
  cancelaciones1_filtro_2006 = [0 for i in range(0,12)]

  cancelaciones1_2007 = [0 for i in range(0,12)]
  cancelaciones1_filtro_2007 = [0 for i in range(0,12)]

  cancelaciones1_2008 = [0 for i in range(0,12)]
  cancelaciones1_filtro_2008 = [0 for i in range(0,12)]

  file_out_1 = directory_1 + '/' + airport

  readFile(file_out_1 + '1998.csv', cancelaciones_1998, cancelaciones_filtro_1998, cancelation_code)
  readFile(file_out_1 + '1999.csv', cancelaciones_1999, cancelaciones_filtro_1999, cancelation_code)
  readFile(file_out_1 + '2000.csv', cancelaciones_2000, cancelaciones_filtro_2000, cancelation_code)
  readFile(file_out_1 + '2001.csv', cancelaciones_2001, cancelaciones_filtro_2001, cancelation_code)
  readFile(file_out_1 + '2002.csv', cancelaciones_2002, cancelaciones_filtro_2002, cancelation_code)
  readFile(file_out_1 + '2003.csv', cancelaciones_2003, cancelaciones_filtro_2003, cancelation_code)
  readFile(file_out_1 + '2004.csv', cancelaciones_2004, cancelaciones_filtro_2004, cancelation_code)
  readFile(file_out_1 + '2005.csv', cancelaciones_2005, cancelaciones_filtro_2005, cancelation_code)
  readFile(file_out_1 + '2006.csv', cancelaciones_2006, cancelaciones_filtro_2006, cancelation_code)
  readFile(file_out_1 + '2007.csv', cancelaciones_2007, cancelaciones_filtro_2007, cancelation_code)
  readFile(file_out_1 + '2008.csv', cancelaciones_2008, cancelaciones_filtro_2008, cancelation_code)

  years_1 = 11
  x_1 = []
  y_1 = []

  for i in range(0, years):
    for j in range(1, 13):
      x_1.append(j+12*i)

      if i < years-3:
        y_1.append(j+12*i)

  cancelaciones1 = cancelaciones1_1998 + cancelaciones1_1999 + cancelaciones1_2000 + cancelaciones1_2001 + cancelaciones1_2002 + cancelaciones1_2003 + cancelaciones1_2004 + cancelaciones1_2005 + cancelaciones1_2006 + cancelaciones1_2007 + cancelaciones1_2008
  cancelaciones1_filtro = cancelaciones1_filtro_2001 + cancelaciones1_filtro_2002 + cancelaciones1_filtro_2003 + cancelaciones1_filtro_2004 + cancelaciones1_filtro_2005 + cancelaciones1_filtro_2006 + cancelaciones1_filtro_2007 + cancelaciones1_filtro_2008


  cancelaciones2_1998 = [0 for i in range(0,12)]
  cancelaciones2_filtro_1998 = [0 for i in range(0,12)]

  cancelaciones2_1999 = [0 for i in range(0,12)]
  cancelaciones2_filtro_1999 = [0 for i in range(0,12)]

  cancelaciones2_2000 = [0 for i in range(0,12)]
  cancelaciones2_filtro_2000 = [0 for i in range(0,12)]

  cancelaciones2_2001 = [0 for i in range(0,12)]
  cancelaciones2_filtro_2001 = [0 for i in range(0,12)]

  cancelaciones2_2002 = [0 for i in range(0,12)]
  cancelaciones2_filtro_2002 = [0 for i in range(0,12)]

  cancelaciones2_2003 = [0 for i in range(0,12)]
  cancelaciones2_filtro_2003 = [0 for i in range(0,12)]

  cancelaciones2_2004 = [0 for i in range(0,12)]
  cancelaciones2_filtro_2004 = [0 for i in range(0,12)]

  cancelaciones2_2005 = [0 for i in range(0,12)]
  cancelaciones2_filtro_2005 = [0 for i in range(0,12)]

  cancelaciones2_2006 = [0 for i in range(0,12)]
  cancelaciones2_filtro_2006 = [0 for i in range(0,12)]

  cancelaciones2_2007 = [0 for i in range(0,12)]
  cancelaciones2_filtro_2007 = [0 for i in range(0,12)]

  cancelaciones2_2008 = [0 for i in range(0,12)]
  cancelaciones2_filtro_2008 = [0 for i in range(0,12)]

  file_out_2 = directory_2 + '/' + airport

  readFile(file_out_2 + '1998.csv', cancelaciones2_1998, cancelaciones2_filtro_1998, cancelation_code)
  readFile(file_out_2 + '1999.csv', cancelaciones2_1999, cancelaciones2_filtro_1999, cancelation_code)
  readFile(file_out_2 + '2000.csv', cancelaciones2_2000, cancelaciones2_filtro_2000, cancelation_code)
  readFile(file_out_2 + '2001.csv', cancelaciones2_2001, cancelaciones2_filtro_2001, cancelation_code)
  readFile(file_out_2 + '2002.csv', cancelaciones2_2002, cancelaciones2_filtro_2002, cancelation_code)
  readFile(file_out_2 + '2003.csv', cancelaciones2_2003, cancelaciones2_filtro_2003, cancelation_code)
  readFile(file_out_2 + '2004.csv', cancelaciones2_2004, cancelaciones2_filtro_2004, cancelation_code)
  readFile(file_out_2 + '2005.csv', cancelaciones2_2005, cancelaciones2_filtro_2005, cancelation_code)
  readFile(file_out_2 + '2006.csv', cancelaciones2_2006, cancelaciones2_filtro_2006, cancelation_code)
  readFile(file_out_2 + '2007.csv', cancelaciones2_2007, cancelaciones2_filtro_2007, cancelation_code)
  readFile(file_out_2 + '2008.csv', cancelaciones2_2008, cancelaciones2_filtro_2008, cancelation_code)

  years = 11
  x_2 = []
  y_2 = []

  for i in range(0, years):
    for j in range(1, 13):
      x_2.append(j+12*i)

      if i < years-3:
        y_2.append(j+12*i)


  cancelaciones2 = cancelaciones2_1998 + cancelaciones2_1999 + cancelaciones2_2000 + cancelaciones2_2001 + cancelaciones2_2002 + cancelaciones2_2003 + cancelaciones2_2004 + cancelaciones2_2005 + cancelaciones2_2006 + cancelaciones2_2007 + cancelaciones2_2008
  cancelaciones2_filtro = cancelaciones2_filtro_2001 + cancelaciones2_filtro_2002 + cancelaciones2_filtro_2003 + cancelaciones2_filtro_2004 + cancelaciones2_filtro_2005 + cancelaciones2_filtro_2006 + cancelaciones2_filtro_2007 + cancelaciones2_filtro_2008

  if not os.path.exists(directory + '/graficos'):
    os.mkdir(directory + '/graficos')

  opacity = 0.4

# Debería haber cantidad de años-1 
  for i in range(1, years):
    plt.axvline(x=12*i, linewidth=2, color='k')

  plt.plot(x_1, cancelaciones1, 'ro', 
           alpha=opacity,
           linestyle='-',
           color='b',
           label=u"Cancelaciones por mes")

  plt.plot(x_2, cancelaciones2, 'ro', 
           alpha=opacity,
           linestyle='-',
           color='r',
           label=u"Cancelaciones por mes")

  plt.xlabel(u"Meses")
  plt.ylabel(u"Cancelaciones")
  plt.xticks([6+12*i for i in range(0,11)],['1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008'],fontsize=10)
  plt.legend()
  plt.savefig(directory + '/graficos/grafico_cancelaciones_mes')
  plt.show()

  if cancelation_code != '':
    lab = ''
    fig = ''
    if cancelation_code == 'A':
      lab = "Cancelaciones de carrier por mes"
      fig = directory + '/graficos/grafico_cancelaciones_carrier_mes'

    if cancelation_code == 'B':
      lab = "Cancelaciones de clima por mes"
      fig = directory + '/graficos/grafico_cancelaciones_clima_mes'

    if cancelation_code == 'C':
      lab = "Cancelaciones de NAS por mes"
      fig = directory + '/graficos/grafico_cancelaciones_NAS_mes'

    if cancelation_code == 'D':
      lab = "Cancelaciones de seguridad por mes"
      fig = directory + '/graficos/grafico_cancelaciones_seguridad_mes'

    for i in range(1, years-3):
      plt.axvline(x=12*i, linewidth=2, color='k')

    plt.plot(y_1, cancelaciones1_filtro, 'ro', 
             alpha=opacity,
             linestyle='-',
             color='b',
             label=lab)

    plt.plot(y_2, cancelaciones2_filtro, 'ro', 
             alpha=opacity,
             linestyle='-',
             color='r',
             label=lab)

    plt.xlabel(u"Mes")
    plt.ylabel(u"Cancelaciones")
    plt.xticks([6+12*i for i in range(0,8)],['2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008'],fontsize=10)
    plt.legend()
    plt.savefig(fig)
    plt.show()

if __name__ == "__main__":
  main()
