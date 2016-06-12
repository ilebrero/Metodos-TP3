#!/bin/bash
# Filtrar por par origen - destino usando awk.

# Definimos algunas variables. Ojo que a bash no le gustan los espacios cerca del "=".

# ------------------ Ocio ------------------- #
airport_hawai="HNL" #hawai
airport_mco="MCO" #orlando 

# ----------------- Trabajo ----------------- #
airport_iad="IAD" #washington 
airport_sfo="SFO" #san francisco

for i in `seq 5 8`;
do
	infile="../data/200"$i".csv"
	outfile_orlando="../data/filtrados/orlando_200"$i"_data.csv"
	outfile_hawai="../data/Filtrados/hawai_200"$i"_data.csv"
	outfile_washington="../data/Filtrados/washington_salida200"$i"_data.csv"
	outfile_san_francico="../data/Filtrados/san_francisco_200"$i"_data.csv"		
	 #Columna 18 ID aeropuerto
	 #Ojo con la secuencia de " y ' al filtrar por &&. 

	./filtrar_fila.sh 18 $airport_mco $infile $outfile_orlando
	./filtrar_fila.sh 18 $airport_hawai $infile $outfile_hawai
	./filtrar_fila.sh 18 $airport_iad $infile $outfile_washington
	./filtrar_fila.sh 18 $airport_sfo $infile $outfile_san_francico
done

#Filtrar columnas fecha, aerolinea, nro. de vuelo 

for i in `seq 5 8`;
do
    infile="../data/Filtrados/washington_200"$i"_data.csv"
	outfile="../data/Filtrados/resultados/washington_200"$i"_por_mes.csv"

	./tomar_columna.sh 2 $infile $outfile
	./count_in_range.sh 1 12 $outfile "../data/Filtrados/resultados/vuelosXmeswashington200"$i
done