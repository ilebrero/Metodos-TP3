#!/usr/bin/env python
# -*- coding: utf-8 -*-

import scipy.optimize as optimization
#sudo pip install scipy
import matplotlib.pyplot as plt
import numpy
import os

def cuadratica(x, a, b, c):
    return a + b*x + c*x*x

def lineal(x, a, b):
    return a + b*x

# Devuleve los valores a, b, c, ..... que minimizan func con respecto a func(xdata) = ydata
# EJ con lineal: calcularCML(xArr, yARR,func) = [0,1293842, 0,1118473] <- [a, b]
def calcularCML(xArr, yArr, func): 
	xdata = numpy.array(xArr)
	ydata = numpy.array(yArr)

	print optimization.curve_fit(cuadratica, xdata, ydata)

	parametros, covarianza = optimization.curve_fit(func, xdata, ydata)

	return parametros

# ejemplo con aridad func(x, a, b)

# param = calcularCML(valsX, valsY, func)
# for i in range(0, len(valsX)):
#	valsEstimacion.append(func(i, param[0], param[1]))
#	plt.plot(valsX, valsEstimacion, 'ro', alpha=opacity, linestyle='-', color='g')





#def extra():
#	airport = raw_input("ingrese el aeropuerto: ")#

#	xArray = []
#	yArray = []
#	sigma = []#

#	cantidadDatos = 0
#	with open("../" + airport + "/datosparacml/cancelaciones_semana_" + airport, 'r') as file_in:
#		
#		for line in file_in:
#			yArray.append(float(line))
#			xArray.append(cantidadDatos)
#			sigma.append(1.0)
#			cantidadDatos = cantidadDatos + 1#

#	xdata = numpy.array(xArray)
#	ydata = numpy.array(yArray)
#	finalSigma = numpy.array(sigma)#

#	print optimization.curve_fit(lineal, xdata, ydata)#

#	parametros, covarianza = optimization.curve_fit(lineal, xdata, ydata, None, finalSigma)#

#	#graficar curva
#	if not os.path.exists('./graficoscml'):
#	    os.mkdir('./graficoscml')
#	opacity = 0.4
#	for i in range(0, cantidadDatos - 1):
#		plt.plot(i, lineal(i, parametros[0], parametros[1]), 'ro', alpha=opacity, linestyle='-', color='b')#

#	plt.xlabel(u"Semanas")
#	plt.ylabel(u"Cantidad de delays")
#	plt.xticks([24+12*i*4 for i in range(0,11)],['1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008'],fontsize=10)
#	plt.legend()
#	plt.savefig('./graficoscml/cancelaciones_semana_' + airport)
#	plt.show()
