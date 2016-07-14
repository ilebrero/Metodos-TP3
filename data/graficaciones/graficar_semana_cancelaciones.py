#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
from graficaciones.graficar_cuadrados_minimos import calcularCML
#from graficaciones.graficar_cuadrados_minimos import errorCuadraticoMedio
import matplotlib.pyplot as plt
import os

#def func(x, a, b):
 # return a*np.sin(x()) + b

#ultima prueba
def func3(x, b, c): #0.0230515984338
  return c * np.sin(x) + b + c * np.cos(x) + b

def func2(x, a, b, c, d): #0.0258012692494
  return c*np.abs(np.cos(x)) + b + a*x + d

def func2(x, b, c): #0.0382813604542
  return c*np.sin(x) + b

def func(x, a, b, c):
  return c*(np.abs(np.cos(x*12))) + a*np.abs(np.sin(12*x))

def errorCuadraticoMedio(valsY, valsEstimacion):
  error = [valsY[i] - valsEstimacion[i] for i in range(0, len(valsY))]

  res = 0
  for num in error:
    res += num*num 

  res /= float(len(valsY))

  return res


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

  #for i in range(0, 48):
  #  if data_1[i] != 0:
  #    data_2[i] /= float(data_1[i])

  #for i in range(0, 48):
  #  if vuelosPorSemana[i] != 0:
  #    data_1[i] /= float(vuelosPorSemana[i])

def graficarSemanaCancelaciones(directory, airport, cancelation_code):

# Instancio los arreglos para los datos
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
  #readFile(file_out + '2003.csv', cancelaciones_2003, cancelaciones_filtro_2003, cancelation_code)
  readFile(file_out + '2004.csv', cancelaciones_2004, cancelaciones_filtro_2004, cancelation_code)
  readFile(file_out + '2005.csv', cancelaciones_2005, cancelaciones_filtro_2005, cancelation_code)
  readFile(file_out + '2006.csv', cancelaciones_2006, cancelaciones_filtro_2006, cancelation_code)
  readFile(file_out + '2007.csv', cancelaciones_2007, cancelaciones_filtro_2007, cancelation_code)
  readFile(file_out + '2008.csv', cancelaciones_2008, cancelaciones_filtro_2008, cancelation_code)

  # Nombre del segundo aeropuerto
  #readFile('SEA/SEA' + '2007.csv', cancelaciones_2007, cancelaciones_filtro_2007, cancelation_code)
  #readFile('SEA/SEA' + '2008.csv', cancelaciones_2008, cancelaciones_filtro_2008, cancelation_code)


  x = []
  y = []
  years = 5

  len_x = years * 12 * 4

  for i in range (0,len_x):
    x.append(i)
    y.append(i)

  cancelaciones_filtro = []
  cancelaciones = []

  #for i in range (inicioAno, finAno+1):
  cancelaciones = cancelaciones_2004 + cancelaciones_2005 + cancelaciones_2006 + cancelaciones_2007 + cancelaciones_2008
  cancelaciones_filtro = cancelaciones_filtro_2004 + cancelaciones_filtro_2005 + cancelaciones_filtro_2006 + cancelaciones_filtro_2007 + cancelaciones_filtro_2008

  if not os.path.exists(directory + '/graficos'):
    os.mkdir(directory + '/graficos')

  opacity = 0.4

# Debería haber cantidad de años-1 
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

    for i in range(1, years*4):
      plt.axvline(x=12*i, linewidth=2, color='g')

    plt.plot(x, cancelaciones_filtro, 'ro',
      alpha=opacity,
      linestyle='-',
      color='b'
    )

    ################## CML EMPIEZA
    valsEstimacion = []
    #anios_a_estimar = 1
    anios_para_entrenar = 2
    inicio = 48 * anios_para_entrenar 
    #anios_a_estimar = 1
    #inicio = 240 - 48 * anios_a_estimar 
    fin = 240
    param = []

    # PLOTEO DE CON EL ANO DIVIDO EN 4
    for i in range(0, anios_para_entrenar*4):
      # Se divide al año en cuatro -> calculo CML de a 12 datos (4 semanas de 3 meses)
      param.append(calcularCML(x[12*i : 12*i + 12], cancelaciones_filtro[12*i : 12*i + 12], func))

    for i in range(0, fin):
      semana = (i % 48) / 12
      valsEstimacion.append(func(i, param[semana] [0], param[semana] [1], param[semana] [2])) #, param[semana] [3], param[semana] [4], param[semana] [5], param[semana] [6], param[semana] [7], param[semana] [8], param[semana][9], param[semana][10])) #, param[semana] [2])) #, param[semana] [3]))

    # PLOTE SIN DIVIDIRLO
    #param = calcularCML(x[0 : inicio], cancelaciones_filtro[0 : inicio], func)

    #for i in range(0, fin):
    #  valsEstimacion.append(func(i % (2*48), param  [0], param  [1], param  [2])) #, param  [3], param  [4], param  [5], param  [6], param  [7], param  [8], param [9], param [10])) #, param  [2])) #, param  [3]))

    plt.plot(x[0 : inicio], valsEstimacion[0 : inicio], 'ro', alpha=opacity, linestyle='-', color='r')
    plt.plot(x[inicio : fin], valsEstimacion[inicio : fin], 'ro', alpha=opacity, linestyle='-', color='#602312')

    error = errorCuadraticoMedio(cancelaciones_filtro[inicio : fin], valsEstimacion[inicio : fin])
    with open(airport + 'func' + str(anios_para_entrenar) + '.tex', 'w') as file_write:
    #with open(airport + 'cuadLog_' + str(anios_a_entrenar) + '_2008' + '.tex', 'a') as file_write:
      file_write.write(str(error) + '\n')

    ################## CML TERMINA


    fig += airport + str(anios_para_entrenar)
    plt.xlabel(u"Semanas")
    plt.ylabel(u"Cantidad de cancelaciones")
    plt.xticks([24+12*i*4 for i in range(0,5)],['2004', '2005', '2006', '2007', '2008'],fontsize=10)
    plt.legend()
    plt.savefig(fig)
    plt.show()


#    for j in range(len(finalData), len(finaldatas)):
 #     finalData.append(finalData[len(finalData)-1])      




if __name__ == "__main__":
  main()

    #print "<<<<<<<<<<<<<<<<<<x<<<<<<<<<<<<<<< " 
    #print len(x)
    #print x 
    #print "<<<<<<<<<<<<<<<<<<x<<<<<<<<<<<<<<< " 
    #print "<<<<<<<<<<<<<<<<<<valsEstimacion<<<<<<<<<<<<<<< " 
    #print len(valsEstimacion)
    #print valsEstimacion 
    #print "<<<<<<<<<<<<<<<<<<valsEstimacion<<<<<<<<<<<<<<< " 

  #anos_filtro = {
  #  "2003" : cancelaciones_filtro_2003,
  #  "2004" : cancelaciones_filtro_2004,
  #  "2005" : cancelaciones_filtro_2005,
  #  "2006" : cancelaciones_filtro_2006,
  #  "2007" : cancelaciones_filtro_2007,
  #  "2008" : cancelaciones_filtro_2008
  #}

  #inicioAno = int( raw_input("año inicial") )
  #finAno    = int( raw_input("año final") )
  #finEntrenamiento = int( raw_input("año de entrenamiento final") )

  #years = finAno - inicioAno + 1


  #if not os.path.exists(directory + '/datosparacml'):
  #  os.mkdir(directory + '/datosparacml')

  #with open(directory + '/datosparacml/' + 'cancelaciones_semana_' + airport, 'w+') as file_out_data:
  #  for val in cancelaciones:
  #    file_out_data.write(str(val) + '\n')



    #finaldatas = []
    #finaly = []
    #for i in range(0, len(cancelaciones_filtro)):
    #  finaldatas.append(cancelaciones_filtro[i])

    #for j in range(0, len(finaldatas)):
    #  finaly.append(j)

    #plt.plot(finaly, finaldatas, 'ro', 
    #         alpha=opacity,
    #         linestyle='-',
    #         color='b',
    #         label=lab)

    #finalData = []
    #
    #trainYears = finEntrenamiento - inicioAno + 1

    #entY = finaly [0 : trainYears*48]
    #entD = finaldatas [0 : trainYears*48]

    #trainDataPredict = []
    #trainYPredict = []

    #paramsCML = []

    ##abre archivo donde se van a guardar los parametros
    #for an in range (0, trainYears):
    #  entY2 = entY[len(entY) / trainYears * an:len(entY) / trainYears * (an + 1)]
    #  entD2 = entD[len(entD) / trainYears * an:len(entD) / trainYears * (an + 1)]

    #  for j in range(0, 4):
    #    yActual = entY2[len(entY2) / 4 * j : len(entY2) / 4 * (j + 1)]
    #    cancelaciones_filtroActual = entD2[len(entD2) / 4 * j:len(entD2) / 4 * (j + 1)]
    #    
    #    #Guarda los parametros en el archivo
    #    param = calcularCML(yActual, cancelaciones_filtroActual, func)
    #    paramsCML.append(param)

    #    for i in yActual:
    #      trainDataPredict.append(func(i, param[0], param[1], param[2]))
    #      trainYPredict.append(i)

    #predictYears = finAno - finEntrenamiento + 1

    ##abre archivo donde se van a guardar los parametros

    #entY = finaly [trainYears*48 : len(finaly)]
    #entD = finaldatas [trainYears*48 : len(finaldatas)]

    #newDataPredict = []
    #newYPredict = []

    #for an in range(0, predictYears):
    #  entY2 = entY[len(entY) / predictYears * an:len(entY) / predictYears * (an + 1)]
    #  entD2 = entD[len(entD) / predictYears * an:len(entD) / predictYears * (an + 1)]

    #  for j in range(0, 4):
    #    yActual = entY2[len(entY2) / 4 * j:len(entY2) / 4 * (j + 1)]
    #    cancelaciones_filtroActual = entD2[len(entD2) / 4 * j:len(entD2) / 4 * (j + 1)]

    #    param = paramsCML[(an + j) % len(paramsCML)]

    #    for i in yActual:
    #      newDataPredict.append(func(i, param[0], param[1], param[2]))
    #      newYPredict.append(i)

    #errorCuadratico = errorCuadraticoMedio(entD, newDataPredict)

    #print("el error cuadratico medio es: " + str(errorCuadratico))

    #plt.plot(trainYPredict, trainDataPredict, 'ro',
    #  alpha=opacity,
    #  linestyle='-',
    #  color='r'
    #)

    #plt.plot(finaly, finaldatas, 'ro',
    #  alpha=opacity,
    #  linestyle='-',
    #  color='b'
    #)

    #plt.plot(newYPredict, newDataPredict, 'ro',
    #  alpha=opacity,
    #  linestyle='-',
    #  color='y'
    #)
