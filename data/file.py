
with open('2005.csv', 'r') as f:
  f.readline()
  line = f.readline()
  l = line.split(',')
  tiempo = int(l[5][:2])
  print tiempo
###  for line in f:
###    line_aux = line.split(',')
###    if 0 <= int(line_aux[5]) <= 10:
###      print line_aux[5]
###
