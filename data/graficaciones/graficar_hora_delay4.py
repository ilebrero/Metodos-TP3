#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
from graficaciones.graficar_cuadrados_minimos import calcularCML
import matplotlib.pyplot as plt
from math import log
import os

#para CML: función utilizada para aproximar
def func(x, b, c):
  return np.abs(np.sin(x + c) + np.cos(x + b))

#def func(x, a, b):
 # return a*np.sin(x()) + b

#def func2(x, b):
#  return np.abs(0.7 * np.sin(x/float(10)) * np.cos(x/float(10))) + b

#función utilizada para calcular promedios
def func_prom(data, data_filter, amount):
  for i in range(0, 12):
    for k in range(0, 24):

      if amount[i] != 0:
        data[i][0][k] /= float(amount[i]) 
        data[i][1][k] /= float(amount[i]) 
        data_filter[i][0][k] /= float(amount[i])
        data_filter[i][1][k] /= float(amount[i])

##directory = directorio donde se crearán archivos con resultados
##airport = aeropuerto 
##an = año 
##delay_filter = por qué delay filtrar
##data = la información que se quiere obtener

def readFile(File, anio, filtro_anio, data, d_filter):

  vuelos_por_dia =        [[[0 for k in range(0, 24)] for i in range(0, 31)] for j in range(0, 12)] #arreglo de dimensión 24(horas)*31(días)*12(meses)
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

      if tiempo_de_vuelo != 'NA': #cuento sólo si tengo datos
        if len(tiempo_de_vuelo) == 4:
          tiempo_de_vuelo = int(tiempo_de_vuelo[:2]) # Extrae los 2 primeros caracteres 

        elif len(tiempo_de_vuelo) == 3:
          tiempo_de_vuelo = int(tiempo_de_vuelo[:1]) # Extrae el primer caracter

        elif len(tiempo_de_vuelo) <= 2:
          tiempo_de_vuelo = 0                        # Es 00 y un numerito por ende es la primer posicion 

        if (delay != 'NA'):
          vuelos_por_dia[mes][dia_del_mes][tiempo_de_vuelo] += 1 

        if (delay != 'NA' and int(delay) > 15):
        #if (delay != 'NA' and int(delay) < 15):

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
            anio[i][j][0][k] /= float(vuelos_por_dia[i][j][k])               # Divido la cantidad de delays por la cantidad de vuelos en el dia en horario k

          if filtro_anio[i][j][0][k] != 0:
            filtro_anio[i][j][1][k] /= float(filtro_anio[i][j][0][k])         # Divido la sumatoria de delays por la cantidad de delays

          if vuelos_por_dia_filtro[i][j][k] != 0:
            filtro_anio[i][j][0][k] /= float(vuelos_por_dia_filtro[i][j][k]) # Divido la cantidad de delays por la cantidad de vuelos en el dia

#directory = directorio donde se crearán archivos con resultados
#airport = aeropuerto 
#an = año 
#delay_filter = por qué delay filtrar
#data = la información que se quiere obtener

def graficarHoraDelay4(directory, airport, an, delay_filter, data):
#requiere primer_anio <= ultimo_anio y primer_anio >= 2000  
  primer_anio = 5
  ultimo_anio = 5
        
# Instancio los arreglos para los datos, del 2005 al 2008
  anio_lunes     = [[[[[0 for k in range(0, 24)], [0 for z in range(0, 24)], 0, 0] for i in range(0, 31)] for j in range(0,12)] for q in range(0, ultimo_anio - primer_anio + 1)]
  anio_martes    = [[[[[0 for k in range(0, 24)], [0 for z in range(0, 24)], 0, 0] for i in range(0, 31)] for j in range(0,12)] for q in range(0, ultimo_anio - primer_anio + 1)]
  anio_miercoles = [[[[[0 for k in range(0, 24)], [0 for z in range(0, 24)], 0, 0] for i in range(0, 31)] for j in range(0,12)] for q in range(0, ultimo_anio - primer_anio + 1)]
  anio_jueves    = [[[[[0 for k in range(0, 24)], [0 for z in range(0, 24)], 0, 0] for i in range(0, 31)] for j in range(0,12)] for q in range(0, ultimo_anio - primer_anio + 1)]
  anio_viernes   = [[[[[0 for k in range(0, 24)], [0 for z in range(0, 24)], 0, 0] for i in range(0, 31)] for j in range(0,12)] for q in range(0, ultimo_anio - primer_anio + 1)]
  anio_sabado    = [[[[[0 for k in range(0, 24)], [0 for z in range(0, 24)], 0, 0] for i in range(0, 31)] for j in range(0,12)] for q in range(0, ultimo_anio - primer_anio + 1)]
  anio_domingo   = [[[[[0 for k in range(0, 24)], [0 for z in range(0, 24)], 0, 0] for i in range(0, 31)] for j in range(0,12)] for q in range(0, ultimo_anio - primer_anio + 1)]

  for l in range(primer_anio, ultimo_anio + 1):

    filtro_anio = [[[[0 for k in range(0, 24)], [0 for z in range(0, 24)], 0, 0] for i in range(0, 31)] for j in range(0,12)]
    anio        = [[[[0 for k in range(0, 24)], [0 for z in range(0, 24)], 0, 0] for i in range(0, 31)] for j in range(0,12)]

    file_out = directory + '/' + airport + "200"+ str(l) + '.csv'
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
        
        #acumulo la cantidad de días en un mes que son lu-ma-mi-ju-vi-sa-do 
        if day[2] == 1:
          cant_lunes[i] += 1
        elif day[2] == 2:
          cant_martes[i] += 1
        elif day[2] == 3:
          cant_miercoles[i] += 1
        elif day[2] == 4:
          cant_jueves[i] += 1
        elif day[2] == 5:
          cant_viernes[i] += 1
        elif day[2] == 6:
          cant_sabado[i] += 1
        elif day[2] == 7:
          cant_domingo[i] += 1

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

          elif day[2] == 2:
            martes[i][0][k] += cant_datos # Le meto en la primer posicion la cantidad de datos
            martes[i][1][k] += datos # Le meto en la segunda posicion la suma de los daots
            filtro_martes[i][0][k] += filtro_cant_datos
            filtro_martes[i][1][k] += filtro_datos

          elif day[2] == 3:
            miercoles[i][0][k] += cant_datos # Le meto en la primer posicion la cantidad de datos
            miercoles[i][1][k] += datos # Le meto en la segunda posicion la suma de los daots
            filtro_miercoles[i][0][k] += filtro_cant_datos
            filtro_miercoles[i][1][k] += filtro_datos

          elif day[2] == 4:
            jueves[i][0][k] += cant_datos # Le meto en la primer posicion la cantidad de datos
            jueves[i][1][k] += datos # Le meto en la segunda posicion la suma de los daots
            filtro_jueves[i][0][k] += filtro_cant_datos
            filtro_jueves[i][1][k] += filtro_datos

          elif day[2] == 5:
            viernes[i][0][k] += cant_datos # Le meto en la primer posicion la cantidad de datos
            viernes[i][1][k] += datos # Le meto en la segunda posicion la suma de los daots
            filtro_viernes[i][0][k] += filtro_cant_datos
            filtro_viernes[i][1][k] += filtro_datos

          elif day[2] == 6:
            sabado[i][0][k] += cant_datos # Le meto en la primer posicion la cantidad de datos
            sabado[i][1][k] += datos # Le meto en la segunda posicion la suma de los daots
            filtro_sabado[i][0][k] += filtro_cant_datos
            filtro_sabado[i][1][k] += filtro_datos

          elif day[2] == 7:
            domingo[i][0][k] += cant_datos # Le meto en la primer posicion la cantidad de datos
            domingo[i][1][k] += datos # Le meto en la segunda posicion la suma de los daots
            filtro_domingo[i][0][k] += filtro_cant_datos
            filtro_domingo[i][1][k] += filtro_datos

    # Sacar el promedio por mes
    func_prom(lunes, filtro_lunes, cant_lunes)
    func_prom(martes, filtro_martes, cant_martes)
    func_prom(miercoles, filtro_miercoles, cant_miercoles)
    func_prom(jueves, filtro_jueves, cant_jueves)
    func_prom(viernes, filtro_viernes, cant_viernes)
    func_prom(sabado, filtro_sabado, cant_sabado)
    func_prom(domingo, filtro_domingo, cant_domingo)

    #guardo los datos de un año y vuelvo a iterar
    anio_lunes[l - primer_anio] = lunes
    anio_martes[l - primer_anio] = martes
    anio_miercoles[l - primer_anio] = miercoles
    anio_jueves[l - primer_anio] = jueves
    anio_viernes[l - primer_anio] = viernes
    anio_sabado[l - primer_anio] = sabado
    anio_domingo[l - primer_anio] = domingo


  # El promedio de cada hora por anio.
  # Total de valores 24.

  # El promedio de cada hora por anio dentro de todos los anios

  if not os.path.exists(directory + '/graficos'):
    os.mkdir(directory + '/graficos')

# NO HICE NINGUNA CARPETA PARTICULAR PARA CML, NI IDEA SI ESTA MAL O QUE, SOY JES        
#  if not os.path.exists(directory + '/datosparacml'):
#    os.mkdir(directory + '/datosparacml')

# with open(directory + '/datosparacml/' + 'cancelaciones_semana_' + airport, 'w+') as file_out_data:
#     for val in cancelaciones:
#       file_out_data.write(str(val) + '\n')
  

  dias_grafico = ['lu', 'ma', 'mi', 'ju', 'vi', 'sa', 'do']
  dias = ['lunes', 'martes', 'miercoles', 'jueves', 'viernes', 'sabado', 'domingo']
  meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']


  aux = 0
  #inicializo dict eje_x con 24 horas para cada dia de la semana para cada anio entre ultimo_anio y primer_anio 
  eje_x = {}
  eje_x2 = {}
  
  for s in range(0, ultimo_anio - primer_anio + 1):
    aux = 0
    for d in dias:      
      if s == 0:
        eje_x['x_' + d + '_' + str(s)] = [i for i in range(aux, aux+24)]
        eje_x2['x_' + d + '_' + str(s)] = [i for i in range(aux+168, aux+24+168)]
        aux +=24
      else:
        eje_x['x_' + d + '_' + str(s)] = [i for i in range(336+aux, 336+aux+24)]
        eje_x2['x_' + d + '_' + str(s)] = [i for i in range(504+aux, aux+24+504)]
        aux +=24


  opacity = 0.4


  #for j in range(0, 12):
  for j in range(0, 6):

    #inicializo arreglos para CML
    valsX = []
    valsY = []
    
    for h in range(0, ultimo_anio - primer_anio + 1):
    
      for k in range(0, 2*7*(ultimo_anio - primer_anio + 1)):
        plt.axvline(x=24*k, linewidth=1, color='k')
    
      if h == 0:  
    
#       print eje_x['x_lunes_' + str(h)]
        plt.plot(eje_x['x_lunes_' + str(h)], anio_lunes[h][2*j][0], 'ro', 
        alpha=opacity,
        color='b',
        linestyle='-',
        label=u"Lunes")
        valsX += eje_x['x_lunes_' + str(h)]
        valsY += anio_lunes[h][2*j][0]


#       print eje_x['x_martes_' + str(h)]
        plt.plot(eje_x['x_martes_' + str(h)], anio_martes[h][2*j][0], 'ro', 
        alpha=opacity,
        color='g',
        linestyle='-',
        label=u"Martes")
        valsX += eje_x['x_martes_' + str(h)]
        valsY += anio_martes[h][2*j][0]

#       print eje_x['x_miercoles_' + str(h)]
        plt.plot(eje_x['x_miercoles_' + str(h)], anio_miercoles[h][2*j][0], 'ro', 
        alpha=opacity,
        color='r',
        linestyle='-',
        label=u"Miercoles")
        valsX += eje_x['x_miercoles_' + str(h)]
        valsY += anio_miercoles[h][2*j][0]

#       print eje_x['x_jueves_' + str(h)]
        plt.plot(eje_x['x_jueves_' + str(h)], anio_jueves[h][2*j][0], 'ro', 
        alpha=opacity,
        color='c',
        linestyle='-',
        label=u"Jueves")
        valsX += eje_x['x_jueves_' + str(h)]
        valsY += anio_jueves[h][2*j][0]

#       print eje_x['x_martes_' + str(h)]
        plt.plot(eje_x['x_viernes_' + str(h)], anio_viernes[h][2*j][0], 'ro', 
        alpha=opacity,
        color='m',
        linestyle='-',
        label=u"Viernes")
        valsX += eje_x['x_viernes_' + str(h)]
        valsY += anio_viernes[h][2*j][0]

#       print eje_x['x_sabado_' + str(h)]
        plt.plot(eje_x['x_sabado_' + str(h)], anio_sabado[h][2*j][0], 'ro', 
        alpha=opacity,
        color='y',
        linestyle='-',
        label=u"Sabado")
        valsX += eje_x['x_sabado_' + str(h)]
        valsY += anio_sabado[h][2*j][0]

#       print eje_x['x_domingo_' + str(h)]
        plt.plot(eje_x['x_domingo_' + str(h)], anio_domingo[h][2*j][0], 'ro', 
        alpha=opacity,
        color='k',                                                                                                  linestyle='-',
        label=u"Domingo")
        valsX += eje_x['x_domingo_' + str(h)]
        valsY += anio_domingo[h][2*j][0]


        plt.plot(eje_x2['x_lunes_' + str(h)], anio_lunes[h][2*j+1][0], 'ro', 
        alpha=opacity,
        color='b',
        linestyle='-',
        )
        #label=u"Lunes")
        valsX += eje_x2['x_lunes_' + str(h)]
        valsY += anio_lunes[h][2*j+1][0]


#       print eje_x2['x_martes_' + str(h)]
        plt.plot(eje_x2['x_martes_' + str(h)], anio_martes[h][2*j+1][0], 'ro', 
        alpha=opacity,
        color='g',
        linestyle='-',
        )
        #label=u"Martes")
        valsX += eje_x2['x_martes_' + str(h)]
        valsY += anio_martes[h][2*j+1][0]

#       print eje_x2['x_miercoles_' + str(h)]
        plt.plot(eje_x2['x_miercoles_' + str(h)], anio_miercoles[h][2*j+1][0], 'ro', 
        alpha=opacity,
        color='r',
        linestyle='-',
        )
        #label=u"Miercoles")
        valsX += eje_x2['x_miercoles_' + str(h)]
        valsY += anio_miercoles[h][2*j+1][0]

#       print eje_x2['x_jueves_' + str(h)]
        plt.plot(eje_x2['x_jueves_' + str(h)], anio_jueves[h][2*j+1][0], 'ro', 
        alpha=opacity,
        color='c',
        linestyle='-',
        )
        #label=u"Jueves")
        valsX += eje_x2['x_jueves_' + str(h)]
        valsY += anio_jueves[h][2*j+1][0]

#       print eje_x2['x_martes_' + str(h)]
        plt.plot(eje_x2['x_viernes_' + str(h)], anio_viernes[h][2*j+1][0], 'ro', 
        alpha=opacity,
        color='m',
        linestyle='-',
        )
        #label=u"Viernes")
        valsX += eje_x2['x_viernes_' + str(h)]
        valsY += anio_viernes[h][2*j+1][0]

#       print eje_x2['x_sabado_' + str(h)]
        plt.plot(eje_x2['x_sabado_' + str(h)], anio_sabado[h][2*j+1][0], 'ro', 
        alpha=opacity,
        color='y',
        linestyle='-',
        )
        #label=u"Sabado")
        valsX += eje_x2['x_sabado_' + str(h)]
        valsY += anio_sabado[h][2*j+1][0]

#       print eje_x2['x_domingo_' + str(h)]
        plt.plot(eje_x2['x_domingo_' + str(h)], anio_domingo[h][2*j+1][0], 'ro', 
        alpha=opacity,
        color='k',                                                                                                  linestyle='-',
        )
        #label=u"Domingo")
        valsX += eje_x2['x_domingo_' + str(h)]
        valsY += anio_domingo[h][2*j+1][0]


      else:

#       print eje_x['x_lunes_' + str(h)]
        plt.plot(eje_x['x_lunes_' + str(h)], anio_lunes[h][2*j][0], 'ro', 
        alpha=opacity,
        color='b',
        linestyle='-')
        valsX += eje_x['x_lunes_' + str(h)]
        valsY += anio_lunes[h][2*j][0]


#       print eje_x['x_martes_' + str(h)]
        plt.plot(eje_x['x_martes_' + str(h)], anio_martes[h][2*j][0], 'ro', 
        alpha=opacity,
        color='g',
        linestyle='-')
        valsX += eje_x['x_martes_' + str(h)]
        valsY += anio_martes[h][2*j][0]

#       print eje_x['x_miercoles_' + str(h)]
        plt.plot(eje_x['x_miercoles_' + str(h)], anio_miercoles[h][2*j][0], 'ro', 
        alpha=opacity,
        color='r',
        linestyle='-')
        valsX += eje_x['x_miercoles_' + str(h)]
        valsY += anio_miercoles[h][2*j][0]

#       print eje_x['x_jueves_' + str(h)]
        plt.plot(eje_x['x_jueves_' + str(h)], anio_jueves[h][2*j][0], 'ro', 
        alpha=opacity,
        color='c',
        linestyle='-')
        valsX += eje_x['x_jueves_' + str(h)]
        valsY += anio_jueves[h][2*j][0]

#       print eje_x['x_martes_' + str(h)]
        plt.plot(eje_x['x_viernes_' + str(h)], anio_viernes[h][2*j][0], 'ro', 
        alpha=opacity,
        color='m',
        linestyle='-')
        valsX += eje_x['x_viernes_' + str(h)]
        valsY += anio_viernes[h][2*j][0]

#       print eje_x['x_sabado_' + str(h)]
        plt.plot(eje_x['x_sabado_' + str(h)], anio_sabado[h][2*j][0], 'ro', 
        alpha=opacity,
        color='y',
        linestyle='-')
        valsX += eje_x['x_sabado_' + str(h)]
        valsY += anio_sabado[h][2*j][0]

#       print eje_x['x_domingo_' + str(h)]
        plt.plot(eje_x['x_domingo_' + str(h)], anio_domingo[h][2*j][0], 'ro', 
        alpha=opacity,
        color='k',                                                                                                  linestyle='-')
        valsX += eje_x['x_domingo_' + str(h)]
        valsY += anio_domingo[h][2*j][0]


#       print eje_x2['x_lunes_' + str(h)]
        print eje_x['x_lunes_' + str(h)]
        print eje_x2['x_lunes_' + str(h)]
        plt.plot(eje_x2['x_lunes_' + str(h)], anio_lunes[h][2*j+1][0], 'ro', 
        alpha=opacity,
        color='b',
        linestyle='-')
        valsX += eje_x2['x_lunes_' + str(h)]
        valsY += anio_lunes[h][2*j+1][0]


#       print eje_x2['x_martes_' + str(h)]
        plt.plot(eje_x2['x_martes_' + str(h)], anio_martes[h][2*j+1][0], 'ro', 
        alpha=opacity,
        color='g',
        linestyle='-')
        valsX += eje_x2['x_martes_' + str(h)]
        valsY += anio_martes[h][2*j+1][0]

#       print eje_x2['x_miercoles_' + str(h)]
        plt.plot(eje_x2['x_miercoles_' + str(h)], anio_miercoles[h][2*j+1][0], 'ro', 
        alpha=opacity,
        color='r',
        linestyle='-')
        valsX += eje_x2['x_miercoles_' + str(h)]
        valsY += anio_miercoles[h][2*j+1][0]

#       print eje_x2['x_jueves_' + str(h)]
        plt.plot(eje_x2['x_jueves_' + str(h)], anio_jueves[h][2*j+1][0], 'ro', 
        alpha=opacity,
        color='c',
        linestyle='-')
        valsX += eje_x2['x_jueves_' + str(h)]
        valsY += anio_jueves[h][2*j+1][0]

#       print eje_x2['x_martes_' + str(h)]
        plt.plot(eje_x2['x_viernes_' + str(h)], anio_viernes[h][2*j+1][0], 'ro', 
        alpha=opacity,
        color='m',
        linestyle='-')
        valsX += eje_x2['x_viernes_' + str(h)]
        valsY += anio_viernes[h][2*j+1][0]

#       print eje_x2['x_sabado_' + str(h)]
        plt.plot(eje_x2['x_sabado_' + str(h)], anio_sabado[h][2*j+1][0], 'ro', 
        alpha=opacity,
        color='y',
        linestyle='-')
        valsX += eje_x2['x_sabado_' + str(h)]
        valsY += anio_sabado[h][2*j+1][0]

#       print eje_x2['x_domingo_' + str(h)]
        plt.plot(eje_x2['x_domingo_' + str(h)], anio_domingo[h][2*j+1][0], 'ro', 
        alpha=opacity,
        color='k',                                                                                                  linestyle='-')
        valsX += eje_x2['x_domingo_' + str(h)]
        valsY += anio_domingo[h][2*j+1][0]


    
    plt.xlabel(u"días")
    plt.ylabel(u"Cantidad de delays de " + meses[j])
    labels = [dias_grafico[i % 7] for i in range(0, 2*(ultimo_anio - primer_anio + 1)*7)] 
    plt.xticks([12+24*j for j in range(0, 2*(ultimo_anio - primer_anio + 1)*7)],labels,fontsize=10)

    #CML
    valsEstimacion = []
    param = calcularCML(valsX, valsY, func)
    for i in range(0, len(valsX)):
      valsEstimacion.append(func(i, param[0], param[1]))

    #plt.plot(valsX, valsEstimacion, 'ro', alpha=opacity, linestyle='-', color='g')    

    plt.legend(bbox_to_anchor=(0.96, 1), prop={'size': 10})
    plt.savefig(directory + '/graficos/grafico_cantidad_delay_hora')
    plt.show()


if __name__ == "__main__":
  main()