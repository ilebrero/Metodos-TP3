#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from math import log
import os

# Leo los archivos y genero los arreglos con todos los datos

def readFile(File, data_1, data_2, data_3, data_4, delay_filter, data, airport):

  vuelos_por_mes = [0 for i in range(0, 12)]
  vuelos_por_mes_filtro = [0 for i in range(0, 12)]

  with open(File, 'r') as file_:
    for line in file_:
      currentline = line.split(",")
      mes = int(currentline[1]) - 1

      if data == 16:
        
        org = currentline[16]
        dest = currentline[17]
        delay = ''

        if airport == org:
          delay = currentline[15] # El delay es el de salida
        else:
          delay = currentline[14] # El delay es el de llegada

        if (delay != 'NA'):
          vuelos_por_mes[mes] += 1 

        if (delay != 'NA' and int(delay) > 15):
          if int(delay) < 60:

            data_1[mes] += 1 # Cuento la cantidad de datos por mes
            data_2[mes] += int(delay)  # Sumo todos los datos del mes

      else:

        if (currentline[data] != 'NA'):
          vuelos_por_mes[mes] += 1 

        if (currentline[data] != 'NA' and int(currentline[data]) > 15):
          dep_delay = int(currentline[data])
          if dep_delay < 60:

            data_1[mes] += 1 # Cuento la cantidad de datos por mes
            data_2[mes] += dep_delay  # Sumo todos los datos del mes

      if (currentline[delay_filter] != 'NA'):
        vuelos_por_mes_filtro[mes] += 1 

      if (currentline[delay_filter] != 'NA' and int(currentline[delay_filter]) > 15):
        dep_delay = int(currentline[delay_filter])
        if dep_delay < 60:

          data_3[mes] += 1 # Cuento la cantidad de datos por mes
          data_4[mes] += dep_delay  # Sumo todos los datos del mes


  for i in range(0, 12):
    if data_1[i] != 0:
      data_2[i] /= float(data_1[i])

  for i in range(0, 12):
    if vuelos_por_mes[i] != 0:
      data_1[i] /= float(vuelos_por_mes[i])

  for i in range(0, 12):
    if data_3[i] != 0:
      data_4[i] /= float(data_3[i])

  for i in range(0, 12):
    if vuelos_por_mes_filtro[i] != 0:
      data_3[i] /= float(vuelos_por_mes_filtro[i])

def graficarMesDelay2(directory_1, directory_2, directory_both, airport_1, airport_2, delay_filter, data):

# Instancio los arreglos para los datos

  delays_1998 = [0 for i in range(0, 12)]
  cant_delays_1998 = [0 for i in range(0,12)]
  delays_filter_1998 = [0 for i in range(0, 12)]
  cant_delays_filter_1998 = [0 for i in range(0,12)]

  delays_1999 = [0 for i in range(0, 12)]
  cant_delays_1999 = [0 for i in range(0,12)]
  delays_filter_1999 = [0 for i in range(0, 12)]
  cant_delays_filter_1999 = [0 for i in range(0,12)]

  delays_2000 = [0 for i in range(0, 12)]
  cant_delays_2000 = [0 for i in range(0,12)]
  delays_filter_2000 = [0 for i in range(0, 12)]
  cant_delays_filter_2000 = [0 for i in range(0,12)]

  delays_2001 = [0 for i in range(0, 12)]
  cant_delays_2001 = [0 for i in range(0,12)]
  delays_filter_2001 = [0 for i in range(0, 12)]
  cant_delays_filter_2001 = [0 for i in range(0,12)]

  delays_2002 = [0 for i in range(0, 12)]
  cant_delays_2002 = [0 for i in range(0,12)]
  delays_filter_2002 = [0 for i in range(0, 12)]
  cant_delays_filter_2002 = [0 for i in range(0,12)]

  delays_2003 = [0 for i in range(0, 12)]
  cant_delays_2003 = [0 for i in range(0,12)]
  delays_filter_2003 = [0 for i in range(0, 12)]
  cant_delays_filter_2003 = [0 for i in range(0,12)]

  delays_2004 = [0 for i in range(0, 12)]
  cant_delays_2004 = [0 for i in range(0,12)]
  delays_filter_2004 = [0 for i in range(0, 12)]
  cant_delays_filter_2004 = [0 for i in range(0,12)]

  delays_2005 = [0 for i in range(0, 12)]
  cant_delays_2005 = [0 for i in range(0,12)]
  delays_filter_2005 = [0 for i in range(0, 12)]
  cant_delays_filter_2005 = [0 for i in range(0,12)]

  delays_2006 = [0 for i in range(0, 12)]
  cant_delays_2006 = [0 for i in range(0,12)]
  delays_filter_2006 = [0 for i in range(0, 12)]
  cant_delays_filter_2006 = [0 for i in range(0,12)]

  delays_2007 = [0 for i in range(0, 12)]
  cant_delays_2007 = [0 for i in range(0,12)]
  delays_filter_2007 = [0 for i in range(0, 12)]
  cant_delays_filter_2007 = [0 for i in range(0,12)]

  delays_2008 = [0 for i in range(0, 12)]
  cant_delays_2008 = [0 for i in range(0,12)]
  delays_filter_2008 = [0 for i in range(0, 12)]
  cant_delays_filter_2008 = [0 for i in range(0,12)]

  a_delays_1998 = [0 for i in range(0, 12)]
  a_cant_delays_1998 = [0 for i in range(0,12)]
  a_delays_filter_1998 = [0 for i in range(0, 12)]
  a_cant_delays_filter_1998 = [0 for i in range(0,12)]

  a_delays_1999 = [0 for i in range(0, 12)]
  a_cant_delays_1999 = [0 for i in range(0,12)]
  a_delays_filter_1999 = [0 for i in range(0, 12)]
  a_cant_delays_filter_1999 = [0 for i in range(0,12)]

  a_delays_2000 = [0 for i in range(0, 12)]
  a_cant_delays_2000 = [0 for i in range(0,12)]
  a_delays_filter_2000 = [0 for i in range(0, 12)]
  a_cant_delays_filter_2000 = [0 for i in range(0,12)]

  a_delays_2001 = [0 for i in range(0, 12)]
  a_cant_delays_2001 = [0 for i in range(0,12)]
  a_delays_filter_2001 = [0 for i in range(0, 12)]
  a_cant_delays_filter_2001 = [0 for i in range(0,12)]

  a_delays_2002 = [0 for i in range(0, 12)]
  a_cant_delays_2002 = [0 for i in range(0,12)]
  a_delays_filter_2002 = [0 for i in range(0, 12)]
  a_cant_delays_filter_2002 = [0 for i in range(0,12)]

  a_delays_2003 = [0 for i in range(0, 12)]
  a_cant_delays_2003 = [0 for i in range(0,12)]
  a_delays_filter_2003 = [0 for i in range(0, 12)]
  a_cant_delays_filter_2003 = [0 for i in range(0,12)]

  a_delays_2004 = [0 for i in range(0, 12)]
  a_cant_delays_2004 = [0 for i in range(0,12)]
  a_delays_filter_2004 = [0 for i in range(0, 12)]
  a_cant_delays_filter_2004 = [0 for i in range(0,12)]

  a_delays_2005 = [0 for i in range(0, 12)]
  a_cant_delays_2005 = [0 for i in range(0,12)]
  a_delays_filter_2005 = [0 for i in range(0, 12)]
  a_cant_delays_filter_2005 = [0 for i in range(0,12)]

  a_delays_2006 = [0 for i in range(0, 12)]
  a_cant_delays_2006 = [0 for i in range(0,12)]
  a_delays_filter_2006 = [0 for i in range(0, 12)]
  a_cant_delays_filter_2006 = [0 for i in range(0,12)]

  a_delays_2007 = [0 for i in range(0, 12)]
  a_cant_delays_2007 = [0 for i in range(0,12)]
  a_delays_filter_2007 = [0 for i in range(0, 12)]
  a_cant_delays_filter_2007 = [0 for i in range(0,12)]

  a_delays_2008 = [0 for i in range(0, 12)]
  a_cant_delays_2008 = [0 for i in range(0,12)]
  a_delays_filter_2008 = [0 for i in range(0, 12)]
  a_cant_delays_filter_2008 = [0 for i in range(0,12)]

  file_out = directory_1 + '/' + airport_1

  readFile(file_out + '1998.csv', cant_delays_1998, delays_1998, cant_delays_filter_1998, delays_filter_1998, delay_filter, data, airport_1)
  readFile(file_out + '1999.csv', cant_delays_1999, delays_1999, cant_delays_filter_1999, delays_filter_1999, delay_filter, data, airport_1)
  readFile(file_out + '2000.csv', cant_delays_2000, delays_2000, cant_delays_filter_2000, delays_filter_2000, delay_filter, data, airport_1)
  readFile(file_out + '2001.csv', cant_delays_2001, delays_2001, cant_delays_filter_2001, delays_filter_2001, delay_filter, data, airport_1)
  readFile(file_out + '2002.csv', cant_delays_2002, delays_2002, cant_delays_filter_2002, delays_filter_2002, delay_filter, data, airport_1)
  readFile(file_out + '2003.csv', cant_delays_2003, delays_2003, cant_delays_filter_2003, delays_filter_2003, delay_filter, data, airport_1)
  readFile(file_out + '2004.csv', cant_delays_2004, delays_2004, cant_delays_filter_2004, delays_filter_2004, delay_filter, data, airport_1)
  readFile(file_out + '2005.csv', cant_delays_2005, delays_2005, cant_delays_filter_2005, delays_filter_2005, delay_filter, data, airport_1)
  readFile(file_out + '2006.csv', cant_delays_2006, delays_2006, cant_delays_filter_2006, delays_filter_2006, delay_filter, data, airport_1)
  readFile(file_out + '2007.csv', cant_delays_2007, delays_2007, cant_delays_filter_2007, delays_filter_2007, delay_filter, data, airport_1)
  readFile(file_out + '2008.csv', cant_delays_2008, delays_2008, cant_delays_filter_2008, delays_filter_2008, delay_filter, data, airport_1)

  file_out = directory_2 + '/' + airport_2

  readFile(file_out + '1998.csv', a_cant_delays_1998, a_delays_1998, a_cant_delays_filter_1998, a_delays_filter_1998, delay_filter, data, airport_2)
  readFile(file_out + '1999.csv', a_cant_delays_1999, a_delays_1999, a_cant_delays_filter_1999, a_delays_filter_1999, delay_filter, data, airport_2)
  readFile(file_out + '2000.csv', a_cant_delays_2000, a_delays_2000, a_cant_delays_filter_2000, a_delays_filter_2000, delay_filter, data, airport_2)
  readFile(file_out + '2001.csv', a_cant_delays_2001, a_delays_2001, a_cant_delays_filter_2001, a_delays_filter_2001, delay_filter, data, airport_2)
  readFile(file_out + '2002.csv', a_cant_delays_2002, a_delays_2002, a_cant_delays_filter_2002, a_delays_filter_2002, delay_filter, data, airport_2)
  readFile(file_out + '2003.csv', a_cant_delays_2003, a_delays_2003, a_cant_delays_filter_2003, a_delays_filter_2003, delay_filter, data, airport_2)
  readFile(file_out + '2004.csv', a_cant_delays_2004, a_delays_2004, a_cant_delays_filter_2004, a_delays_filter_2004, delay_filter, data, airport_2)
  readFile(file_out + '2005.csv', a_cant_delays_2005, a_delays_2005, a_cant_delays_filter_2005, a_delays_filter_2005, delay_filter, data, airport_2)
  readFile(file_out + '2006.csv', a_cant_delays_2006, a_delays_2006, a_cant_delays_filter_2006, a_delays_filter_2006, delay_filter, data, airport_2)
  readFile(file_out + '2007.csv', a_cant_delays_2007, a_delays_2007, a_cant_delays_filter_2007, a_delays_filter_2007, delay_filter, data, airport_2)
  readFile(file_out + '2008.csv', a_cant_delays_2008, a_delays_2008, a_cant_delays_filter_2008, a_delays_filter_2008, delay_filter, data, airport_2)

  years = 11
  x = []
  y = []

  for i in range(0, years):
    for j in range(1, 13):
      x.append(j+12*i)

      if i < years-3:
        y.append(j+12*i)

  cant_delays = cant_delays_1998 + cant_delays_1999 + cant_delays_2000 + cant_delays_2001 + cant_delays_2002 + cant_delays_2003 + cant_delays_2004 + cant_delays_2005 + cant_delays_2006 + cant_delays_2007 + cant_delays_2008
  delays = delays_1998 + delays_1999 + delays_2000 + delays_2001 + delays_2002 + delays_2003 + delays_2004 + delays_2005 + delays_2006 + delays_2007 + delays_2008

  cant_delays_filter = cant_delays_filter_2001 + cant_delays_filter_2002 + cant_delays_filter_2003 + cant_delays_filter_2004 + cant_delays_filter_2005 + cant_delays_filter_2006 + cant_delays_filter_2007 + cant_delays_filter_2008
  delays_filter = delays_filter_2001 + delays_filter_2002 + delays_filter_2003 + delays_filter_2004 + delays_filter_2005 + delays_filter_2006 + delays_filter_2007 + delays_filter_2008

  a_cant_delays = a_cant_delays_1998 + a_cant_delays_1999 + a_cant_delays_2000 + a_cant_delays_2001 + a_cant_delays_2002 + a_cant_delays_2003 + a_cant_delays_2004 + a_cant_delays_2005 + a_cant_delays_2006 + a_cant_delays_2007 + a_cant_delays_2008
  a_delays = a_delays_1998 + a_delays_1999 + a_delays_2000 + a_delays_2001 + a_delays_2002 + a_delays_2003 + a_delays_2004 + a_delays_2005 + a_delays_2006 + a_delays_2007 + a_delays_2008

  a_cant_delays_filter = a_cant_delays_filter_2001 + a_cant_delays_filter_2002 + a_cant_delays_filter_2003 + a_cant_delays_filter_2004 + a_cant_delays_filter_2005 + a_cant_delays_filter_2006 + a_cant_delays_filter_2007 + a_cant_delays_filter_2008
  a_delays_filter = a_delays_filter_2001 + a_delays_filter_2002 + a_delays_filter_2003 + a_delays_filter_2004 + a_delays_filter_2005 + a_delays_filter_2006 + a_delays_filter_2007 + a_delays_filter_2008

  length = len(cant_delays)
  rest_cant_delays = []
  rest_delays = []
  for i in range (length):
    rest_cant_delays.append(cant_delays[i] - a_cant_delays[i])
    rest_delays.append(delays[i] - a_delays[i])


  if not os.path.exists(directory_both + '/graficos'):
    os.mkdir(directory_both + '/graficos')

  opacity = 0.4


  for i in range(1, years):
    plt.axvline(x=12*i, linewidth=2, color='k')

  positives = [num for num in rest_cant_delays if num >= 0]
  x_positives = [i for i in range(0, len(rest_cant_delays)) if rest_cant_delays[i] >= 0]
  negatives = [num for num in rest_cant_delays if num < 0]
  x_negatives = [i for i in range(0, len(rest_cant_delays)) if rest_cant_delays[i] < 0]

  plt.plot(x_positives, positives, 'ro', 
           alpha=opacity,
           linestyle='-',
           color='b',
           label=u"Cantidad de delays por mes")

  plt.plot(x_negatives, negatives, 'ro', 
           alpha=opacity,
           linestyle='-',
           color='r',
           label=u"Cantidad de delays por mes")

  plt.xlabel(u"Meses")
  plt.ylabel(u"Cantidad de delays")
  plt.xticks([6+12*i for i in range(0,11)],['1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008'],fontsize=10)
  plt.legend()
  plt.savefig(directory_both + '/graficos/grafico_cantidad_delay_mes')
  plt.show()


  for i in range(1, years):
    plt.axvline(x=12*i, linewidth=2, color='k')

  positives = [num for num in rest_delays if num >= 0]
  x_positives = [i for i in range(0, len(rest_delays)) if rest_delays[i] >= 0]
  negatives = [num for num in rest_delays if num < 0]
  x_negatives = [i for i in range(0, len(rest_delays)) if rest_delays[i] < 0]

  plt.plot(x_positives, positives, 'ro', 
           alpha=opacity,
           linestyle='-',
           color='b',
           label=u"Cantidad de delays por mes")

  plt.plot(x_negatives, negatives, 'ro', 
           alpha=opacity,
           linestyle='-',
           color='r',
           label=u"Cantidad de delays por mes")

  plt.xlabel(u"Meses")
  plt.ylabel(u"Cantidad de delays")
  plt.xticks([6+12*i for i in range(0,11)],['1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008'],fontsize=10)
  plt.legend()
  plt.savefig(directory_both + '/graficos/grafico_cantidad_delay_mes')
  plt.show()






# Debería haber cantidad de años-1 
  for i in range(1, years):
    plt.axvline(x=12*i, linewidth=2, color='k')

  plt.plot(x, cant_delays, 'ro', 
           alpha=opacity,
           linestyle='-',
           color='b',
           label=u"Cantidad de delays por mes" + ' ' + airport_1)

  plt.plot(x, a_cant_delays, 'ro', 
           alpha=opacity,
           linestyle='-',
           color='r',
           label=u"Cantidad de delays por mes" + ' ' + airport_2)

  plt.xlabel(u"Meses")
  plt.ylabel(u"Cantidad de delays")
  plt.xticks([6+12*i for i in range(0,11)],['1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008'],fontsize=10)
  plt.legend()
  plt.savefig(directory_both + '/graficos/grafico_cantidad_delay_mes')
  plt.show()

  for i in range(1, years):
    plt.axvline(x=12*i, linewidth=2, color='k')

  plt.plot(x, delays, 'ro', 
           alpha=opacity,
           linestyle='-',
           color='b',
           label=u"Delays por mes" + ' ' + airport_1)

  plt.plot(x, a_delays, 'ro', 
           alpha=opacity,
           linestyle='-',
           color='r',
           label=u"Delays por mes" + ' ' + airport_2)

  plt.xlabel(u"Meses")
  plt.ylabel(u"Delays")
  plt.xticks([6+12*i for i in range(0,11)],['1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008'],fontsize=10)
  plt.legend()
  plt.savefig(directory_both + '/graficos/grafico_delay_mes')
  plt.show()

  if delay_filter != 0:
    lab = ''
    lab_f = ''
    fig = ''
    fig_f = ''
    if delay_filter == 24:
      lab = "Cantidad de delays de carrier por mes"
      lab_f = "Delays de carrier por mes"
      fig = directory_both + '/graficos/grafico_cantidad_delays_carrier_mes'
      fig_f = directory_both + '/graficos/grafico_delays_carrier_mes'

    if delay_filter == 25:
      lab = "Cantidad de delays de clima por mes"
      lab_f = "Delays de clima por mes"
      fig = directory_both + '/graficos/grafico_cantidad_delays_clima_mes'
      fig_f = directory_both + '/graficos/grafico_delays_clima_mes'

    if delay_filter == 26:
      lab = "Cantidad de delays de NAS por mes"
      lab_f = "Delays de NAS por mes"
      fig = directory_both + '/graficos/grafico_cantidad_delays_NAS_mes'
      fig_f = directory_both + '/graficos/grafico_delays_NAS_mes'

    if delay_filter == 27:
      lab = "Cantidad de delays de seguridad por mes"
      lab_f = "Delays de seguridad por mes"
      fig = directory_both + '/graficos/grafico_cantidad_delays_seguridad_mes'
      fig_f = directory_both + '/graficos/grafico_delays_seguridad_mes'

    for i in range(1, years-3):
      plt.axvline(x=12*i, linewidth=2, color='k')

    plt.plot(y, cant_delays_filter, 'ro', 
             alpha=opacity,
             linestyle='-',
             color='b',
             label=lab + ' ' + airport_1)

    plt.plot(y, a_cant_delays_filter, 'ro', 
             alpha=opacity,
             linestyle='-',
             color='r',
             label=lab + ' ' + airport_2)

    plt.xlabel(u"Meses")
    plt.ylabel(u"Cantidad de delays")
    plt.xticks([6+12*i for i in range(0,years-3)],['2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008'],fontsize=10)
    plt.legend()
    plt.savefig(fig)
    plt.show()

    for i in range(1, years-3):
      plt.axvline(x=12*i, linewidth=2, color='k')

    plt.plot(y, delays_filter, 'ro', 
             alpha=opacity,
             linestyle='-',
             color='b',
             label=lab_f + ' ' + airport_1)

    plt.plot(y, a_delays_filter, 'ro', 
             alpha=opacity,
             linestyle='-',
             color='r',
             label=lab_f + ' ' + airport_2)

    plt.xlabel(u"Meses")
    plt.ylabel(u"Delays")
    plt.xticks([6+12*i for i in range(0,years-3)],['2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008'],fontsize=10)
    plt.legend()
    plt.savefig(fig_f)
    plt.show()


if __name__ == "__main__":
  main()
