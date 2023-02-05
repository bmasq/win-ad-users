from Usuari import Usuari
import csv

with open("usuaris.csv", "r") as f:
    files = list(csv.reader(f, delimiter=';'))

usuaris = list()
for fila in files:
    usuaris.append(Usuari(*fila))

for usuari in usuaris:
    usuari.crearUsuari()