import csv 
import json
import unicodedata

import googlemaps
from datetime import datetime

gmaps = googlemaps.Client(key='AIzaSyAv6cAFu6Z19mnwdF2_PUFkpOJWmQwA7Xs ')


latUndLong = []
with open('equipamentos-de-monitoramento-e-ficalizacao.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile, delimiter=';', quotechar='|')
    for row in reader:
        latUndLong.append(row[0])

# print latUndLong #ok

lUndLInt = []
c = []
contador = 0
for i in latUndLong:
    if contador != 0 : #['Peso', 'Nome']
        c = i.split(',')
        lUndLInt.append( [float(c[0]) ,float(c[1])] ) #nome peso
        c = []
    contador += 1


nomeDasRuas = []
for coordenada in lUndLInt :

    reverse_geocode_result = gmaps.reverse_geocode((coordenada[0],coordenada[1]))
    nome = reverse_geocode_result[0]['address_components'][1]['long_name']

    nome = unicodedata.normalize('NFKD', nome).encode('ascii','ignore') #transformando em string
    nomeDasRuas.append(nome)

#print nomeDasRuas #Apenas nome de ruas

nameUndpeso = []
with open('pesos.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile, delimiter=';', quotechar='|')
    for row in reader:
        nameUndpeso.append([row[1],row[0]]) # name , peso
# print nameUndpeso #ok

dicionario = {}
#print type(nameUndpeso[1][0]) # endereco , 0 nome 1 peso
tamanho = len(nameUndpeso)
x = 0
while x != tamanho:
    if nameUndpeso[x][1] != 'Peso':
        dicionario[nameUndpeso[x][0]] =  int(nameUndpeso[x][1])
    x += 1

#print dicionario
#print dicionario['Avenida Recife'] # PESO TA COMO STRING


for i in nomeDasRuas:
    if i in dicionario.keys():
        dicionario[i]-=1
    else:
        dicionario[i] = -1

for j in dicionario:
    str(dicionario[j])


with open('pesosfinaisfinais.json', 'w') as fp:
    json.dump(dicionario, fp)

