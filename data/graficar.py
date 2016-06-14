#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from math import log
from graficaciones.graficar_mes_cancelaciones import graficarMesCancelaciones
from graficaciones.graficar_semana_cancelaciones import graficarSemanaCancelaciones
from graficaciones.graficar_mes_delay import graficarMesDelay
#from graficaciones.graficar_semana_delay import graficarSemanaDelay
import os

def main():

# Instancio los arreglos para los datos
  airport = raw_input("¿Nombre del aeropuerto? ")
  #directory = raw_input("Carpeta con datos: ")
  directory = airport
  os.system('cls' if os.name == 'nt' else 'clear')
  
  print "¿Qué dato querés graficar? "
  #print "13: Tiempo de vuelo " 
  print "14: Delay de llegada "
  print "15: Delay de salida "
  print "16: Delay de llegada y salida "
  #print "18: Distancia " 
  print "21: Cancelaciónes " 
  data = int(raw_input("Ingrese un número: "))
  os.system('cls' if os.name == 'nt' else 'clear')

  if data == 14:
    directory += '/' + airport + 'dest'
  elif data == 15:
    directory += '/' + airport + 'org'

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

    if granularity == 0:
      graficarMesCancelaciones(directory, airport, cancelation_code)
    elif granularity == 1:
      graficarSemanaCancelaciones(directory, airport, cancelation_code)

  elif data == 14 or data == 15 or data == 16: # Delay de salida

    if granularity == 0:
      print "entre bien"
      graficarMesDelay(directory, airport, delay_filter, data)
    elif granularity == 1:
      print "hola"
  #    graficarSemanaCancelaciones(directory, airport, delay_filter)

if __name__ == "__main__":
  main()
