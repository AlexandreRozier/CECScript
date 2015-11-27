# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 12:56:56 2015

@author: hx
"""

import csv
import requests
import itertools
import lxml




# On ouvre le fichier contenant les données
csvfile = open('adresses.csv', 'r')
reader = csv.reader(csvfile, delimiter=';')
row_count = sum(1 for row in csvfile)
csvfile.seek(0)

# Les tableaux contenant les données
numeros = []
rues = []
villes = []
codesPostaux = []

# On itère sur chaque ligne du fichier pour entrer les données dans les tableaux créés ci-desssus
for row in itertools.islice(reader, 1, row_count):
    numeros.append(row[0])
    rues.append(row[1])
    villes.append(row[2])
    codesPostaux.append(row[3])

adresse = "http://sig.ville.gouv.fr/recherche-adresses-qp-polville"

r = requests.post(adresse, data={'@num_adresse': numeros[0], '@nom_voie': rues[0], '@nom_commune': villes[0],'@code_postal': codesPostaux[0]})
print(r.text)

tree = lxml.etree.parse("data.xml")
for user in tree.xpath("/users/user/nom"):
    print(user.text)