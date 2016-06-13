#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from math import log

def readFile(File, data_1, data_2):

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

      if (currentline[15] != 'NA'):
        vuelosPorSemana[semana+mes*4] += 1 # Cuento la cantidad de datos por mes

      if (currentline[15] != 'NA' and int(currentline[15]) > 15):
        dep_delay = int(currentline[15])

        data_1[semana+mes*4] += 1 # Cuento la cantidad de datos por mes
        data_2[semana+mes*4] += dep_delay  # Sumo todos los datos del mes

  for i in range(0, 48):
    if data_1[i] != 0:
      data_2[i] /= float(data_1[i])

  for i in range(0, 48):
    if vuelosPorSemana[i] != 0:
      data_1[i] /= float(vuelosPorSemana[i])

def main():

# Instancio los arreglos para los datos

  datos_semana_1998 = [0 for i in range(0, 48)]
  cant_datos_semana_1998 = [0 for i in range(0, 48)]

  datos_semana_1999 = [0 for i in range(0, 48)]
  cant_datos_semana_1999 = [0 for i in range(0, 48)]

  datos_semana_2000 = [0 for i in range(0, 48)]
  cant_datos_semana_2000 = [0 for i in range(0, 48)]

  datos_semana_2001 = [0 for i in range(0, 48)]
  cant_datos_semana_2001 = [0 for i in range(0, 48)]

  datos_semana_2002 = [0 for i in range(0, 48)]
  cant_datos_semana_2002 = [0 for i in range(0, 48)]

  datos_semana_2003 = [0 for i in range(0, 48)]
  cant_datos_semana_2003 = [0 for i in range(0, 48)]

  datos_semana_2004 = [0 for i in range(0, 48)]
  cant_datos_semana_2004 = [0 for i in range(0, 48)]

  datos_semana_2005 = [0 for i in range(0, 48)]
  cant_datos_semana_2005 = [0 for i in range(0, 48)]

  datos_semana_2006 = [0 for i in range(0, 48)]
  cant_datos_semana_2006 = [0 for i in range(0, 48)]

  datos_semana_2007 = [0 for i in range(0, 48)]
  cant_datos_semana_2007 = [0 for i in range(0, 48)]

  datos_semana_2008 = [0 for i in range(0, 48)]
  cant_datos_semana_2008 = [0 for i in range(0, 48)]

  readFile('BOS1998dest.csv', cant_datos_semana_1998, datos_semana_1998)
  readFile('BOS1999dest.csv', cant_datos_semana_1999, datos_semana_1999)
  readFile('BOS2000dest.csv', cant_datos_semana_2000, datos_semana_2000)
  readFile('BOS2001dest.csv', cant_datos_semana_2001, datos_semana_2001)
  readFile('BOS2002dest.csv', cant_datos_semana_2002, datos_semana_2002)
  readFile('BOS2003dest.csv', cant_datos_semana_2003, datos_semana_2003)
  readFile('BOS2004dest.csv', cant_datos_semana_2004, datos_semana_2004)
  readFile('BOS2005dest.csv', cant_datos_semana_2005, datos_semana_2005)
  readFile('BOS2006dest.csv', cant_datos_semana_2006, datos_semana_2006)
  readFile('BOS2007dest.csv', cant_datos_semana_2007, datos_semana_2007)
  readFile('BOS2008dest.csv', cant_datos_semana_2008, datos_semana_2008)

  datos = []

  years = 11
  x = []

  length = years * 12 * 4

  for i in range(1, length+1):
    x.append(i)

  cant_datos = cant_datos_semana_1998 + cant_datos_semana_1999 + cant_datos_semana_2000 + cant_datos_semana_2001 + cant_datos_semana_2002 + cant_datos_semana_2003 + cant_datos_semana_2004 + cant_datos_semana_2005 + cant_datos_semana_2006 + cant_datos_semana_2007 + cant_datos_semana_2008
  datos = datos_semana_1998 + datos_semana_1999 + datos_semana_2000 + datos_semana_2001 + datos_semana_2002 + datos_semana_2003 + datos_semana_2004 + datos_semana_2005 + datos_semana_2006 + datos_semana_2007 + datos_semana_2008

# x_iteracion es para gráficar, por cada iteración de la variable siendo modificada, cada iteración del K-cross-folding
# Por eso se calcula como cant_iteraciones * K


  opacity = 0.4

# Debería haber cantidad de años-1 
  for i in range(1, years):
    plt.axvline(x=12*4*i, linewidth=2, color='k')

  plt.plot(x, cant_datos, 'ro', 
           alpha=opacity,
           linestyle='-',
           color='b',
           label=u"Cantidad de delay por semana")

  plt.xlabel(u"Semanas")
  plt.ylabel(u"Cantidad de delays")
  plt.xticks([24+12*i*4 for i in range(0,11)],['1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008'],fontsize=10)
  plt.legend()
  plt.savefig('./graficos/grafico_cantidad_delay_semana')
  plt.show()

  for i in range(1, years):
    plt.axvline(x=12*4*i, linewidth=2, color='k')

  plt.plot(x, datos, 'ro', 
           alpha=opacity,
           linestyle='-',
           color='b',
           label=u"Delay por semana")

  plt.xlabel(u"Semanas")
  plt.ylabel(u"Delays")
  plt.xticks([24+12*i*4 for i in range(0,11)],['1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008'],fontsize=10)
  plt.legend()
  plt.savefig('./graficos/grafico_delay_semana')
  plt.show()


if __name__ == "__main__":
  main()
