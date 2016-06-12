#!/bin/bash

#$1 columna a sumar
#$2 archivo de entrada
#$3 archivo de salida

echo "voy a promediar la columna "$1" para la salida "$3
awk '{ sum += $1; n++ } END { print (sum/n) }' $2 >> $3