#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
from graficaciones.graficar_cuadrados_minimos import calcularCML
import matplotlib.pyplot as plt
from math import log
import os

def func(x, a, b, c, d, e, f, g, h, i):
  #return b*np.abs(np.sin(0.5*np.pi*x)) + c*np.abs(np.cos(x))
  #return b*np.abs(np.cos(x)) + c*np.abs(np.sin(x)) + d * x + e*np.cos(x)
  #return b*np.abs(np.cos(x)) + c*np.abs(np.sin(x)) + e*np.cos(x)
  #return np.abs(b*x*x*x + c*x*x + d*x + e)
  #return b*x*x + c*x + d + a*np.cos(x) + e*np.cos(2.0*x)
  #return b*x*x + c*x + d + a*np.abs(np.cos(x)) + e*np.abs(np.sin(x)) 
  #return b*x + c
  #return a*x*x + b*x + c
  #return a*x*x*x + b*x*x + c*x + d
  #return e*x*x*x*x + a*x*x*x + b*x*x + c*x + d
  #return a*np.abs(np.cos(x)) + b*np.abs(np.sin(x)) + c*x + d + e
  #return a*np.abs(np.cos(x)) + c*x + d + e + b
  #return a*np.abs(np.cos(x)) + c*np.abs(np.cos(2*x))+ b*np.exp(x) + d 
  #return a*x*x*(x-2)*(x-1)*x + b*x*(x-2)*(x-1)*x + c*(x-2)*(x-1)*x + d*(x-1)*x + e*x + f*np.cos(x) + g
  #return i*x*x*x*x*x*x*x*x + h*x*x*x*x*x*x*x + f*x*x*x*x*x*x + a*x*x*x*x*x + b*x*x*x*x + c*x*x*x + d*x*x + e*x + g + 300*np.cos(x) + np.sin(x)
  #return i*x*x*x*x*x*x*x*x + h*x*x*x*x*x*x*x + f*x*x*x*x*x*x + a*x*x*x*x*x + b*x*x*x*x + c*x*x*x + d*x*x + e*x + g + 300*np.cos(x) + 300*np.sin(x)
  #return a*np.abs(np.cos(15*x)) + b 
  return a*np.cos(x)*x*x*x + b*np.sin(2*x)*x*x +  d


def errorCuadraticoMedio(valsY, valsEstimacion):
  error = [valsY[i] - valsEstimacion[i] for i in range(0, len(valsY))]

  res = 0
  for num in error:
    res += num*num 

  res /= float(len(valsY))

  return res

def readFile(File, data_1, data_2, cancelation_code):

  vuelosTotales = 0

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

      vuelosTotales += 1 # Cuento la cantidad de datos por mes

      data_1[semana+mes*4] += 1 # Cuento la cantidad de datos por mes

  #for i in range(0, 48):
  #  data_1[i] /= float(vuelosTotales)

def graficarSemanaVuelos(directory, airport, cancelation_code):

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
  years = 11
  x = []
  y = []

  len_x = years * 12 * 2 *2

  for i in range (0,len_x):
    x.append(i)

  len_y = (years) * 12 * 2

  for i in range (1,len_y+1):
    y.append(i)

  cancelaciones = cancelaciones_1998 + cancelaciones_1999 + cancelaciones_2000 + cancelaciones_2001 + cancelaciones_2002 + cancelaciones_2003 + cancelaciones_2004 + cancelaciones_2005 + cancelaciones_2006 + cancelaciones_2007 + cancelaciones_2008
  cancelaciones_filtro = cancelaciones_filtro_1998 + cancelaciones_filtro_1999 + cancelaciones_filtro_2000 + cancelaciones_filtro_2001 + cancelaciones_filtro_2002 + cancelaciones_filtro_2003 + cancelaciones_filtro_2004 + cancelaciones_filtro_2005 + cancelaciones_filtro_2006 + cancelaciones_filtro_2007 + cancelaciones_filtro_2008

  if not os.path.exists(directory + '/graficos'):
    os.mkdir(directory + '/graficos')

  opacity = 0.4

# Debería haber cantidad de años-1 
  for i in range(1, years):
    plt.axvline(x=12*4*i, linewidth=2, color='k')
  
  print len(x)
  print len(cancelaciones)
  plt.plot(x, cancelaciones, 'ro', 
           alpha=opacity,
           linestyle='-',
           color='b',
           label=u"vuelos por semana")


  ################## CML EMPIEZA
  valsEstimacion = []
  inicio = 144
  fin = 240
  param = calcularCML(x[0 : inicio], cancelaciones[0 : inicio], func)
  for i in range(inicio, fin):
    valsEstimacion.append(func(i, param [0], param [1], param [2], param [3], param [4], param [5], param [6], param [7], param [8])) #, param [2])) #, param [3]))

  plt.plot(x[inicio : fin], valsEstimacion, 'ro', alpha=opacity, linestyle='-', color='#602312')

  error = errorCuadraticoMedio(cancelaciones[inicio : fin], valsEstimacion)
  with open('hare2.tex', 'a') as file_write:
    file_write.write(str(error) + '\n')

  ################## CML TERMINA

  plt.xlabel(u"Semana")
  plt.ylabel(u"Cantidad de cancelaciones")
  plt.xticks([24+48*i for i in range(0,5)],['2004', '2005', '2006', '2007', '2008'],fontsize=10)
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
      plt.axvline(x=12*4*i, linewidth=2, color='k')

    plt.plot(y, cancelaciones_filtro, 'ro', 
             alpha=opacity,
             linestyle='-',
             color='b',
             label=lab)

    plt.xlabel(u"Quincenas")
    plt.ylabel(u"Cantidad de cancelaciones")
    plt.xticks([24+48*i for i in range(0,5)],['2004', '2005', '2006', '2007', '2008'],fontsize=10)
    plt.legend()
    plt.savefig(fig)
    plt.show()


if __name__ == "__main__":
  main()
