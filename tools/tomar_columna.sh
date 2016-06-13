#!/bin/bash
# tomar una columna usando cut.

#ojo que en $0 hay un parametro del sistema implicito

# -- Datos -- #
# $1 columna  #
# $2 entrada  #
# $3 salida   #
###############

# -f indica que columnas, "-d," significa "delimitador es una ','".
echo "tomando columna "$1
cut -f$1 -d, $2 > $3