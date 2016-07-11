#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
from graficaciones.graficar_cuadrados_minimos import calcularCML
import matplotlib.pyplot as plt
from math import log
import os

#para CML: función utilizada para aproximar
def func(x, b, c, d):
  #return b*np.abs(np.sin(0.5*np.pi*x)) + c*np.abs(np.cos(x))
  return b*x*x*x + c*x*x + d*np.abs(np.sin(0.5*np.pi*x))

#def func(x, a, b):
 # return a*np.sin(x()) + b

#def func2(x, b):
#  return np.abs(0.7 * np.sin(x/float(10)) * np.cos(x/float(10))) + b

#def func_intervalos(data_intervalos, data):
#  for i in range(0, 12):
#
#    for k in range(7, 9):
#      data_intervalos[i][0] += data[i][0][k]
#
#    for k in range(9, 11):
#      data_intervalos[i][1] += data[i][0][k]
#
#    for k in range(11, 13):
#      data_intervalos[i][2] += data[i][0][k]
#
#    for k in range(13, 15):
#      data_intervalos[i][3] += data[i][0][k]
#
#    for k in range(15, 17):
#      data_intervalos[i][4] += data[i][0][k]
#
#    for k in range(17, 19):
#      data_intervalos[i][5] += data[i][0][k]
#
#    for k in range(19, 21):
#      data_intervalos[i][6] += data[i][0][k]
#
#    data_intervalos[i][0] /= float(2)
#    data_intervalos[i][1] /= float(2)
#    data_intervalos[i][2] /= float(2)
#    data_intervalos[i][3] /= float(2)
#    data_intervalos[i][4] /= float(2)
#    data_intervalos[i][5] /= float(2)
#    data_intervalos[i][6] /= float(2)

def func_intervalos(data_intervalos, data):
  for i in range(0, 12):

    for k in range(7, 22):
      data_intervalos[i][k-7] = data[i][0][k]

#función utilizada para calcular promedios
def func_prom(data, data_filter, amount):
  for i in range(0, 12):
    for k in range(0, 24):

      if amount[i] != 0:
        data[i][0][k] /= float(amount[i]) 
        data[i][1][k] /= float(amount[i]) 
        data_filter[i][0][k] /= float(amount[i])
        data_filter[i][1][k] /= float(amount[i])

def media_podada(data, cant):
  poda = 0.25

  cant_datos_podados = int(len(data) * poda)

  data.sort()

  data_podada = [data[i] for i in range(0, len(data) - cant_datos_podados)]
  #print "con poda"
  #print len(data_podada)

  cant_datos = len(data_podada) / float(cant - cant_datos_podados)

  if cant_datos == 0 and len(data) != 0:
    print "me podo todo"
  return cant_datos

def readFile(File, anio, filtro_anio, data, d_filter):

  vuelos_por_dia = [[[0 for k in range(0, 24)] for i in range(0, 31)] for j in range(0, 12)] #arreglo de dimensión 24(horas)*31(días)*12(meses)
  datos_por_mes  = [[[[] for k in range(0, 24)] for i in range(0, 31)] for j in range(0, 12)]

  with open(File, 'r') as file_:
    for line in file_:
      currentline = line.split(",")
      dia_del_mes = int(currentline[2]) - 1
      dia_de_semana = int(currentline[3])
      mes = int(currentline[1]) - 1
      delay_filter = currentline[d_filter]
      delay = currentline[15]

      tiempo_de_vuelo = currentline[5]
      if int(tiempo_de_vuelo) >= 2300:
        print "haaaaaaaaaaaaaaaaaaaaaay 23"

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

          datos_por_mes[mes][dia_del_mes][tiempo_de_vuelo].append(int(delay))
          anio[mes][dia_del_mes][2]                  = dia_de_semana  # Sumo todos los datos del dia
          anio[mes][dia_del_mes][3]                  = dia_del_mes    # Guardo el dia de semana para el gráfico

    for i in range(0, 12):
      for j in range(0, 31):
        for k in range(0, 24):

          if vuelos_por_dia[i][j][k] != 0:
            #print "sin podar"
            #print len(datos_por_mes[i][j][k])
            anio[i][j][0][k] = media_podada(datos_por_mes[i][j][k], vuelos_por_dia[i][j][k])

#directory = directorio donde se crearán archivos con resultados
#airport = aeropuerto 
#an = año 
#delay_filter = por qué delay filtrar
#data = la información que se quiere obtener

def graficarPostaIntervalos(directory, airport, an, delay_filter, data):
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

    for a in range(0, 12):
      for b in range(0, 31):
        if anio[a][b][0][23] != 0: #or anio[a][b][0][22]:
          print "hay datos"
    
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

    intervalo_lunes     = [ [0 for z in range(0, 15)] for j in range(0, 12)]
    intervalo_martes    = [ [0 for z in range(0, 15)] for j in range(0, 12)]
    intervalo_miercoles = [ [0 for z in range(0, 15)] for j in range(0, 12)]
    intervalo_jueves    = [ [0 for z in range(0, 15)] for j in range(0, 12)]
    intervalo_viernes   = [ [0 for z in range(0, 15)] for j in range(0, 12)]
    intervalo_sabado    = [ [0 for z in range(0, 15)] for j in range(0, 12)]
    intervalo_domingo   = [ [0 for z in range(0, 15)] for j in range(0, 12)]

    func_intervalos(intervalo_lunes, lunes)
    func_intervalos(intervalo_martes, martes)
    func_intervalos(intervalo_miercoles, miercoles)
    func_intervalos(intervalo_jueves, jueves)
    func_intervalos(intervalo_viernes, viernes)
    func_intervalos(intervalo_sabado, sabado)
    func_intervalos(intervalo_domingo, domingo)


    #guardo los datos de un año y vuelvo a iterar
    anio_lunes[l - primer_anio]     = intervalo_lunes
    anio_martes[l - primer_anio]    = intervalo_martes
    anio_miercoles[l - primer_anio] = intervalo_miercoles
    anio_jueves[l - primer_anio]    = intervalo_jueves
    anio_viernes[l - primer_anio]   = intervalo_viernes
    anio_sabado[l - primer_anio]    = intervalo_sabado
    anio_domingo[l - primer_anio]   = intervalo_domingo


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
  eje_x3 = {}
  
  for s in range(0, ultimo_anio - primer_anio + 1):
    aux = 0
    for d in dias:      
      #eje_x['x_' + d + '_' + str(s)] = [i for i in range(aux, aux+18)]
      #eje_x2['x_' + d + '_' + str(s)] = [i for i in range(aux+126, aux+126+18)]
      #eje_x3['x_' + d + '_' + str(s)] = [i for i in range(aux+252, aux+252+18)]
      #aux +=18
      #eje_x['x_' + d + '_' + str(s)] = [i for i in range(aux, aux+5)]
      #eje_x2['x_' + d + '_' + str(s)] = [i for i in range(aux+35, aux+35+5)]
      #eje_x3['x_' + d + '_' + str(s)] = [i for i in range(aux+70, aux+70+5)]
      #aux +=5
      eje_x['x_' + d + '_' + str(s)] = [i for i in range(aux, aux+15)]
      eje_x2['x_' + d + '_' + str(s)] = [i for i in range(aux+105, aux+105+15)]
      eje_x3['x_' + d + '_' + str(s)] = [i for i in range(aux+210, aux+210+15)]
      aux +=15


  opacity = 0.4


  #for j in range(0, 12):
  #for j in range(0, 4):
  for j in range(1, 2):

    #inicializo arreglos para CML
    valsX = []
    valsY = []
    
    for h in range(0, ultimo_anio - primer_anio + 1):
    
      for k in range(0, 3*7*(ultimo_anio - primer_anio + 1)):
        #plt.axvline(x=18*k, linewidth=1, color='k')
        plt.axvline(x=15*k, linewidth=1, color='k')
    
#     print eje_x['x_lunes_' + str(h)]
      if j == 0:

        print len(anio_lunes[h][11] )
        print len(eje_x['x_lunes_' + str(h)])
        plt.plot(eje_x['x_lunes_' + str(h)], anio_lunes[h][11] , 'ro', 
        alpha=opacity,
        color='b',
        linestyle='-',
        label=u"Lunes")
        valsX += eje_x['x_lunes_' + str(h)]
        valsY += anio_lunes[h][11] 

#       print eje_x['x_martes_' + str(h)]
        plt.plot(eje_x['x_martes_' + str(h)], anio_martes[h][11] , 'ro', 
        alpha=opacity,
        color='g',
        linestyle='-',
        label=u"Martes")
        valsX += eje_x['x_martes_' + str(h)]
        valsY += anio_martes[h][11] 

#       print eje_x['x_miercoles_' + str(h)]
        plt.plot(eje_x['x_miercoles_' + str(h)], anio_miercoles[h][11] , 'ro', 
        alpha=opacity,
        color='r',
        linestyle='-',
        label=u"Miercoles")
        valsX += eje_x['x_miercoles_' + str(h)]
        valsY += anio_miercoles[h][11] 

#       print eje_x['x_jueves_' + str(h)]
        plt.plot(eje_x['x_jueves_' + str(h)], anio_jueves[h][11] , 'ro', 
        alpha=opacity,
        color='c',
        linestyle='-',
        label=u"Jueves")
        valsX += eje_x['x_jueves_' + str(h)]
        valsY += anio_jueves[h][11] 

#       print eje_x['x_martes_' + str(h)]
        plt.plot(eje_x['x_viernes_' + str(h)], anio_viernes[h][11] , 'ro', 
        alpha=opacity,
        color='m',
        linestyle='-',
        label=u"Viernes")
        valsX += eje_x['x_viernes_' + str(h)]
        valsY += anio_viernes[h][11] 

#       print eje_x['x_sabado_' + str(h)]
        plt.plot(eje_x['x_sabado_' + str(h)], anio_sabado[h][11] , 'ro', 
        alpha=opacity,
        color='y',
        linestyle='-',
        label=u"Sabado")
        valsX += eje_x['x_sabado_' + str(h)]
        valsY += anio_sabado[h][11] 

#       print eje_x['x_domingo_' + str(h)]
        plt.plot(eje_x['x_domingo_' + str(h)], anio_domingo[h][11] , 'ro', 
        alpha=opacity,
        color='k',                                                                                                  linestyle='-',
        label=u"Domingo")
        valsX += eje_x['x_domingo_' + str(h)]
        valsY += anio_domingo[h][11] 

        plt.plot(eje_x2['x_lunes_' + str(h)], anio_lunes[h][0], 'ro', 
        alpha=opacity,
        color='b',
        linestyle='-',
        )
        #label=u"Lunes")
        valsX += eje_x2['x_lunes_' + str(h)]
        valsY += anio_lunes[h][0]


#       print eje_x2['x_martes_' + str(h)]
        plt.plot(eje_x2['x_martes_' + str(h)], anio_martes[h][0], 'ro', 
        alpha=opacity,
        color='g',
        linestyle='-',
        )
        #label=u"Martes")
        valsX += eje_x2['x_martes_' + str(h)]
        valsY += anio_martes[h][0]

#       print eje_x2['x_miercoles_' + str(h)]
        plt.plot(eje_x2['x_miercoles_' + str(h)], anio_miercoles[h][0], 'ro', 
        alpha=opacity,
        color='r',
        linestyle='-',
        )
        #label=u"Miercoles")
        valsX += eje_x2['x_miercoles_' + str(h)]
        valsY += anio_miercoles[h][0]

#       print eje_x2['x_jueves_' + str(h)]
        plt.plot(eje_x2['x_jueves_' + str(h)], anio_jueves[h][0], 'ro', 
        alpha=opacity,
        color='c',
        linestyle='-',
        )
        #label=u"Jueves")
        valsX += eje_x2['x_jueves_' + str(h)]
        valsY += anio_jueves[h][0]

#       print eje_x2['x_martes_' + str(h)]
        plt.plot(eje_x2['x_viernes_' + str(h)], anio_viernes[h][0], 'ro', 
        alpha=opacity,
        color='m',
        linestyle='-',
        )
        #label=u"Viernes")
        valsX += eje_x2['x_viernes_' + str(h)]
        valsY += anio_viernes[h][0]

#       print eje_x2['x_sabado_' + str(h)]
        plt.plot(eje_x2['x_sabado_' + str(h)], anio_sabado[h][0], 'ro', 
        alpha=opacity,
        color='y',
        linestyle='-',
        )
        #label=u"Sabado")
        valsX += eje_x2['x_sabado_' + str(h)]
        valsY += anio_sabado[h][0]

#       print eje_x2['x_domingo_' + str(h)]
        plt.plot(eje_x2['x_domingo_' + str(h)], anio_domingo[h][0], 'ro', 
        alpha=opacity,
        color='k',                                                                                                  linestyle='-',
        )
        #label=u"Domingo")
        valsX += eje_x2['x_domingo_' + str(h)]
        valsY += anio_domingo[h][0]
    

        plt.plot(eje_x3['x_lunes_' + str(h)], anio_lunes[h][1] , 'ro', 
        alpha=opacity,
        color='b',
        linestyle='-',
        )
        #label=u"Lunes")
        valsX += eje_x3['x_lunes_' + str(h)]
        valsY += anio_lunes[h][1] 


#       print eje_x3['x_martes_' + str(h)]
        plt.plot(eje_x3['x_martes_' + str(h)], anio_martes[h][1] , 'ro', 
        alpha=opacity,
        color='g',
        linestyle='-',
        )
        #label=u"Martes")
        valsX += eje_x3['x_martes_' + str(h)]
        valsY += anio_martes[h][1] 

#       print eje_x3['x_miercoles_' + str(h)]
        plt.plot(eje_x3['x_miercoles_' + str(h)], anio_miercoles[h][1] , 'ro', 
        alpha=opacity,
        color='r',
        linestyle='-',
        )
        #label=u"Miercoles")
        valsX += eje_x3['x_miercoles_' + str(h)]
        valsY += anio_miercoles[h][1] 

#       print eje_x3['x_jueves_' + str(h)]
        plt.plot(eje_x3['x_jueves_' + str(h)], anio_jueves[h][1] , 'ro', 
        alpha=opacity,
        color='c',
        linestyle='-',
        )
        #label=u"Jueves")
        valsX += eje_x3['x_jueves_' + str(h)]
        valsY += anio_jueves[h][1] 

#       print eje_x3['x_martes_' + str(h)]
        plt.plot(eje_x3['x_viernes_' + str(h)], anio_viernes[h][1] , 'ro', 
        alpha=opacity,
        color='m',
        linestyle='-',
        )
        #label=u"Viernes")
        valsX += eje_x3['x_viernes_' + str(h)]
        valsY += anio_viernes[h][1] 

#       print eje_x3['x_sabado_' + str(h)]
        plt.plot(eje_x3['x_sabado_' + str(h)], anio_sabado[h][1] , 'ro', 
        alpha=opacity,
        color='y',
        linestyle='-',
        )
        #label=u"Sabado")
        valsX += eje_x3['x_sabado_' + str(h)]
        valsY += anio_sabado[h][1] 

#       print eje_x3['x_domingo_' + str(h)]
        plt.plot(eje_x3['x_domingo_' + str(h)], anio_domingo[h][1] , 'ro', 
        alpha=opacity,
        color='k',                                                                                                  linestyle='-',
        )
        #label=u"Domingo")
        valsX += eje_x3['x_domingo_' + str(h)]
        valsY += anio_domingo[h][1] 

      else:

        plt.plot(eje_x['x_lunes_' + str(h)], anio_lunes[h][3*j-1] , 'ro', 
        alpha=opacity,
        color='b',
        linestyle='-',
        label=u"Lunes")
        valsX += eje_x['x_lunes_' + str(h)]
        valsY += anio_lunes[h][3*j-1] 


#       print eje_x['x_martes_' + str(h)]
        plt.plot(eje_x['x_martes_' + str(h)], anio_martes[h][3*j-1] , 'ro', 
        alpha=opacity,
        color='g',
        linestyle='-',
        label=u"Martes")
        valsX += eje_x['x_martes_' + str(h)]
        valsY += anio_martes[h][3*j-1] 

#       print eje_x['x_miercoles_' + str(h)]
        plt.plot(eje_x['x_miercoles_' + str(h)], anio_miercoles[h][3*j-1] , 'ro', 
        alpha=opacity,
        color='r',
        linestyle='-',
        label=u"Miercoles")
        valsX += eje_x['x_miercoles_' + str(h)]
        valsY += anio_miercoles[h][3*j-1] 

#       print eje_x['x_jueves_' + str(h)]
        plt.plot(eje_x['x_jueves_' + str(h)], anio_jueves[h][3*j-1] , 'ro', 
        alpha=opacity,
        color='c',
        linestyle='-',
        label=u"Jueves")
        valsX += eje_x['x_jueves_' + str(h)]
        valsY += anio_jueves[h][3*j-1] 

#       print eje_x['x_martes_' + str(h)]
        plt.plot(eje_x['x_viernes_' + str(h)], anio_viernes[h][3*j-1] , 'ro', 
        alpha=opacity,
        color='m',
        linestyle='-',
        label=u"Viernes")
        valsX += eje_x['x_viernes_' + str(h)]
        valsY += anio_viernes[h][3*j-1] 

#       print eje_x['x_sabado_' + str(h)]
        plt.plot(eje_x['x_sabado_' + str(h)], anio_sabado[h][3*j-1] , 'ro', 
        alpha=opacity,
        color='y',
        linestyle='-',
        label=u"Sabado")
        valsX += eje_x['x_sabado_' + str(h)]
        valsY += anio_sabado[h][3*j-1] 

#       print eje_x['x_domingo_' + str(h)]
        plt.plot(eje_x['x_domingo_' + str(h)], anio_domingo[h][3*j-1] , 'ro', 
        alpha=opacity,
        color='k',                                                                                                  linestyle='-',
        label=u"Domingo")
        valsX += eje_x['x_domingo_' + str(h)]
        valsY += anio_domingo[h][3*j-1] 


        plt.plot(eje_x2['x_lunes_' + str(h)], anio_lunes[h][3*j] , 'ro', 
        alpha=opacity,
        color='b',
        linestyle='-',
        )
        #label=u"Lunes")
        valsX += eje_x2['x_lunes_' + str(h)]
        valsY += anio_lunes[h][3*j] 


#       print eje_x2['x_martes_' + str(h)]
        plt.plot(eje_x2['x_martes_' + str(h)], anio_martes[h][3*j] , 'ro', 
        alpha=opacity,
        color='g',
        linestyle='-',
        )
        #label=u"Martes")
        valsX += eje_x2['x_martes_' + str(h)]
        valsY += anio_martes[h][3*j] 

#       print eje_x2['x_miercoles_' + str(h)]
        plt.plot(eje_x2['x_miercoles_' + str(h)], anio_miercoles[h][3*j] , 'ro', 
        alpha=opacity,
        color='r',
        linestyle='-',
        )
        #label=u"Miercoles")
        valsX += eje_x2['x_miercoles_' + str(h)]
        valsY += anio_miercoles[h][3*j] 

#       print eje_x2['x_jueves_' + str(h)]
        plt.plot(eje_x2['x_jueves_' + str(h)], anio_jueves[h][3*j] , 'ro', 
        alpha=opacity,
        color='c',
        linestyle='-',
        )
        #label=u"Jueves")
        valsX += eje_x2['x_jueves_' + str(h)]
        valsY += anio_jueves[h][3*j] 

#       print eje_x2['x_martes_' + str(h)]
        plt.plot(eje_x2['x_viernes_' + str(h)], anio_viernes[h][3*j] , 'ro', 
        alpha=opacity,
        color='m',
        linestyle='-',
        )
        #label=u"Viernes")
        valsX += eje_x2['x_viernes_' + str(h)]
        valsY += anio_viernes[h][3*j] 

#       print eje_x2['x_sabado_' + str(h)]
        plt.plot(eje_x2['x_sabado_' + str(h)], anio_sabado[h][3*j] , 'ro', 
        alpha=opacity,
        color='y',
        linestyle='-',
        )
        #label=u"Sabado")
        valsX += eje_x2['x_sabado_' + str(h)]
        valsY += anio_sabado[h][3*j] 

#       print eje_x2['x_domingo_' + str(h)]
        plt.plot(eje_x2['x_domingo_' + str(h)], anio_domingo[h][3*j] , 'ro', 
        alpha=opacity,
        color='k',                                                                                                  linestyle='-',
        )
        #label=u"Domingo")
        valsX += eje_x2['x_domingo_' + str(h)]
        valsY += anio_domingo[h][3*j] 
    

        plt.plot(eje_x3['x_lunes_' + str(h)], anio_lunes[h][3*j+1] , 'ro', 
        alpha=opacity,
        color='b',
        linestyle='-',
        )
        #label=u"Lunes")
        valsX += eje_x3['x_lunes_' + str(h)]
        valsY += anio_lunes[h][3*j+1] 


#       print eje_x3['x_martes_' + str(h)]
        plt.plot(eje_x3['x_martes_' + str(h)], anio_martes[h][3*j+1] , 'ro', 
        alpha=opacity,
        color='g',
        linestyle='-',
        )
        #label=u"Martes")
        valsX += eje_x3['x_martes_' + str(h)]
        valsY += anio_martes[h][3*j+1] 

#       print eje_x3['x_miercoles_' + str(h)]
        plt.plot(eje_x3['x_miercoles_' + str(h)], anio_miercoles[h][3*j+1] , 'ro', 
        alpha=opacity,
        color='r',
        linestyle='-',
        )
        #label=u"Miercoles")
        valsX += eje_x3['x_miercoles_' + str(h)]
        valsY += anio_miercoles[h][3*j+1] 

#       print eje_x3['x_jueves_' + str(h)]
        plt.plot(eje_x3['x_jueves_' + str(h)], anio_jueves[h][3*j+1] , 'ro', 
        alpha=opacity,
        color='c',
        linestyle='-',
        )
        #label=u"Jueves")
        valsX += eje_x3['x_jueves_' + str(h)]
        valsY += anio_jueves[h][3*j+1] 

#       print eje_x3['x_martes_' + str(h)]
        plt.plot(eje_x3['x_viernes_' + str(h)], anio_viernes[h][3*j+1] , 'ro', 
        alpha=opacity,
        color='m',
        linestyle='-',
        )
        #label=u"Viernes")
        valsX += eje_x3['x_viernes_' + str(h)]
        valsY += anio_viernes[h][3*j+1] 

#       print eje_x3['x_sabado_' + str(h)]
        plt.plot(eje_x3['x_sabado_' + str(h)], anio_sabado[h][3*j+1] , 'ro', 
        alpha=opacity,
        color='y',
        linestyle='-',
        )
        #label=u"Sabado")
        valsX += eje_x3['x_sabado_' + str(h)]
        valsY += anio_sabado[h][3*j+1] 

#       print eje_x3['x_domingo_' + str(h)]
        plt.plot(eje_x3['x_domingo_' + str(h)], anio_domingo[h][3*j+1] , 'ro', 
        alpha=opacity,
        color='k',                                                                                                  linestyle='-',
        )
        #label=u"Domingo")
        valsX += eje_x3['x_domingo_' + str(h)]
        valsY += anio_domingo[h][3*j+1] 

    plt.xlabel(u"días")
    if j == 0:
      plt.ylabel(u"Cantidad de delays de " + meses[11] + ", " + meses[0] + " y " + meses[1])
    else:
      plt.ylabel(u"Cantidad de delays de " + meses[3*j-1] + ", " + meses[3*j] + " y " + meses[3*j+1])
    labels = [dias_grafico[i % 7] for i in range(0, 3*(ultimo_anio - primer_anio + 1)*7)] 
    #plt.xticks([2.5+5*z for z in range(0, 3*(ultimo_anio - primer_anio + 1)*7)],labels,fontsize=10)
    plt.xticks([7.5+15*z for z in range(0, 3*(ultimo_anio - primer_anio + 1)*7)],labels,fontsize=10)
    #plt.xticks([9+18*z for z in range(0, 3*(ultimo_anio - primer_anio + 1)*7)],labels,fontsize=10)

    #CML
    valsEstimacion = []
    param = calcularCML(valsX, valsY, func)
    for i in range(0, len(valsX)):
      valsEstimacion.append(func(i, param[0], param[1], param[2]))

    plt.plot(valsX, valsEstimacion, 'ro', alpha=opacity, linestyle='-', color='#602312')

    plt.legend(bbox_to_anchor=(0.96, 1), prop={'size': 10})
    #plt.savefig(directory + '/graficos/grafico_cantidad_delay_hora')

    if j == 0:
      directory = directory + '/graficos_sin_ceros_estimaciones'

    if not os.path.exists(directory):
      os.mkdir(directory)

    print directory + '/' + meses[11] + "_" + meses[0] + "_" + meses[1] + "_2005"
    if j == 0:
      plt.savefig(directory + '/' + meses[11] + "_" + meses[0] + "_" + meses[1] + "_2005")
    else:
      plt.savefig(directory + '/' + meses[3*j-1] + "_" + meses[3*j] + "_" + meses[3*j+1] + "_2005")

    plt.show()


if __name__ == "__main__":
  main()
