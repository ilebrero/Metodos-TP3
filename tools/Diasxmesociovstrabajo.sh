#!/bin/bash
for i in `seq 5 8`;
do 
	infile="../data/Filtrados/orlando_200"$i"_data.csv"
	columnas="../data/Filtrados/orlando_diasDelMes_"$i".data"
	orlando_final="../data/Filtrados/resultados/orlando_diasDelMes_200"$i".data"

	./tomar_columna.sh 3 $infile $columnas
	./count_in_range.sh 1 31 $columnas $orlando_final

	infile="../data/Filtrados/washington_200"$i"_data.csv"
	columnas="../data/Filtrados/washington_diasDelMes_"$i".data"
	washington_final="../data/Filtrados/resultados/washington_diasDelMes_200"$i".data"

	./tomar_columna.sh 3 $infile $columnas
	./count_in_range.sh 1 31 $columnas $washington_final

	infile="../data/Filtrados/san_francisco_200"$i"_data.csv"
	columnas="../data/Filtrados/san_francisco_diasDelMes_"$i".data"
	san_francisco_final="../data/Filtrados/resultados/san_francisco_diasDelMes_200"$i".data"

	./tomar_columna.sh 3 $infile $columnas
	./count_in_range.sh 1 31 $columnas $san_francisco_final

	infile="../data/Filtrados/hawai_200"$i"_data.csv"
	columnas="../data/Filtrados/hawai_diasDelMes_"$i".data"
	hawai_final="../data/Filtrados/resultados/hawai_diasDelMes_200"$i".data"

	./tomar_columna.sh 3 $infile $columnas
	./count_in_range.sh 1 31 $columnas $hawai_final
done