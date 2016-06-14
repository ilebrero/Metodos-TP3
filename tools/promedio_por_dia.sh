# $1 lugar
# $2 código
# $3 año
# $4 entrada/salida

mkdir ../data/filtrados/resultados/$1_$2_porcentaje_por_dia_$4

python porcentaje_delay_por_dia.py ../data/filtrados/$1_$2_$4/$1_$2_$3_$4.csv ../data/filtrados/resultados/$1_$2_porcentaje_por_dia_$4/$1_$2_porcentaje_por_dia_$3 $4
