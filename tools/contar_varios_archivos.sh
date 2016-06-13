#!/bin/bash
# Filtrar por input usando awk.

# -------------- Datos ------------------------------------ #
# $1 nombre del lugar del aeropuerto (ej: orlando)          #
# $2 es el dato a tener en cuenta para comparación (ej: MCO)#
# $3 entrada/salida                                         #                 
############################################################

  mkdir ../data/filtrados/$1_$2_$3 #crea carpeta para guardar datos filtrados
for i in `seq 5 8`;
do
  in="../data/200"$i".csv"
  out="../data/filtrados/"$1"_"$2"_"$3"/"$1"_"$2"_200"$i"_"$3".csv" 
  
  #Entrada 18 - Salida 17
  if [ "$3" = "entrada" ]; then
    n=18
  else
    n=17
  fi
  ./generic_filter.sh $n $2 $in $out  #pone en out un archivo filtrando los vuelos de aeropuerto $2

  #filtro la columna día
  aux="../data/auxiliar.csv" #guardo en la variable la k-ésima columna del archivo
  ./tomar_columna.sh 4 $out $aux

  mkdir ../data/filtrados/resultados/$1_$2_por_dia_contar_$3 #carpeta donde se guarda la cantidad final
  outfile="../data/filtrados/resultados/"$1"_"$2"_por_dia_contar_"$3"/"$1"_"$2"_por_dia_200"$i".csv" 
  #ejecuto el comando que cuenta
  for j in `seq 1 7`;
  do
    ./count.sh $j $aux $outfile 
  done
  rm ../data/auxiliar.csv
  echo terminó el año 200$i
done  
