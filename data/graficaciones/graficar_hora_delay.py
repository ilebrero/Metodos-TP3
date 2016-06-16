#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from math import log
import os

def readFile(File, año, filtro_año, data):

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

        año[mes][dia_del_mes][0][tiempo_de_vuelo] += 1             # Cuento la cantidad de datos por hora
        año[mes][dia_del_mes][1][tiempo_de_vuelo] += int(delay)    # Cuento la cantidad de datos por hora
        año[mes][dia_del_mes][2]                  = dia_de_semana  # Sumo todos los datos del dia
        año[mes][dia_del_mes][3]                  = dia_del_mes    # Guardo el dia de semana para el gráfico

      if (delay_filter != 'NA'):
        vuelos_por_dia_filtro[mes][dia_del_mes][tiempo_de_vuelo] += 1 

      if (delay_filter != 'NA' and int(delay_filter) > 15):

        filtro_año[mes][dia_del_mes][0][tiempo_de_vuelo] += 1                 # Cuento la cantidad de datos por hora
        filtro_año[mes][dia_del_mes][1][tiempo_de_vuelo] += int(delay_filter) # Cuento la cantidad de datos por hora
        filtro_año[mes][dia_del_mes][2]                  = dia_de_semana      # Sumo todos los datos del dia
        filtro_año[mes][dia_del_mes][3]                  = dia_del_mes        # Guardo el dia de semana para el gráfico


    for i in range(0, 12):
      for j in range(0, 31):
        for k in range(0, 24):
          if año[i][j][0][k] != 0:
            año[i][j][1][k] /= float(año[i][j][0][k])                       # Divido la sumatoria de delays por la cantidad de delays

          if vuelos_por_dia[i][j][k] != 0:
            año[i][j][0][k] /= float(vuelos_por_dia[i][j][k])               # Divido la cantidad de delays por la cantidad de vuelos en el dia

          if filtro_año[i][j][0][k] != 0:
            filtro_año[i][j][1][k] /= float(filtro_año[i][j][0][k])         # Divido la sumatoria de delays por la cantidad de delays

          if vuelos_por_dia_filtro[i][j][k] != 0:
            filtro_año[i][j][0][k] /= float(vuelos_por_dia_filtro[i][j][k]) # Divido la cantidad de delays por la cantidad de vuelos en el dia


def graficarDiaDelay(directory, airport, data):

# Instancio los arreglos para los datos

  año_1998 = [[[[0 for k in range(0, 24)], [0 for z in range(0, 24)], 0, 0] for i in range(0, 31)] for j in range(0,12)]  
  año_1999 = [[[[0 for k in range(0, 24)], [0 for z in range(0, 24)], 0, 0] for i in range(0, 31)] for j in range(0,12)]
  año_2000 = [[[[0 for k in range(0, 24)], [0 for z in range(0, 24)], 0, 0] for i in range(0, 31)] for j in range(0,12)]
  año_2001 = [[[[0 for k in range(0, 24)], [0 for z in range(0, 24)], 0, 0] for i in range(0, 31)] for j in range(0,12)]
  año_2002 = [[[[0 for k in range(0, 24)], [0 for z in range(0, 24)], 0, 0] for i in range(0, 31)] for j in range(0,12)]
  año_2003 = [[[[0 for k in range(0, 24)], [0 for z in range(0, 24)], 0, 0] for i in range(0, 31)] for j in range(0,12)]
  año_2004 = [[[[0 for k in range(0, 24)], [0 for z in range(0, 24)], 0, 0] for i in range(0, 31)] for j in range(0,12)]
  año_2005 = [[[[0 for k in range(0, 24)], [0 for z in range(0, 24)], 0, 0] for i in range(0, 31)] for j in range(0,12)]
  año_2006 = [[[[0 for k in range(0, 24)], [0 for z in range(0, 24)], 0, 0] for i in range(0, 31)] for j in range(0,12)]
  año_2007 = [[[[0 for k in range(0, 24)], [0 for z in range(0, 24)], 0, 0] for i in range(0, 31)] for j in range(0,12)]
  año_2008 = [[[[0 for k in range(0, 24)], [0 for z in range(0, 24)], 0, 0] for i in range(0, 31)] for j in range(0,12)]

  filtro_año_1998 = [[[0, [0 for z in range(0, 24)], 0] for i in range(0, 31)] for j in range(0,12)]  
  filtro_año_1999 = [[[0, [0 for z in range(0, 24)], 0] for i in range(0, 31)] for j in range(0,12)]
  filtro_año_2000 = [[[0, [0 for z in range(0, 24)], 0] for i in range(0, 31)] for j in range(0,12)]
  filtro_año_2001 = [[[0, [0 for z in range(0, 24)], 0] for i in range(0, 31)] for j in range(0,12)]
  filtro_año_2002 = [[[0, [0 for z in range(0, 24)], 0] for i in range(0, 31)] for j in range(0,12)]
  filtro_año_2003 = [[[0, [0 for z in range(0, 24)], 0] for i in range(0, 31)] for j in range(0,12)]
  filtro_año_2004 = [[[0, [0 for z in range(0, 24)], 0] for i in range(0, 31)] for j in range(0,12)]
  filtro_año_2005 = [[[0, [0 for z in range(0, 24)], 0] for i in range(0, 31)] for j in range(0,12)]
  filtro_año_2006 = [[[0, [0 for z in range(0, 24)], 0] for i in range(0, 31)] for j in range(0,12)]
  filtro_año_2007 = [[[0, [0 for z in range(0, 24)], 0] for i in range(0, 31)] for j in range(0,12)]
  filtro_año_2008 = [[[0, [0 for z in range(0, 24)], 0] for i in range(0, 31)] for j in range(0,12)]

  file_out = directory + '/' + airport
  print file_out

  readFile(file_out + '1998.csv', año_1998, filtro_año_1998, data)
  readFile(file_out + '1999.csv', año_1998, filtro_año_1999, data)
  readFile(file_out + '2000.csv', año_1998, filtro_año_2000, data)
  readFile(file_out + '2001.csv', año_1998, filtro_año_2001, data)
  readFile(file_out + '2002.csv', año_1998, filtro_año_2002, data)
  readFile(file_out + '2003.csv', año_1998, filtro_año_2003, data)
  readFile(file_out + '2004.csv', año_1998, filtro_año_2004, data)
  readFile(file_out + '2005.csv', año_2005, filtro_año_2005, data)
  readFile(file_out + '2006.csv', año_2006, filtro_año_2006, data)
  readFile(file_out + '2007.csv', año_2007, filtro_año_2007, data)
  readFile(file_out + '2008.csv', año_2008, filtro_año_2008, data)

  x_lunes     = [] 
  x_martes    = [] 
  x_miercoles = []   
  x_jueves    = [] 
  x_viernes   = [] 
  x_sabado    = [] 
  x_domingo   = [] 

  lunes_2005     = [] 
  martes_2005    = [] 
  miercoles_2005 = []   
  jueves_2005    = [] 
  viernes_2005   = [] 
  sabado_2005    = [] 
  domingo_2005   = [] 

  #print anio_2005

  for i in range(0, 12):
    mes = año_2005[i]
    for day in mes:
      data = day[0]
      
      if day[1] == 1:
        lunes_2005.append(data)
        x_lunes.append(day[2]+31*i)

      elif day[1] == 2:
        martes_2005.append(data)
        x_martes.append(day[2]+31*i)

      elif day[1] == 3:
        miercoles_2005.append(data)
        x_miercoles.append(day[2]+31*i)

      elif day[1] == 4:
        jueves_2005.append(data)
        x_jueves.append(day[2]+31*i)

      elif day[1] == 5:
        viernes_2005.append(data)
        x_viernes.append(day[2]+31*i)

      elif day[1] == 6:
        sabado_2005.append(data)
        x_sabado.append(day[2]+31*i)

      elif day[1] == 7:
        domingo_2005.append(data)
        x_domingo.append(day[2]+31*i)

  if not os.path.exists(directory + '/graficos'):
    os.mkdir(directory + '/graficos')

  opacity = 0.4

  years=12
# Debería haber cantidad de anios-1 
  for i in range(1, years):
    plt.axvline(x=31*i, linewidth=2, color='k')

  plt.plot(x_lunes, lunes_2005, 'ro', 
           alpha=opacity,
           color='b',
           linestyle='-',
           label=u"Lunes")

  plt.plot(x_martes, martes_2005, 'ro', 
           alpha=opacity,
           color='g',
           linestyle='-',
           label=u"Martes")

  plt.plot(x_miercoles, miercoles_2005, 'ro', 
           alpha=opacity,
           color='r',
           linestyle='-',
           label=u"Miercoles")

  plt.plot(x_jueves, jueves_2005, 'ro', 
           alpha=opacity,
           color='c',
           linestyle='-',
           label=u"Jueves")

  plt.plot(x_viernes, viernes_2005, 'ro', 
           alpha=opacity,
           color='m',
           linestyle='-',
           label=u"Viernes")

  plt.plot(x_sabado, sabado_2005, 'ro', 
           alpha=opacity,
           color='y',
           linestyle='-',
           label=u"Sabado")

  plt.plot(x_domingo, domingo_2005, 'ro', 
           alpha=opacity,
           color='k',
           linestyle='-',
           label=u"Domingo")

  plt.xlabel(u"dias")
  plt.ylabel(u"Cantidad de delays")
  plt.xticks([15+31*i for i in range(0,years)],['Ene', 'feb', 'mar', 'abr', 'may', 'jun', 'jul', 'ago', 'sep', 'oct', 'nov', 'dic'],fontsize=10)
  plt.legend()
  plt.savefig(directory + '/graficos/grafico_cantidad_delay_semana')
  plt.show()

if __name__ == "__main__":
  main()
