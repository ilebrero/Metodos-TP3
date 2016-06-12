#!/bin/bash
# cuenta valores en un archivo por rango

# --- Datos --- #
# $1 valor  	#
# $2 entrada    #
# $3 salida     #
#################

grep -c "$1" $(find $2 -type f -print0 | xargs -0 echo) >> $3
