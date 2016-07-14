#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from math import log
import os

def readFile(File, anio):

  vuelos_por_dia = [[0 for i in range(0, 31)] for j in range(0, 12)]

  with open(File, 'r') as file_:
    for line in file_:
      currentline = line.split(",")
      mes = int(currentline[1]) - 1
      dia_del_mes = int(currentline[2]) - 1
      dia_de_semana = int(currentline[3])

      if data == 16:
        
        org = currentline[16]
        dest = currentline[17]
        delay = ''

        if airport == org:
          delay = currentline[15] # El delay es el de salida
        else:
          delay = currentline[14] # El delay es el de llegada

      else:
        delay = currentline[data]


        if (delay != 'NA'):
          vuelos_por_dia[mes][dia_del_mes] += 1 

        if (delay != 'NA' and int(delay) > 15):

          anio[mes][dia_del_mes][0] += 1 # Cuento la cantidad de datos por mes
          anio[mes][dia_del_mes][1] += int(delay)  # Sumo todos los datos del mes
          anio[mes][dia_del_mes][2] += dia_de_semana  # Guardo el dia de semana para el grafico

      if (currentline[delay_filter] != 'NA'):
        vuelos_por_semana_filtro[semana+4*mes] += 1 

      if (currentline[delay_filter] != 'NA' and int(currentline[delay_filter]) > 15):
        dep_delay = int(currentline[delay_filter])

        data_3[semana+4*mes] += 1 # Cuento la cantidad de datos por mes
        data_4[semana+4*mes] += dep_delay  # Sumo todos los datos del mes

  for i in range(0, 48):
    if data_1[i] != 0:
      data_2[i] /= float(data_1[i])

  for i in range(0, 48):
    if vuelos_por_semana[i] != 0:
      data_1[i] /= float(vuelos_por_semana[i])

  for i in range(0, 48):
    if data_3[i] != 0:
      data_4[i] /= float(data_3[i])

  for i in range(0, 48):
    if vuelos_por_semana_filtro[i] != 0:
      data_3[i] /= float(vuelos_por_semana_filtro[i])

def graficarSemanaDelay(directory, airport, delay_filter, data):

# Instancio los arreglos para los datos

  anio = [[[0, 0, 0] for i in range(0, 31)] for j in range(0, 13)]

  file_out = directory + '/' + airport
  print file_out

  readFile(file_out + '1998.csv', cant_delays_1998, delays_1998, cant_delays_filter_1998, delays_filter_1998, delay_filter, data, airport)
  readFile(file_out + '1999.csv', cant_delays_1999, delays_1999, cant_delays_filter_1999, delays_filter_1999, delay_filter, data, airport)
  readFile(file_out + '2000.csv', cant_delays_2000, delays_2000, cant_delays_filter_2000, delays_filter_2000, delay_filter, data, airport)
  readFile(file_out + '2001.csv', cant_delays_2001, delays_2001, cant_delays_filter_2001, delays_filter_2001, delay_filter, data, airport)
  readFile(file_out + '2002.csv', cant_delays_2002, delays_2002, cant_delays_filter_2002, delays_filter_2002, delay_filter, data, airport)
  readFile(file_out + '2003.csv', cant_delays_2003, delays_2003, cant_delays_filter_2003, delays_filter_2003, delay_filter, data, airport)
  readFile(file_out + '2004.csv', cant_delays_2004, delays_2004, cant_delays_filter_2004, delays_filter_2004, delay_filter, data, airport)
  readFile(file_out + '2005.csv', cant_delays_2005, delays_2005, cant_delays_filter_2005, delays_filter_2005, delay_filter, data, airport)
  readFile(file_out + '2006.csv', cant_delays_2006, delays_2006, cant_delays_filter_2006, delays_filter_2006, delay_filter, data, airport)
  readFile(file_out + '2007.csv', cant_delays_2007, delays_2007, cant_delays_filter_2007, delays_filter_2007, delay_filter, data, airport)
  readFile(file_out + '2008.csv', cant_delays_2008, delays_2008, cant_delays_filter_2008, delays_filter_2008, delay_filter, data, airport)

  datos = []

  years = 11
  x = []
  y = []

  len_x = years * 12 * 4
  len_y = (years-3) * 12 * 4

  for i in range(1, len_x+1):
    x.append(i)

  for i in range(1, len_y+1):
    y.append(i)

  cant_delays = cant_delays_1998 + cant_delays_1999 + cant_delays_2000 + cant_delays_2001 + cant_delays_2002 + cant_delays_2003 + cant_delays_2004 + cant_delays_2005 + cant_delays_2006 + cant_delays_2007 + cant_delays_2008
  delays = delays_1998 + delays_1999 + delays_2000 + delays_2001 + delays_2002 + delays_2003 + delays_2004 + delays_2005 + delays_2006 + delays_2007 + delays_2008

  cant_delays_filter = cant_delays_filter_2001 + cant_delays_filter_2002 + cant_delays_filter_2003 + cant_delays_filter_2004 + cant_delays_filter_2005 + cant_delays_filter_2006 + cant_delays_filter_2007 + cant_delays_filter_2008
  delays_filter = delays_filter_2001 + delays_filter_2002 + delays_filter_2003 + delays_filter_2004 + delays_filter_2005 + delays_filter_2006 + delays_filter_2007 + delays_filter_2008

  if not os.path.exists(directory + '/graficos'):
    os.mkdir(directory + '/graficos')

  opacity = 0.4

# Debería haber cantidad de anios-1 
  for i in range(1, years):
    plt.axvline(x=12*4*i, linewidth=2, color='k')

  plt.plot(x, cant_delays, 'ro', 
           alpha=opacity,
           linestyle='-',
           color='b',
           label=u"Cantidad de delay por semana")

  plt.xlabel(u"Semanas")
  plt.ylabel(u"Cantidad de delays")
  plt.xticks([24+12*i*4 for i in range(0,years)],['1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008'],fontsize=10)
  plt.legend()
  plt.savefig(directory + '/graficos/grafico_cantidad_delay_semana')
  plt.show()

  for i in range(1, years):
    plt.axvline(x=12*4*i, linewidth=2, color='k')

  plt.plot(x, delays, 'ro', 
           alpha=opacity,
           linestyle='-',
           color='b',
           label=u"Delays por semana")

  plt.xlabel(u"Semanas")
  plt.ylabel(u"Delays")
  plt.xticks([24+12*i*4 for i in range(0,years)],['1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008'],fontsize=10)
  plt.legend()
  plt.savefig(directory + '/graficos/grafico_delay_semana')
  plt.show()

  if delay_filter != 0:
    lab = ''
    lab_f = ''
    fig = ''
    fig_f = ''
    if delay_filter == 24:
      lab = "Cantidad de delays de carrier por semana"
      lab_f = "Delays de carrier por semana"
      fig = directory + '/graficos/grafico_cantidad_delays_carrier_semana'
      fig_f = directory + '/graficos/grafico_delays_carrier_semana'

    if delay_filter == 25:
      lab = "Cantidad de delays de clima por semana"
      lab_f = "Delays de clima por semana"
      fig = directory + '/graficos/grafico_cantidad_delays_clima_semana'
      fig_f = directory + '/graficos/grafico_delays_clima_semana'

    if delay_filter == 26:
      lab = "Cantidad de delays de NAS por semana"
      lab_f = "Delays de NAS por semana"
      fig = directory + '/graficos/grafico_cantidad_delays_NAS_semana'
      fig_f = directory + '/graficos/grafico_delays_NAS_semana'

    if delay_filter == 27:
      lab = "Cantidad de delays de seguridad por semana"
      lab_f = "Delays de seguridad por semana"
      fig = directory + '/graficos/grafico_cantidad_delays_seguridad_semana'
      fig_f = directory + '/graficos/grafico_delays_seguridad_semana'

    for i in range(1, years-3):
      plt.axvline(x=12*i*4, linewidth=2, color='k')

    plt.plot(y, cant_delays_filter, 'ro', 
             alpha=opacity,
             linestyle='-',
             color='b',
             label=lab)

    plt.xlabel(u"Semanas")
    plt.ylabel(u"Cantidad de delays")
    plt.xticks([6+12*i*4 for i in range(0,years-3)],['2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008'],fontsize=10)
    plt.legend()
    plt.savefig(fig)
    plt.show()

    for i in range(1, years-3):
      plt.axvline(x=12*i*4, linewidth=2, color='k')

    plt.plot(y, delays_filter, 'ro', 
             alpha=opacity,
             linestyle='-',
             color='b',
             label=lab_f)

    plt.xlabel(u"Semanas")
    plt.ylabel(u"Delays")
    plt.xticks([6+12*i*4 for i in range(0,years-3)],['2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008'],fontsize=10)
    plt.legend()
    plt.savefig(fig_f)
    plt.show()

if __name__ == "__main__":
  main()
