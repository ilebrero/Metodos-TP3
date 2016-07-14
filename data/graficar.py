#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from math import log
from graficaciones.graficar_mes_cancelaciones import graficarMesCancelaciones
from graficaciones.graficar_mes_cancelaciones2 import graficarMesCancelaciones2
from graficaciones.graficar_semana_cancelaciones import graficarSemanaCancelaciones
from graficaciones.graficar_semana_cancelaciones2 import graficarSemanaCancelaciones2
from graficaciones.graficar_mes_delay import graficarMesDelay
from graficaciones.graficar_mes_delay2 import graficarMesDelay2
from graficaciones.graficar_semana_delay import graficarSemanaDelay
from graficaciones.graficar_semana_delay2 import graficarSemanaDelay2
from graficaciones.graficar_hora_delay import graficarHoraDelay
from graficaciones.graficar_hora_delay2 import graficarHoraDelay2
from graficaciones.graficar_hora_delay3 import graficarHoraDelay3
from graficaciones.graficar_hora_delay4 import graficarHoraDelay4
from graficaciones.graficar_posta import graficarPosta
from graficaciones.graficar_posta_intervalos import graficarPostaIntervalos
from graficaciones.graficar_semana_vuelos import graficarSemanaVuelos
from graficaciones.graficar_mes_vuelos import graficarMesVuelos
import os

def menu(airport_1, airport_2 = None):

  directory_1 = airport_1
  directory_2 = airport_2

  directory_both = ''
  if airport_2 != None:
    directory_both = airport_1 + '_' + airport_2
    if not os.path.exists(directory_both):
      os.mkdir(directory_both)

  os.system('cls' if os.name == 'nt' else 'clear')
  print "¿Qué dato querés graficar? "
  #print "13: Tiempo de vuelo " 
  print "14: Delay de llegada "
  print "15: Delay de salida "
  print "16: Delay de llegada y salida "
  #print "18: Distancia " 
  print "21: Cancelaciónes " 
  print "22: Cantidad de vuelos " 
  data = int(raw_input("Ingrese un número: "))
  os.system('cls' if os.name == 'nt' else 'clear')

  if data == 14:
    directory_1 += '/' + airport_1 + 'dest'
    if airport_2 != None:
      directory_2 += '/' + airport_2 + 'dest'
  elif data == 15 or data == 21:
    directory_1 += '/' + airport_1 + 'org'
    if airport_2 != None:
      directory_2 += '/' + airport_2 + 'org'


  print "¿Querés filtrar por alguno de los siguientes?: "
  print "24: Carrier delay " 
  print "25: Weather delay " 
  print "26: NAS delay "
  print "27: Security delay " 
  #print "28: Late Aircraft delay " 
  print "0: Ninguno de los anteriores" 
  delay_filter = int(raw_input("Ingrese un número: "))
  os.system('cls' if os.name == 'nt' else 'clear')

  print "¿Qué granularidad deseas? "
  print "0: Mes"
  print "1: Semana por año" 
  print "2: Día del mes" 
  print "3: Día de la semana" 
  print "4: Hora" 
  print "5: Ninguno de los anteriores" 
  granularity = int(raw_input("Ingrese un número: "))
  os.system('cls' if os.name == 'nt' else 'clear')

  if data == 21: # Cancelaciones
    cancelation_code = ''

    if delay_filter == 24:
      cancelation_code = 'A'
    elif delay_filter == 25:
      cancelation_code = 'B'
    elif delay_filter == 26:
      cancelation_code = 'C'
    elif delay_filter == 27:
      cancelation_code = 'D'

    print ("granularity = " + str(granularity))
    print directory_1
    if granularity == 0:
      
      if airport_2 == None:
        graficarMesCancelaciones(directory_1, airport_1, cancelation_code)
      else:
        graficarMesCancelaciones2(directory_1, directory_2, airport_1, airport_2, cancelation_code)
    
    elif granularity == 1:
      
      if airport_2 == None:
        graficarSemanaCancelaciones(directory_1, airport_1, cancelation_code)
      else:
        graficarSemanaCancelaciones2(directory_1, directory_2, airport_1, airport_2, cancelation_code)

  elif data == 14 or data == 15 or data == 16: # Delay de salida

    if granularity == 0:
      if airport_2 == None:
        graficarMesDelay(directory_1, airport_1, delay_filter, data)
      else:
        graficarMesDelay2(directory_1, directory_2, directory_both, airport_1, airport_2, delay_filter, data)

    elif granularity == 1:
      if airport_2 == None:
        graficarSemanaDelay(directory_1, airport_1, delay_filter, data)
      else:
        graficarSemanaDelay2(directory_1, directory_2, directory_both, airport_1, airport_2, delay_filter, data)

    elif granularity == 4:
      #graficarHoraDelay(directory_1, airport_1, delay_filter, data)
      op = raw_input("¿De a 1 mes, de a 3 meses, o varios años? (1/3/v) ")
      if op == '1':
        graficarHoraDelay2(directory_1, airport_1, '2005', delay_filter, data)
      elif op == '3':
        #graficarHoraDelay3(directory_1, airport_1, '2005', delay_filter, data)
        graficarPostaIntervalos(directory_1, airport_1, '2005', delay_filter, data)
      elif op == 'v':
        graficarHoraDelay4(directory_1, airport_1, '2005', delay_filter, data)

  elif data == 22:
    if granularity == 1:
      print directory_1
      graficarSemanaVuelos(directory_1, airport_1, '')
    else:
      graficarMesVuelos(directory_1, airport_1, '')




def main():

# Instancio los arreglos para los datos
  opcion = raw_input("¿Querés comparar entre aeropuertos? (y/n) ")
  if opcion == 'y':
    print "Ingresa los aeropuertos: "
    airport_1 = raw_input("Primer aeropuerto: ")
    airport_2 = raw_input("Segundo aeropuerto: ")
    menu(airport_1, airport_2)

  else:
    airport = raw_input("¿Nombre del aeropuerto? ")
    menu(airport, None)
    #directory = raw_input("Carpeta con datos: ")
    

if __name__ == "__main__":
  main()