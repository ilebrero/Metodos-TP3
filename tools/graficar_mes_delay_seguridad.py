#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from math import log


# Leo los archivos y genero los arreglos con todos los datos

def readFile(File, data_1, data_2):

  vuelosPorMes = [0 for i in range(0, 12)]

  with open(File, 'r') as file_:
    for line in file_:
      currentline = line.split(",")
      mes = int(currentline[1]) - 1

      if (currentline[27] != 'NA'):
        vuelosPorMes[mes] += 1 

      if (currentline[27] != 'NA' and int(currentline[27]) > 15):
        dep_delay = int(currentline[27])

        data_1[mes] += 1 # Cuento la cantidad de datos por mes
        data_2[mes] += dep_delay  # Sumo todos los datos del mes

  for i in range(0, 12):
    if data_1[i] != 0:
      data_2[i] /= float(data_1[i])

  for i in range(0, 12):
    if vuelosPorMes[i] != 0:
      data_1[i] /= float(vuelosPorMes[i])

def main():

# Instancio los arreglos para los datos

  datos_1998 = [0 for i in range(0, 12)]
  cant_datos_1998 = [0 for i in range(0,12)]

  datos_1999 = [0 for i in range(0, 12)]
  cant_datos_1999 = [0 for i in range(0,12)]

  datos_2000 = [0 for i in range(0, 12)]
  cant_datos_2000 = [0 for i in range(0,12)]

  datos_2001 = [0 for i in range(0, 12)]
  cant_datos_2001 = [0 for i in range(0,12)]

  datos_2002 = [0 for i in range(0, 12)]
  cant_datos_2002 = [0 for i in range(0,12)]

  datos_2003 = [0 for i in range(0, 12)]
  cant_datos_2003 = [0 for i in range(0,12)]

  datos_2004 = [0 for i in range(0, 12)]
  cant_datos_2004 = [0 for i in range(0,12)]

  datos_2005 = [0 for i in range(0, 12)]
  cant_datos_2005 = [0 for i in range(0,12)]

  datos_2006 = [0 for i in range(0, 12)]
  cant_datos_2006 = [0 for i in range(0,12)]

  datos_2007 = [0 for i in range(0, 12)]
  cant_datos_2007 = [0 for i in range(0,12)]

  datos_2008 = [0 for i in range(0, 12)]
  cant_datos_2008 = [0 for i in range(0,12)]

  readFile('ATL1998.csv', cant_datos_1998, datos_1998)
  readFile('ATL1999.csv', cant_datos_1999, datos_1999)
  readFile('ATL2000.csv', cant_datos_2000, datos_2000)
  readFile('ATL2001.csv', cant_datos_2001, datos_2001)
  readFile('ATL2002.csv', cant_datos_2002, datos_2002)
  readFile('ATL2003.csv', cant_datos_2003, datos_2003)
  readFile('ATL2004.csv', cant_datos_2004, datos_2004)
  readFile('ATL2005.csv', cant_datos_2005, datos_2005)
  readFile('ATL2006.csv', cant_datos_2006, datos_2006)
  readFile('ATL2007.csv', cant_datos_2007, datos_2007)
  readFile('ATL2008.csv', cant_datos_2008, datos_2008)

  datos = []

  years = 6
  x = []

  for i in range(0, years):
      for j in range(1, 13):
          x.append(j+12*i)

  cant_datos = cant_datos_2003 + cant_datos_2004 + cant_datos_2005 + cant_datos_2006 + cant_datos_2007 + cant_datos_2008
  datos = datos_2003 + datos_2004 + datos_2005 + datos_2006 + datos_2007 + datos_2008

  print len(x)
  print len(datos)

# x_iteracion es para gráficar, por cada iteración de la variable siendo modificada, cada iteración del K-cross-folding
# Por eso se calcula como cant_iteraciones * K


  opacity = 0.4

# Debería haber cantidad de años-1 
  for i in range(1, years):
    plt.axvline(x=12*i, linewidth=2, color='k')

  plt.plot(x, cant_datos, 'ro', 
           alpha=opacity,
           linestyle='-',
           color='b',
           label=u"Cantidad de delays de seguridad por mes")

  plt.xlabel(u"Meses")
  plt.ylabel(u"Cantidad de delays")
  plt.xticks([6+12*i for i in range(0,years)],['2003', '2004', '2005', '2006', '2007', '2008'],fontsize=10)
  plt.legend()
  plt.savefig('./graficos/grafico_mes_cantidad_delay_seguridad')
  plt.show()

  for i in range(1, years):
    plt.axvline(x=12*i, linewidth=2, color='k')

  plt.plot(x, datos, 'ro', 
           alpha=opacity,
           linestyle='-',
           color='b',
           label=u"Delays de seguridad por mes")

  plt.xlabel(u"Meses")
  plt.ylabel(u"Delays")
  plt.xticks([6+12*i for i in range(0,years)],['2003', '2004', '2005', '2006', '2007', '2008'],fontsize=10)
  plt.legend()
  plt.savefig('./graficos/grafico_mes_delay_seguridad')
  plt.show()

if __name__ == "__main__":
  main()
