#!/bin/bash
# Filtrar por input usando awk.

# -------------- Datos ------------ #
# $0 es la columna a filtrar        #
# $1 es el dato a tener en cuenta   #
# $2 año de inicio                  #
# $3 año de fin                     #
#####################################

for i in `seq $3 $4`;
do
	#"../data/200"$i".csv"
	infile="../data/"$i".csv"

	# el path es /data/filtrados/<columnafiltrada>_<datofiltrado>_<año>_data.csv
	outfile="../data/filtrados/"$1"_"$2"_"$i"_data.csv"

	 #Ojo con la secuencia de " y ' al filtrar por &&. 
	 #Filtro la columna
	awk -F, '$'"$1"' == "'"$2"'"' $infile > $outfile
done