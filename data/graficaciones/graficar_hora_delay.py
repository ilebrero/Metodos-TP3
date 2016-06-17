#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from math import log
import os

def readFile(File, anio, filtro_anio, data, d_filter):

  vuelos_por_dia = [[[0 for k in range(0, 24)] for i in range(0, 31)] for j in range(0, 12)]
  vuelos_por_dia_filtro = [[[0 for k in range(0, 24)] for i in range(0, 31)] for j in range(0, 12)]

  with open(File, 'r') as file_:
    for line in file_:
      currentline = line.split(",")
      dia_del_mes = int(currentline[2]) - 1
      dia_de_semana = int(currentline[3])
      mes = int(currentline[1]) - 1
      delay_filter = currentline[d_filter]
      delay = currentline[15]

      tiempo_de_vuelo = currentline[5]

      if len(tiempo_de_vuelo) == 4:
        tiempo_de_vuelo = int(tiempo_de_vuelo[:2]) # Le saco los primeros dos caracteres

      elif len(tiempo_de_vuelo) == 3:
        tiempo_de_vuelo = int(tiempo_de_vuelo[:1]) # Le saco primer caracter

      elif len(tiempo_de_vuelo) <= 2:
        tiempo_de_vuelo = 0                        # Es 00 y un numerito por ende es la primer posicion 


      if (delay != 'NA'):
        vuelos_por_dia[mes][dia_del_mes][tiempo_de_vuelo] += 1 

      if (delay != 'NA' and int(delay) > 15):

        anio[mes][dia_del_mes][0][tiempo_de_vuelo] += 1             # Cuento la cantidad de datos por hora
        anio[mes][dia_del_mes][1][tiempo_de_vuelo] += int(delay)    # Cuento la cantidad de datos por hora
        anio[mes][dia_del_mes][2]                  = dia_de_semana  # Sumo todos los datos del dia
        anio[mes][dia_del_mes][3]                  = dia_del_mes    # Guardo el dia de semana para el gráfico

      if (delay_filter != 'NA'):
        vuelos_por_dia_filtro[mes][dia_del_mes][tiempo_de_vuelo] += 1 

      if (delay_filter != 'NA' and int(delay_filter) > 15):

        filtro_anio[mes][dia_del_mes][0][tiempo_de_vuelo] += 1                 # Cuento la cantidad de datos por hora
        filtro_anio[mes][dia_del_mes][1][tiempo_de_vuelo] += int(delay_filter) # Cuento la cantidad de datos por hora
        filtro_anio[mes][dia_del_mes][2]                  = dia_de_semana      # Sumo todos los datos del dia
        filtro_anio[mes][dia_del_mes][3]                  = dia_del_mes        # Guardo el dia de semana para el gráfico


    for i in range(0, 12):
      for j in range(0, 31):
        for k in range(0, 24):
          if anio[i][j][0][k] != 0:
            anio[i][j][1][k] /= float(anio[i][j][0][k])                       # Divido la sumatoria de delays por la cantidad de delays

          if vuelos_por_dia[i][j][k] != 0:
            anio[i][j][0][k] /= float(vuelos_por_dia[i][j][k])               # Divido la cantidad de delays por la cantidad de vuelos en el dia

          if filtro_anio[i][j][0][k] != 0:
            filtro_anio[i][j][1][k] /= float(filtro_anio[i][j][0][k])         # Divido la sumatoria de delays por la cantidad de delays

          if vuelos_por_dia_filtro[i][j][k] != 0:
            filtro_anio[i][j][0][k] /= float(vuelos_por_dia_filtro[i][j][k]) # Divido la cantidad de delays por la cantidad de vuelos en el dia


def graficarHoraDelay(directory, airport, delay_filter, data):

# Instancio los arreglos para los datos

  anio_1998 = [[[[0 for k in range(0, 24)], [0 for z in range(0, 24)], 0, 0] for i in range(0, 31)] for j in range(0,12)]  
  anio_1999 = [[[[0 for k in range(0, 24)], [0 for z in range(0, 24)], 0, 0] for i in range(0, 31)] for j in range(0,12)]
  anio_2000 = [[[[0 for k in range(0, 24)], [0 for z in range(0, 24)], 0, 0] for i in range(0, 31)] for j in range(0,12)]
  anio_2001 = [[[[0 for k in range(0, 24)], [0 for z in range(0, 24)], 0, 0] for i in range(0, 31)] for j in range(0,12)]
  anio_2002 = [[[[0 for k in range(0, 24)], [0 for z in range(0, 24)], 0, 0] for i in range(0, 31)] for j in range(0,12)]
  anio_2003 = [[[[0 for k in range(0, 24)], [0 for z in range(0, 24)], 0, 0] for i in range(0, 31)] for j in range(0,12)]
  anio_2004 = [[[[0 for k in range(0, 24)], [0 for z in range(0, 24)], 0, 0] for i in range(0, 31)] for j in range(0,12)]
  anio_2005 = [[[[0 for k in range(0, 24)], [0 for z in range(0, 24)], 0, 0] for i in range(0, 31)] for j in range(0,12)]
  anio_2006 = [[[[0 for k in range(0, 24)], [0 for z in range(0, 24)], 0, 0] for i in range(0, 31)] for j in range(0,12)]
  anio_2007 = [[[[0 for k in range(0, 24)], [0 for z in range(0, 24)], 0, 0] for i in range(0, 31)] for j in range(0,12)]
  anio_2008 = [[[[0 for k in range(0, 24)], [0 for z in range(0, 24)], 0, 0] for i in range(0, 31)] for j in range(0,12)]

  filtro_anio_1998 = [[[[0 for k in range(0, 24)], [0 for z in range(0, 24)], 0, 0] for i in range(0, 31)] for j in range(0,12)]  
  filtro_anio_1999 = [[[[0 for k in range(0, 24)], [0 for z in range(0, 24)], 0, 0] for i in range(0, 31)] for j in range(0,12)]
  filtro_anio_2000 = [[[[0 for k in range(0, 24)], [0 for z in range(0, 24)], 0, 0] for i in range(0, 31)] for j in range(0,12)]
  filtro_anio_2001 = [[[[0 for k in range(0, 24)], [0 for z in range(0, 24)], 0, 0] for i in range(0, 31)] for j in range(0,12)]
  filtro_anio_2002 = [[[[0 for k in range(0, 24)], [0 for z in range(0, 24)], 0, 0] for i in range(0, 31)] for j in range(0,12)]
  filtro_anio_2003 = [[[[0 for k in range(0, 24)], [0 for z in range(0, 24)], 0, 0] for i in range(0, 31)] for j in range(0,12)]
  filtro_anio_2004 = [[[[0 for k in range(0, 24)], [0 for z in range(0, 24)], 0, 0] for i in range(0, 31)] for j in range(0,12)]
  filtro_anio_2005 = [[[[0 for k in range(0, 24)], [0 for z in range(0, 24)], 0, 0] for i in range(0, 31)] for j in range(0,12)]
  filtro_anio_2006 = [[[[0 for k in range(0, 24)], [0 for z in range(0, 24)], 0, 0] for i in range(0, 31)] for j in range(0,12)]
  filtro_anio_2007 = [[[[0 for k in range(0, 24)], [0 for z in range(0, 24)], 0, 0] for i in range(0, 31)] for j in range(0,12)]
  filtro_anio_2008 = [[[[0 for k in range(0, 24)], [0 for z in range(0, 24)], 0, 0] for i in range(0, 31)] for j in range(0,12)]

  file_out = directory + '/' + airport
  print file_out

  readFile(file_out + '1998.csv', anio_1998, filtro_anio_1998, data, delay_filter)
  readFile(file_out + '1999.csv', anio_1998, filtro_anio_1999, data, delay_filter)
  readFile(file_out + '2000.csv', anio_1998, filtro_anio_2000, data, delay_filter)
  readFile(file_out + '2001.csv', anio_1998, filtro_anio_2001, data, delay_filter)
  readFile(file_out + '2002.csv', anio_1998, filtro_anio_2002, data, delay_filter)
  readFile(file_out + '2003.csv', anio_1998, filtro_anio_2003, data, delay_filter)
  readFile(file_out + '2004.csv', anio_1998, filtro_anio_2004, data, delay_filter)
  readFile(file_out + '2005.csv', anio_2005, filtro_anio_2005, data, delay_filter)
  readFile(file_out + '2006.csv', anio_2006, filtro_anio_2006, data, delay_filter)
  readFile(file_out + '2007.csv', anio_2007, filtro_anio_2007, data, delay_filter)
  readFile(file_out + '2008.csv', anio_2008, filtro_anio_2008, data, delay_filter)

  years = 11

  # Instancio una lista vacia por cada mes de cada anio
  # Por cada mes quiero tener la cantidad de datos y los datos por dia 
  
  lunes     = [[ [ [], [] ] for j in range(0, 12)] for i in range(0, years)] 
  martes    = [[ [ [], [] ] for j in range(0, 12)] for i in range(0, years)] 
  miercoles = [[ [ [], [] ] for j in range(0, 12)] for i in range(0, years)]   
  jueves    = [[ [ [], [] ] for j in range(0, 12)] for i in range(0, years)] 
  viernes   = [[ [ [], [] ] for j in range(0, 12)] for i in range(0, years)] 
  sabado    = [[ [ [], [] ] for j in range(0, 12)] for i in range(0, years)] 
  domingo   = [[ [ [], [] ] for j in range(0, 12)] for i in range(0, years)] 

  filtro_lunes     = [[ [ [], [] ] for j in range(0, 12)] for i in range(0, years)] 
  filtro_martes    = [[ [ [], [] ] for j in range(0, 12)] for i in range(0, years)] 
  filtro_miercoles = [[ [ [], [] ] for j in range(0, 12)] for i in range(0, years)]   
  filtro_jueves    = [[ [ [], [] ] for j in range(0, 12)] for i in range(0, years)] 
  filtro_viernes   = [[ [ [], [] ] for j in range(0, 12)] for i in range(0, years)] 
  filtro_sabado    = [[ [ [], [] ] for j in range(0, 12)] for i in range(0, years)] 
  filtro_domingo   = [[ [ [], [] ] for j in range(0, 12)] for i in range(0, years)] 

  #print anio_2005

  anios = [anio_1998, anio_1999, anio_2000, anio_2001, anio_2002, anio_2003, anio_2004, anio_2005, anio_2006, anio_2007, anio_2008]

  filtro_anios = [filtro_anio_1998, filtro_anio_1999, filtro_anio_2000, filtro_anio_2001, filtro_anio_2002, filtro_anio_2003, filtro_anio_2004, filtro_anio_2005, filtro_anio_2006, filtro_anio_2007, filtro_anio_2008]

  # Ya tengo el promedio de cantidad de datos y datos de cada hora por dia 
  # Para mes y anio

  # Ahora quiero:
  # El promedio de cada hora por mes 

  # El promedio de cada hora por mes dentro de un anio. Así obtendria
  # 168 valores por mes. Total de valores = 2016

  # El promedio de cada hora por mes dentro de un anio. 
  # 24*7 valores por anio. Total de valores = 168
  # Tengo que sumar todos los dias con sus respectivos

  [[[[0 for k in range(0, 24)], [0 for z in range(0, 24)], 0, 0] for i in range(0, 31)] for j in range(0,12)]

  for i in range(0, years):
    anio = anios[i]
    filtro_anio = filtro_anios[i]
    for j in range(0, 12):
      mes = anio[j]
      filtro_mes = filtro_anio[j]
      for k in range(0, 31):
        day = mes[k]
        filtro_day = filtro_mes[k]

        for z in range(0, 24):

          cant_datos = day[0][z]
          datos = day[1][z]

          filtro_cant_datos = filtro_day[0][z]
          filtro_datos = filtro_day[1][z]
          
          if day[2] == 1:
            lunes[i][j][0][z] += cant_datos # Le meto en la primer posicion la cantidad de datos
            lunes[i][j][1][z] += datos # Le meto en la segunda posicion la suma de los daots
            filtro_lunes[i][j][0][z] += filtro_cant_datos
            filtro_lunes[i][j][1][z] += filtro_datos

          elif day[2] == 2:
            martes[i][j][0][z] += cant_datos # Le meto en la primer posicion la cantidad de datos
            martes[i][j][1][z] += datos # Le meto en la segunda posicion la suma de los daots
            filtro_martes[i][j][0][z] += filtro_cant_datos
            filtro_martes[i][j][1][z] += filtro_datos

          elif day[2] == 3:
            miercoles[i][j][0][z] += cant_datos # Le meto en la primer posicion la cantidad de datos
            miercoles[i][j][1][z] += datos # Le meto en la segunda posicion la suma de los daots
            filtro_miercoles[i][j][0][z] += filtro_cant_datos
            filtro_miercoles[i][j][1][z] += filtro_datos

          elif day[2] == 4:
            jueves[i][j][0][z] += cant_datos # Le meto en la primer posicion la cantidad de datos
            jueves[i][j][1][z] += datos # Le meto en la segunda posicion la suma de los daots
            filtro_jueves[i][j][0][z] += filtro_cant_datos
            filtro_jueves[i][j][1][z] += filtro_datos

          elif day[2] == 5:
            viernes[i][j][0][z] += cant_datos # Le meto en la primer posicion la cantidad de datos
            viernes[i][j][1][z] += datos # Le meto en la segunda posicion la suma de los daots
            filtro_viernes[i][j][0][z] += filtro_cant_datos
            filtro_viernes[i][j][1][z] += filtro_datos

          elif day[2] == 6:
            sabado[i][j][0][z] += cant_datos # Le meto en la primer posicion la cantidad de datos
            sabado[i][j][1][z] += datos # Le meto en la segunda posicion la suma de los daots
            filtro_sabado[i][j][0][z] += filtro_cant_datos
            filtro_sabado[i][j][1][z] += filtro_datos

          elif day[2] == 7:
            domingo[i][j][0][z] += cant_datos # Le meto en la primer posicion la cantidad de datos
            domingo[i][j][1][z] += datos # Le meto en la segunda posicion la suma de los daots
            filtro_domingo[i][j][0][z] += filtro_cant_datos
            filtro_domingo[i][j][1][z] += filtro_datos

  # El promedio de cada hora por anio.
  # Total de valores 24.

  # El promedio de cada hora por anio dentro de todos los anios

  if not os.path.exists(directory + '/graficos'):
    os.mkdir(directory + '/graficos')

  # lunes[anio][mes][0][hora] Tengo la acumulada de cantidad de delays por mes
  # lunes[anio][mes][1][hora] Tengo la acumulada de delays por mes

  x_lunes     = [i for i in range(0, 24)] 
  x_martes    = [i for i in range(24, 48)] 
  x_miercoles = [i for i in range(48, 72)]   
  x_jueves    = [i for i in range(72, 96)] 
  x_viernes   = [i for i in range(96, 120)] 
  x_sabado    = [i for i in range(120, 144)] 
  x_domingo   = [i for i in range(144, 168)] 

  opacity = 0.4

  years=12
# Debería haber cantidad de anios-1 
  for i in range(0, 7):
    plt.axvline(x=24*i, linewidth=2, color='k')

  for i in range(0, 3):
    plt.plot(x_lunes, lunes[4][i][0], 'ro', 
             alpha=opacity,
             color='b',
             label=u"Lunes")

    plt.plot(x_martes, martes[4][i][0], 'ro', 
             alpha=opacity,
             color='g',
             label=u"Martes")

    plt.plot(x_miercoles, miercoles[4][i][0], 'ro', 
             alpha=opacity,
             color='r',
             label=u"Miercoles")

    plt.plot(x_jueves, jueves[4][i][0], 'ro', 
             alpha=opacity,
             color='c',
             label=u"Jueves")

    plt.plot(x_viernes, viernes[4][i][0], 'ro', 
             alpha=opacity,
             color='m',
             label=u"Viernes")

    plt.plot(x_sabado, sabado[4][i][0], 'ro', 
             alpha=opacity,
             color='y',
             label=u"Sabado")

    plt.plot(x_domingo, domingo[4][i][0], 'ro', 
             alpha=opacity,
             color='k',
             label=u"Domingo")

    plt.xlabel(u"dias")
    plt.ylabel(u"Cantidad de delays")
    plt.xticks([12+24*j for j in range(0,7)],['Lun', 'mar', 'mier', 'juev', 'vier', 'sab', 'dom'],fontsize=10)
    plt.legend()
    plt.savefig(directory + '/graficos/grafico_cantidad_delay_hora')
    plt.show()

if __name__ == "__main__":
  main()
