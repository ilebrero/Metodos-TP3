#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from math import log
import os

def readFile(File, data_1, data_2, cancelation_code):

  vuelosTotales = 0

  with open(File, 'r') as file_:
    for line in file_:
      currentline = line.split(",")
      mes = int(currentline[1]) - 1

      vuelosTotales += 1 

      data_1[mes] += 1 # Cuento la cantidad de datos por mes

  #for i in range(0, 12):
  #  data_1[i] /= float(vuelosTotales)


def graficarMesVuelos(directory, airport, cancelation_code):

# Instancio los arreglos para los datos

  cancelaciones_1998 = [0 for i in range(0,12)]
  cancelaciones_filtro_1998 = [0 for i in range(0,12)]

  cancelaciones_1999 = [0 for i in range(0,12)]
  cancelaciones_filtro_1999 = [0 for i in range(0,12)]

  cancelaciones_2000 = [0 for i in range(0,12)]
  cancelaciones_filtro_2000 = [0 for i in range(0,12)]

  cancelaciones_2001 = [0 for i in range(0,12)]
  cancelaciones_filtro_2001 = [0 for i in range(0,12)]

  cancelaciones_2002 = [0 for i in range(0,12)]
  cancelaciones_filtro_2002 = [0 for i in range(0,12)]

  cancelaciones_2003 = [0 for i in range(0,12)]
  cancelaciones_filtro_2003 = [0 for i in range(0,12)]

  cancelaciones_2004 = [0 for i in range(0,12)]
  cancelaciones_filtro_2004 = [0 for i in range(0,12)]

  cancelaciones_2005 = [0 for i in range(0,12)]
  cancelaciones_filtro_2005 = [0 for i in range(0,12)]

  cancelaciones_2006 = [0 for i in range(0,12)]
  cancelaciones_filtro_2006 = [0 for i in range(0,12)]

  cancelaciones_2007 = [0 for i in range(0,12)]
  cancelaciones_filtro_2007 = [0 for i in range(0,12)]

  cancelaciones_2008 = [0 for i in range(0,12)]
  cancelaciones_filtro_2008 = [0 for i in range(0,12)]

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

  years = 11
  x = []
  y = []

  for i in range(0, years):
    for j in range(1, 13):
      x.append(j+12*i)

      if i < years-3:
        y.append(j+12*i)

  cancelaciones = cancelaciones_1998 + cancelaciones_1999 + cancelaciones_2000 + cancelaciones_2001 + cancelaciones_2002 + cancelaciones_2003 + cancelaciones_2004 + cancelaciones_2005 + cancelaciones_2006 + cancelaciones_2007 + cancelaciones_2008

  if not os.path.exists(directory + '/graficos'):
    os.mkdir(directory + '/graficos')

  opacity = 0.4

# Debería haber cantidad de años-1 
  for i in range(1, years):
    plt.axvline(x=12*i, linewidth=2, color='k')

  plt.plot(x, cancelaciones, 'ro', 
           alpha=opacity,
           linestyle='-',
           color='b',
           label=u"Cancelaciones por mes")

  plt.xlabel(u"Meses")
  plt.ylabel(u"Cancelaciones")
  plt.xticks([6+12*i for i in range(0,11)],['1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008'],fontsize=10)
  plt.legend()
  plt.savefig(directory + '/graficos/grafico_cancelaciones_mes')
  plt.show()

if __name__ == "__main__":
  main()
