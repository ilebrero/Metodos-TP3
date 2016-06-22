#!/bin/bash
# Filtrar por input usando awk.

# -------------- Datos -----------#
# $1 es la columna a filtrar      #
# $2 es el dato a tener en cuenta #
# $3 archivo de entrada			  #
# $4 archivo de salida            #
###################################

 #Ojo con la secuencia de " y ' al filtrar por &&. 
 #Filtro la columna
awk -F, '$'"$1"' == "'"$2"'"' $3 > $4
