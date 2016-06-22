# coding=utf-8

#argv[1] archivo de entrada
#argv[2] archivo de salida
#argv[3] entrada (para arrival delay) / salida (para departure delay)
import sys

archivo_salida = open(sys.argv[2], "wb")

if sys.argv[3] == 'entrada': #si voy a ver delay de entrada o de salida
  n = 14
else:
  n = 15

with open(sys.argv[1], "r") as archivo_entrada:
  linea = archivo_entrada.readline()
  linea_actual = linea.split(",")
  print "lpm"

  for i in range(1, 13):
    cantidad_con_delay = [0 for k in range(0, 31)]
    cantidad_total = [0 for k in range(0, 31)]
    
    while (len(linea_actual) > 2 and int(linea_actual[1]) == i): #mientras sean datos del mes i
      
      if linea_actual[n] != 'NA': #si tengo datos válidos
        
        if int(linea_actual[n]) > 15: #si hay delay
          cantidad_con_delay[int(linea_actual[2])-1] += 1 #en el día del delay, sumo 1
      
        cantidad_total[int(linea_actual[2])-1] += 1
      
      linea = archivo_entrada.readline()
      linea_actual = linea.split(",")

    for j in range(0, 31):
      if cantidad_total[j] != 0:
        promedio = cantidad_con_delay[j] / float(cantidad_total[j])
        prom = str(promedio) + '\n'
        archivo_salida.write(prom)

archivo_salida.close()
