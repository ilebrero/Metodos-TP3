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

      if (currentline[15] != 'NA'):
        vuelosPorMes[mes] += 1 

      if (currentline[21] == '1'):

        data_1[mes] += 1 # Cuento la cantidad de datos por mes

      if (currentline[22] == 'D'):

        data_2[mes] += 1
      
  for i in range(0, 12):
    if data_1[i] != 0:
      data_2[i] /= float(data_1[i])

  for i in range(0, 12):
    if vuelosPorMes[i] != 0:
      data_1[i] /= float(vuelosPorMes[i])


def main():

# Instancio los arreglos para los datos

  cancelaciones_1998 = [0 for i in range(0,12)]
  cancelaciones_seguridad_1998 = [0 for i in range(0,12)]

  cancelaciones_1999 = [0 for i in range(0,12)]
  cancelaciones_seguridad_1999 = [0 for i in range(0,12)]

  cancelaciones_2000 = [0 for i in range(0,12)]
  cancelaciones_seguridad_2000 = [0 for i in range(0,12)]

  cancelaciones_2001 = [0 for i in range(0,12)]
  cancelaciones_seguridad_2001 = [0 for i in range(0,12)]

  cancelaciones_2002 = [0 for i in range(0,12)]
  cancelaciones_seguridad_2002 = [0 for i in range(0,12)]

  cancelaciones_2003 = [0 for i in range(0,12)]
  cancelaciones_seguridad_2003 = [0 for i in range(0,12)]

  cancelaciones_2004 = [0 for i in range(0,12)]
  cancelaciones_seguridad_2004 = [0 for i in range(0,12)]

  cancelaciones_2005 = [0 for i in range(0,12)]
  cancelaciones_seguridad_2005 = [0 for i in range(0,12)]

  cancelaciones_2006 = [0 for i in range(0,12)]
  cancelaciones_seguridad_2006 = [0 for i in range(0,12)]

  cancelaciones_2007 = [0 for i in range(0,12)]
  cancelaciones_seguridad_2007 = [0 for i in range(0,12)]

  cancelaciones_2008 = [0 for i in range(0,12)]
  cancelaciones_seguridad_2008 = [0 for i in range(0,12)]


  readFile('ATL1998.csv', cancelaciones_1998, cancelaciones_seguridad_1998)
  readFile('ATL1999.csv', cancelaciones_1999, cancelaciones_seguridad_1999)
  readFile('ATL2000.csv', cancelaciones_2000, cancelaciones_seguridad_2000)
  readFile('ATL2001.csv', cancelaciones_2001, cancelaciones_seguridad_2001)
  readFile('ATL2002.csv', cancelaciones_2002, cancelaciones_seguridad_2002)
  readFile('ATL2003.csv', cancelaciones_2003, cancelaciones_seguridad_2003)
  readFile('ATL2004.csv', cancelaciones_2004, cancelaciones_seguridad_2004)
  readFile('ATL2005.csv', cancelaciones_2005, cancelaciones_seguridad_2005)
  readFile('ATL2006.csv', cancelaciones_2006, cancelaciones_seguridad_2006)
  readFile('ATL2007.csv', cancelaciones_2007, cancelaciones_seguridad_2007)
  readFile('ATL2008.csv', cancelaciones_2008, cancelaciones_seguridad_2008)

  datos = []

  years = 11
  x = []

  for i in range(0, years):
      for j in range(1, 13):
          x.append(j+12*i)

  cancelaciones = cancelaciones_1998 + cancelaciones_1999 + cancelaciones_2000 + cancelaciones_2001 + cancelaciones_2002 + cancelaciones_2003 + cancelaciones_2004 + cancelaciones_2005 + cancelaciones_2006 + cancelaciones_2007 + cancelaciones_2008
  cancelaciones_seguridad = cancelaciones_seguridad_1998 + cancelaciones_seguridad_1999 + cancelaciones_seguridad_2000 + cancelaciones_seguridad_2001 + cancelaciones_seguridad_2002 + cancelaciones_seguridad_2003 + cancelaciones_seguridad_2004 + cancelaciones_seguridad_2005 + cancelaciones_seguridad_2006 + cancelaciones_seguridad_2007 + cancelaciones_seguridad_2008
  print len(x)
  print len(datos)

# x_iteracion es para gráficar, por cada iteración de la variable siendo modificada, cada iteración del K-cross-folding
# Por eso se calcula como cant_iteraciones * K


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
  plt.savefig('./graficos/grafico_cancelaciones_mes')
  plt.show()

  for i in range(1, years):
    plt.axvline(x=12*i, linewidth=2, color='k')

  plt.plot(x, cancelaciones_seguridad, 'ro', 
           alpha=opacity,
           linestyle='-',
           color='b',
           label=u"Cancelaciones de seguridad por mes")

  plt.xlabel(u"Mes")
  plt.ylabel(u"Cancelaciones")
  plt.xticks([6+12*i for i in range(0,11)],['1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008'],fontsize=10)
  plt.legend()
  plt.savefig('./graficos/grafico_cancelaciones_seguridad_mes')
  plt.show()

if __name__ == "__main__":
  main()
