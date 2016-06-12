#!/bin/bash
# cuenta valores en un archivo por rango

# ----- Datos ------ #
# $1 inicio de rango #
# $2 fin de rango    #
# $3 entrada         #
# $4 salida          #
######################

for j in `seq $1 $2`;
do
	grep -c "$j" $(find $3 -type f -print0 | xargs -0 echo) >> $4
done