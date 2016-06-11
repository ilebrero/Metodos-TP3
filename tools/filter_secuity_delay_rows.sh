#!/bin/bash
# Filtrar por par origen - destino usando awk.

# Definimos algunas variables. Ojo que a bash no le gustan los espacios cerca del "=".
infile1998="../data/1998.csv"
infile1999="../data/1999.csv"
infile2000="../data/2000.csv"
infile2001="../data/2001.csv"
infile2002="../data/2002.csv"
infile2003="../data/2003.csv"

outfile1998="../data/airport_security_delay_1998.csv"
outfile1999="../data/airport_security_delay_1999.csv"
outfile2000="../data/airport_security_delay_2000.csv"
outfile2001="../data/airport_security_delay_2001.csv"
outfile2002="../data/airport_security_delay_2002.csv"
outfile2003="../data/airport_security_delay_2003.csv"

security_ap="NA"
security_apcero="0" 

# Columna 17 aeropuerto origen, columna 18 aeropuerto destino
# Ojo con la secuencia de " y ' al filtrar por &&. 
awk -F, '$28 != "'"$security_ap"'" && $28 != "'"$security_apcero"'"' $infile1998 > $outfile1998
awk -F, '$28 != "'"$security_ap"'" && $28 != "'"$security_apcero"'"' $infile1999 > $outfile1999
awk -F, '$28 != "'"$security_ap"'" && $28 != "'"$security_apcero"'"' $infile2000 > $outfile2000
awk -F, '$28 != "'"$security_ap"'" && $28 != "'"$security_apcero"'"' $infile2001 > $outfile2001
awk -F, '$28 != "'"$security_ap"'" && $28 != "'"$security_apcero"'"' $infile2002 > $outfile2002
awk -F, '$28 != "'"$security_ap"'" && $28 != "'"$security_apcero"'"' $infile2003 > $outfile2003
