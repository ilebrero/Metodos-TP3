#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
from graficaciones.graficar_cuadrados_minimos import calcularCML
import matplotlib.pyplot as plt
import os


#def func(x, a, b):
 # return a*np.sin(x()) + b

#ultima prueba
def func(x, b, c):
  return np.abs(np.sin(x + c) + np.cos(x + b))

#def func2(x, b):
#  return np.abs(0.7 * np.sin(x/float(10)) * np.cos(x/float(10))) + b




  #if ( (x % 50) < 25 ):
#    res = 0.7 * np.sin(x/float(10)) * np.cos(x/float(10)) + b
#  else:
#    res = 2* (0.7 * np.sin(x/float(10)) * np.cos(x/float(10)) + b)
#  return res

#return  -0.7 * np.sin(x/float(10)) + b <- joaco aprobes

#return np.abs(0.7 * np.sin(x/float(10)) + b) <- ponele que ajusta

def readFile(File, data_1, data_2, cancelation_code):

  vuelosPorSemana = [0 for i in range(0, 48)]

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

      if (currentline[21] != 'NA'):
        vuelosPorSemana[semana+mes*4] += 1 # Cuento la cantidad de datos por mes

      if (currentline[21] == '1'):

        data_1[semana+mes*4] += 1 # Cuento la cantidad de datos por mes

      if currentline[22] == cancelation_code:
        data_2[semana+mes*4] += 1  # Sumo todos los datos del mes

  for i in range(0, 48):
    if data_1[i] != 0:
      data_2[i] /= float(data_1[i])

  for i in range(0, 48):
    if vuelosPorSemana[i] != 0:
      data_1[i] /= float(vuelosPorSemana[i])

def graficarSemanaCancelaciones(directory, airport, cancelation_code):

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

  #readFile(file_out + '1998.csv', cancelaciones_1998, cancelaciones_filtro_1998, cancelation_code)
  #readFile(file_out + '1999.csv', cancelaciones_1999, cancelaciones_filtro_1999, cancelation_code)
  #readFile(file_out + '2000.csv', cancelaciones_2000, cancelaciones_filtro_2000, cancelation_code)
  #readFile(file_out + '2001.csv', cancelaciones_2001, cancelaciones_filtro_2001, cancelation_code)
  #readFile(file_out + '2002.csv', cancelaciones_2002, cancelaciones_filtro_2002, cancelation_code)
  readFile(file_out + '2003.csv', cancelaciones_2003, cancelaciones_filtro_2003, cancelation_code)
  readFile(file_out + '2004.csv', cancelaciones_2004, cancelaciones_filtro_2004, cancelation_code)
  readFile(file_out + '2005.csv', cancelaciones_2005, cancelaciones_filtro_2005, cancelation_code)
  readFile(file_out + '2006.csv', cancelaciones_2006, cancelaciones_filtro_2006, cancelation_code)
  readFile(file_out + '2007.csv', cancelaciones_2007, cancelaciones_filtro_2007, cancelation_code)
  readFile(file_out + '2008.csv', cancelaciones_2008, cancelaciones_filtro_2008, cancelation_code)

  years = 6
  x = []
  y = []

  len_x = years * 12 * 4

  for i in range (1,len_x+1):
    x.append(i)
    y.append(i)
  cancelaciones = cancelaciones_2003 + cancelaciones_2004 + cancelaciones_2005 + cancelaciones_2006 + cancelaciones_2007 + cancelaciones_2008
  cancelaciones_filtro = cancelaciones_filtro_2003 + cancelaciones_filtro_2004 + cancelaciones_filtro_2005 + cancelaciones_filtro_2006 + cancelaciones_filtro_2007 + cancelaciones_filtro_2008


  if not os.path.exists(directory + '/graficos'):
    os.mkdir(directory + '/graficos')

  opacity = 0.4

  if not os.path.exists(directory + '/datosparacml'):
    os.mkdir(directory + '/datosparacml')

  with open(directory + '/datosparacml/' + 'cancelaciones_semana_' + airport, 'w+') as file_out_data:
    for val in cancelaciones:
      file_out_data.write(str(val) + '\n')

# Debería haber cantidad de años-1 
  for i in range(1, years):
    plt.axvline(x=12*4*i, linewidth=2, color='k')

  #plt.plot(x, cancelaciones, 'ro', 
#           alpha=opacity,
#           linestyle='-',
#           color='b',
#           label=u"Cancelaciones por semana")


#   for j in range(0, 4):
#    
#    xActual = x[len(x) / 4 * j:len(x) / 4 * (j + 1)]
#    cancelaciones_filtroActual = cancelaciones_filtro[len(cancelaciones_filtro) / 4 * j:len(cancelaciones_filtro) / 4 * (j + 1)]#

#    if (j%2 == 0):
#      print "1"
#      param = calcularCML(xActual, cancelaciones_filtroActual, func)
#    else:
#      print "2"
#      param = calcularCML(xActual, cancelaciones_filtroActual, func2)
#    
#    for i in range(0, len(cancelaciones_filtroActual)):
#    
#      xActual = [i for i in range(0, len(cancelaciones_filtroActual))]
#      data = [func(i, param[0]) for i in range(0, len(cancelaciones_filtroActual))]#

#      plt.plot(xActual, data, 'ro', 
#        alpha=opacity,
#        linestyle='-',
#        color='g'
#      )
#    

  plt.xlabel(u"Semanas")
  plt.ylabel(u"Cantidad de cancelaciones")
  plt.xticks([24+12*i*4 for i in range(0,6)],['2003', '2004', '2005', '2006', '2007', '2008'],fontsize=10)
  plt.legend()
  #plt.savefig(directory + '/graficos/grafico_cancelaciones_semana')
  #plt.show()

  if cancelation_code != '':
    lab = ''
    fig = ''
    if cancelation_code == 'A':
      lab = "Cancelaciones de carrier por semana"
      fig = directory + '/graficos/grafico_cancelaciones_carrier_semana'

    if cancelation_code == 'B':
      lab = "Cancelaciones de clima por semana"
      fig = directory + '/graficos/grafico_cancelaciones_clima_semana'

    if cancelation_code == 'C':
      lab = "Cancelaciones de NAS por semana"
      fig = directory + '/graficos/grafico_cancelaciones_NAS_semana'

    if cancelation_code == 'D':
      lab = "Cancelaciones de seguridad por semana"
      fig = directory + '/graficos/grafico_cancelaciones_seguridad_semana'

    for i in range(1, years):
      plt.axvline(x=12*4*i, linewidth=2, color='k')

    media = np.mean(cancelaciones_filtro)
    desvio = np.std(cancelaciones_filtro)
    finaldatas = []
    finaly = []
    print "----------------meida--------------"
    for i in range(0, len(cancelaciones_filtro)):
      #if np.abs(cancelaciones_filtro[i] - media) > 0.4 * desvio:
#        finaldatas.append(cancelaciones_filtro[i])
#      else:
#        finaldatas.append(media)

      finaldatas.append(cancelaciones_filtro[i])

    for j in range(0, len(finaldatas)):
      finaly.append(j)

    print ("finaldatas - " + str(len(finaldatas)))
    print ("finaly - " + str(len(finaly)))

    plt.plot(finaly, finaldatas, 'ro', 
             alpha=opacity,
             linestyle='-',
             color='b',
             label=lab)

    finalData = []

    for j in range(0, 4):
      
      yActual = finaldatas[len(finaly) / 4 * j:len(finaly) / 4 * (j + 1)]
      cancelaciones_filtroActual = finaldatas[len(finaldatas) / 4 * j:len(finaldatas) / 4 * (j + 1)]
        
      for i in range(len(finaly) / 4 * j,len(finaly) / 4 * (j + 1)):
        #if (i%34 <= 17):
#          print "1"
#          param = calcularCML(yActual, cancelaciones_filtroActual, func)
#          finalData.append(func(i, param[0], param[1], param[2]))#

#        else:
          print "2"
          param = calcularCML(yActual, cancelaciones_filtroActual, func)
          finalData.append(func(i, param[0], param[1]))

    for j in range(len(finalData), len(finaldatas)):
      finalData.append(finalData[len(finalData)-1])      

    print (len(finalData))
    print (len(finaly))


    plt.plot(finaly, finalData, 'ro',
      alpha=opacity,
      linestyle='-',
      color='r'
    )
      
    plt.xlabel(u"Semanas")
    plt.ylabel(u"Cantidad de cancelaciones")
    plt.xticks([24+12*i*4 for i in range(0,6)],['2003', '2004', '2005', '2006', '2007', '2008'],fontsize=10)
    plt.legend()
    plt.savefig(fig)
    plt.show()


if __name__ == "__main__":
  main()
