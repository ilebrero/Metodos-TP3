#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from math import log
import os

def func(data, data_filter, amount):
  for i in range(0, 12):
    for k in range(0, 24):

      if amount[i] != 0:
        data[i][0][k] /= float(amount[i]) 
        data[i][1][k] /= float(amount[i]) 
        data_filter[i][0][k] /= float(amount[i])
        data_filter[i][1][k] /= float(amount[i])

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

      # ESTOY CALCULANDO MAL EL TIEMPO DE VUELO. DEBERIA SER UN ENTERO ENTRE [0..23],  
      # TIEMPO DE VUELO = HORARIO DE VUELO

      if len(tiempo_de_vuelo) == 4:
        tiempo_de_vuelo = int(tiempo_de_vuelo[:2]) # Le saco los primeros dos caracteres

      elif len(tiempo_de_vuelo) == 3:
        tiempo_de_vuelo = int(tiempo_de_vuelo[:1]) # Le saco primer caracter

      elif len(tiempo_de_vuelo) <= 2:
        tiempo_de_vuelo = 0                        # Es 00 y un numerito por ende es la primer posicion 

      print tiempo_de_vuelo

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


def graficarHoraDelay2(directory, airport, an, delay_filter, data):

# Instancio los arreglos para los datos

  anio = [[[[0 for k in range(0, 24)], [0 for z in range(0, 24)], 0, 0] for i in range(0, 31)] for j in range(0,12)]

  filtro_anio = [[[[0 for k in range(0, 24)], [0 for z in range(0, 24)], 0, 0] for i in range(0, 31)] for j in range(0,12)]

  file_out = directory + '/' + airport + an + '.csv'
  print file_out

  readFile(file_out, anio, filtro_anio, data, delay_filter)

  # Instancio una lista vacia por cada mes de cada anio
  # Por cada mes quiero tener la cantidad de datos y los datos por dia 
  # lunes[mes][0] = Cantidad de delays por dia (por hora) 
  # lunes[mes][1] = Sumatoria de delays por dia (por hora) 
  
  lunes     = [ [ [0 for z in range(0, 24)], [0 for k in range(0, 24)] ] for j in range(0, 12)]
  martes    = [ [ [0 for z in range(0, 24)], [0 for k in range(0, 24)] ] for j in range(0, 12)]
  miercoles = [ [ [0 for z in range(0, 24)], [0 for k in range(0, 24)] ] for j in range(0, 12)]
  jueves    = [ [ [0 for z in range(0, 24)], [0 for k in range(0, 24)] ] for j in range(0, 12)]
  viernes   = [ [ [0 for z in range(0, 24)], [0 for k in range(0, 24)] ] for j in range(0, 12)]
  sabado    = [ [ [0 for z in range(0, 24)], [0 for k in range(0, 24)] ] for j in range(0, 12)]
  domingo   = [ [ [0 for z in range(0, 24)], [0 for k in range(0, 24)] ] for j in range(0, 12)]

  # Esto debería ser por la cantidad de lunes del mes. ESTO ahora esta haciendolo por hora (creo)
  cant_lunes     = [0 for i in range(0, 12)] 
  cant_martes    = [0 for i in range(0, 12)] 
  cant_miercoles = [0 for i in range(0, 12)]   
  cant_jueves    = [0 for i in range(0, 12)] 
  cant_viernes   = [0 for i in range(0, 12)] 
  cant_sabado    = [0 for i in range(0, 12)] 
  cant_domingo   = [0 for i in range(0, 12)] 

  filtro_lunes     = [ [ [0 for z in range(0, 24)], [0 for k in range(0, 24)] ] for j in range(0, 12)]
  filtro_martes    = [ [ [0 for z in range(0, 24)], [0 for k in range(0, 24)] ] for j in range(0, 12)]
  filtro_miercoles = [ [ [0 for z in range(0, 24)], [0 for k in range(0, 24)] ] for j in range(0, 12)]  
  filtro_jueves    = [ [ [0 for z in range(0, 24)], [0 for k in range(0, 24)] ] for j in range(0, 12)]
  filtro_viernes   = [ [ [0 for z in range(0, 24)], [0 for k in range(0, 24)] ] for j in range(0, 12)]
  filtro_sabado    = [ [ [0 for z in range(0, 24)], [0 for k in range(0, 24)] ] for j in range(0, 12)]
  filtro_domingo   = [ [ [0 for z in range(0, 24)], [0 for k in range(0, 24)] ] for j in range(0, 12)]

  # Por cada mes
  for i in range(0, 12):
    mes = anio[i]
    filtro_mes = filtro_anio[i]

    # Por cada dia del mes
    for j in range(0, 31):
      day = mes[j]
      filtro_day = filtro_mes[j]

      # Por cada hora
      for k in range(0, 24):

        # Levanto la acumulada en la hora (dia y mes ya están fijos)
        cant_datos = day[0][k]
        datos = day[1][k]

        filtro_cant_datos = filtro_day[0][k]
        filtro_datos = filtro_day[1][k]
        
        # Dependiendo del día de semana(lun-dom) acumulo los datos
        # Ejemplo: Al lunes del mes i, en la hora k le acumulo los datos
        # Promedio de todos los lunes del mes
        if day[2] == 1:
          lunes[i][0][k] += cant_datos      # Le meto en la primer posicion la cantidad de datos
          lunes[i][1][k] += datos           # Le meto en la segunda posicion la suma de los daots
          filtro_lunes[i][0][k] += filtro_cant_datos
          filtro_lunes[i][1][k] += filtro_datos

          # ESTO ME PARECE QUE ESTOY SUMANDO POR HORA EN VEZ DE POR DIA

          cant_lunes[i] += 1 # Le meto en la primer posicion la cantidad de datos

        elif day[2] == 2:
          martes[i][0][k] += cant_datos # Le meto en la primer posicion la cantidad de datos
          martes[i][1][k] += datos # Le meto en la segunda posicion la suma de los daots
          filtro_martes[i][0][k] += filtro_cant_datos
          filtro_martes[i][1][k] += filtro_datos

          cant_martes[i] += 1 # Le meto en la primer posicion la cantidad de datos

        elif day[2] == 3:
          miercoles[i][0][k] += cant_datos # Le meto en la primer posicion la cantidad de datos
          miercoles[i][1][k] += datos # Le meto en la segunda posicion la suma de los daots
          filtro_miercoles[i][0][k] += filtro_cant_datos
          filtro_miercoles[i][1][k] += filtro_datos

          cant_miercoles[i] += 1 # Le meto en la primer posicion la cantidad de datos

        elif day[2] == 4:
          jueves[i][0][k] += cant_datos # Le meto en la primer posicion la cantidad de datos
          jueves[i][1][k] += datos # Le meto en la segunda posicion la suma de los daots
          filtro_jueves[i][0][k] += filtro_cant_datos
          filtro_jueves[i][1][k] += filtro_datos

          cant_jueves[i] += 1 # Le meto en la primer posicion la cantidad de datos

        elif day[2] == 5:
          viernes[i][0][k] += cant_datos # Le meto en la primer posicion la cantidad de datos
          viernes[i][1][k] += datos # Le meto en la segunda posicion la suma de los daots
          filtro_viernes[i][0][k] += filtro_cant_datos
          filtro_viernes[i][1][k] += filtro_datos

          cant_viernes[i] += 1 # Le meto en la primer posicion la cantidad de datos

        elif day[2] == 6:
          sabado[i][0][k] += cant_datos # Le meto en la primer posicion la cantidad de datos
          sabado[i][1][k] += datos # Le meto en la segunda posicion la suma de los daots
          filtro_sabado[i][0][k] += filtro_cant_datos
          filtro_sabado[i][1][k] += filtro_datos

          cant_sabado[i] += 1 # Le meto en la primer posicion la cantidad de datos

        elif day[2] == 7:
          domingo[i][0][k] += cant_datos # Le meto en la primer posicion la cantidad de datos
          domingo[i][1][k] += datos # Le meto en la segunda posicion la suma de los daots
          filtro_domingo[i][0][k] += filtro_cant_datos
          filtro_domingo[i][1][k] += filtro_datos

          cant_domingo[i] += 1 # Le meto en la primer posicion la cantidad de datos

  print "printeando"
  print lunes[0]

  # Sacar el promedio por mes
  func(lunes, filtro_lunes, cant_lunes)
  func(martes, filtro_martes, cant_martes)
  func(miercoles, filtro_miercoles, cant_miercoles)
  func(jueves, filtro_jueves, cant_jueves)
  func(viernes, filtro_viernes, cant_viernes)
  func(sabado, filtro_sabado, cant_sabado)
  func(domingo, filtro_domingo, cant_domingo)


  # El promedio de cada hora por anio.
  # Total de valores 24.

  # El promedio de cada hora por anio dentro de todos los anios

  if not os.path.exists(directory + '/graficos'):
    os.mkdir(directory + '/graficos')

  # lunes[mes][0][hora] Tengo la acumulada de cantidad de delays por mes
  # lunes[mes][1][hora] Tengo la acumulada de delays por mes

  x_lunes     = [i for i in range(0, 24)] 
  x_martes    = [i for i in range(24, 48)] 
  x_miercoles = [i for i in range(48, 72)]   
  x_jueves    = [i for i in range(72, 96)] 
  x_viernes   = [i for i in range(96, 120)] 
  x_sabado    = [i for i in range(120, 144)] 
  x_domingo   = [i for i in range(144, 168)] 

  print lunes[0][0][0]

  opacity = 0.4

  years=11

  for j in range(0, 12):

    for k in range(0, 7):
      plt.axvline(x=24*k, linewidth=2, color='k')

    plt.plot(x_lunes, lunes[j][0], 'ro', 
             alpha=opacity,
             color='b',
             linestyle='-',
             label=u"Lunes")

    plt.plot(x_martes, martes[j][0], 'ro', 
             alpha=opacity,
             color='g',
             linestyle='-',
             label=u"Martes")

    plt.plot(x_miercoles, miercoles[j][0], 'ro', 
             alpha=opacity,
             color='r',
             linestyle='-',
             label=u"Miercoles")

    plt.plot(x_jueves, jueves[j][0], 'ro', 
             alpha=opacity,
             color='c',
             linestyle='-',
             label=u"Jueves")

    plt.plot(x_viernes, viernes[j][0], 'ro', 
             alpha=opacity,
             color='m',
             linestyle='-',
             label=u"Viernes")

    plt.plot(x_sabado, sabado[j][0], 'ro', 
             alpha=opacity,
             color='y',
             linestyle='-',
             label=u"Sabado")

    plt.plot(x_domingo, domingo[j][0], 'ro', 
             alpha=opacity,
             color='k',
             linestyle='-',
             label=u"Domingo")

    plt.xlabel(u"dias")
    plt.ylabel(u"Cantidad de delays")
    plt.xticks([12+24*j for j in range(0,7)],['Lun', 'mar', 'mier', 'juev', 'vier', 'sab', 'dom'],fontsize=10)
    plt.legend()
    plt.savefig(directory + '/graficos/grafico_cantidad_delay_hora')
    plt.show()

if __name__ == "__main__":
  main()
