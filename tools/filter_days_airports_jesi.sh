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
	outfile_hawai="../data/filtrados/hawai_200"$i"_data.csv"
	outfile_washington="../data/filtrados/washington_salida200"$i"_data.csv"
	outfile_san_francico="../data/filtrados/san_francisco_200"$i"_data.csv"		
	 #Columna 18 ID aeropuerto
	 #Ojo con la secuencia de " y ' al filtrar por &&. 

# awk -F, '$18 == "'"$airport_mco"'"' $infile > $outfile_orlando
#	awk -F, '$18 == "'"$airport_hawai"'"' $infile > $outfile_hawai
	awk -F, '$18 == "'"$airport_iad"'"' $infile > $outfile_washington
#	awk -F, '$18 == "'"$airport_sfo"'"' $infile > $outfile_san_francico
done

 #Filtrar columnas fecha, aerolinea, nro. de vuelo 

for i in `seq 5 8`;
do
    infile="../data/filtrados/washington_200"$i"_data.csv"
	outfile="../data/filtrados/resultados/washington_200"$i"_por_dia.csv"

	# -f indica que columnas, "-d," significa "delimitador es una ','".
	cut -f4 -d, $infile > $outfile
  echo anio $i
  
	for j in `seq 1 7`;
		do
			grep -c $j $(find $outfile -type f -print0 | xargs -0 echo) >> "../data/filtrados/resultados/vuelos_X_dia_washington200"$i
      echo dia $j
		done
done 
