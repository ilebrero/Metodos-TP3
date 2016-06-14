#!/bin/bash
for i in `seq 5 8`;
do 
	infile="../data/Filtrados/orlando_200"$i"_data.csv"
	columnas="../data/Filtrados/orlando_diasDelMes_"$i".data"
	orlando_final="../data/Filtrados/resultados/orlando_prom_delay_diasDelMes_200"$i".data"

	for j in `seq 1 31`;
		do
			dia="../data/Filtrados/dias/orlando_"$j".data"
			dia_delay="../data/Filtrados/dias/orlando"$j"_delay.data"
			./filtrar_fila.sh 3 $j $infile $dia
			./tomar_columna.sh 15 $dia $dia_delay
			./tomar_promedio_columna.sh 1 $dia_delay $orlando_final
		done

	infile="../data/Filtrados/washington_200"$i"_data.csv"
	columnas="../data/Filtrados/washington_diasDelMes_"$i".data"
	washington_final="../data/Filtrados/resultados/washington_prom_delay__diasDelMes_200"$i".data"
	for j in `seq 1 31`;
		do
			dia="../data/Filtrados/dias/washington"$j".data"
			dia_delay="../data/Filtrados/dias/washington"$j"_delay.data"
			./filtrar_fila.sh 3 $j $infile $dia
			./tomar_columna.sh 15 $dia $dia_delay
			./tomar_promedio_columna.sh 1 $dia_delay $washington_final
		done

	infile="../data/Filtrados/san_francisco_200"$i"_data.csv"
	columnas="../data/Filtrados/san_francisco_diasDelMes_"$i".data"
	san_francisco_final="../data/Filtrados/resultados/san_francisco_prom_delay__diasDelMes_200"$i".data"
	for j in `seq 1 31`;
		do
			dia="../data/Filtrados/dias/san_francisco_"$j".data"
			dia_delay="../data/Filtrados/dias/san_francisco"$j"_delay.data"
			./filtrar_fila.sh 3 $j $infile $dia
			./tomar_columna.sh 15 $dia $dia_delay
			./tomar_promedio_columna.sh 1 $dia_delay $san_francisco_final
		done

	infile="../data/Filtrados/hawai_200"$i"_data.csv"
	columnas="../data/Filtrados/hawai_diasDelMes_"$i".data"
	hawai_final="../data/Filtrados/resultados/hawai_prom_delay__diasDelMes_200"$i".data"
	for j in `seq 1 31`;
		do
			dia="../data/Filtrados/dias/hawai_"$j".data"
			dia_delay="../data/Filtrados/dias/hawai"$j"_delay.data"
			./filtrar_fila.sh 3 $j $infile $dia
			./tomar_columna.sh 15 $dia $dia_delay
			./tomar_promedio_columna.sh 1 $dia_delay $hawai_final
		done
afplay "audios/miami-ricardo-fort.mp3"
done