from Usuari import Usuari
import csv
import sys

try:
    filename = sys.argv[1]
except IndexError as e:
    print("ERROR: " + e.args[0])
    exit(1)
with open(filename, "r", encoding="utf-8") as f:
    files = list(csv.reader(f, delimiter=';'))

usuaris = list()
for fila in files:
    usuaris.append(Usuari(*fila))

for usuari in usuaris:
    usuari.crearUsuari()