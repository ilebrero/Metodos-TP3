#!/usr/bin/env python
# -*- coding: utf-8 -*-

from scripts.utils import listfiles
import os

airport = raw_input("¿Qué aeropuerto desea filtrar? ")
#origin = raw_input("¿Desea filtrar por origen? (y/n) ")
#destination = raw_input("¿Desea filtrar por destino? (y/n) ")

os.makedirs(airport)
os.makedirs(airport + '/' + airport + 'org')
os.makedirs(airport + '/' + airport + 'dest')

files = [f for f in listfiles('./','*.csv')]
files.sort()

for f in files:

  print "termine" + f[2:]
  with open(f, 'r') as file_data:

    file_both = (airport + '/' + airport + f[2:])

    with open(file_both, 'w') as file_out:
      for line in file_data:
        line_aux = line.split(',')

        if line_aux[16] == airport or line_aux[17] == airport:
          file_out.write(line)


directory = './' + airport + '/'
files = [f for f in listfiles(directory,'*.csv')]
files.sort()

for f in files:

  print "termine" + f[9:]
  with open(f, 'r') as file_data:

    file_org = (airport + '/' + airport + 'org' + '/' + airport + f[9:]) 

    with open(file_org, 'w') as file_out:
      for line in file_data:
        line_aux = line.split(',')

        if line_aux[16] == airport:
          file_out.write(line)

for f in files:

  print "termine" + f[9:]
  with open(f, 'r') as file_data:

    file_dest = (airport + '/' + airport + 'dest' + '/' + airport + f[9:])

    with open(file_dest, 'w') as file_out:
      for line in file_data:
        line_aux = line.split(',')

        if line_aux[17] == airport:
          file_out.write(line)

os.system("cvlc ../tools/audios/delicious.mp3" )
