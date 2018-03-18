import csv 

import unicodedata

import googlemaps
from datetime import datetime

gmaps = googlemaps.Client(key='AIzaSyAv6cAFu6Z19mnwdF2_PUFkpOJWmQwA7Xs ')


latUndLong = []
with open('acidentes-2016.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile, delimiter=';', quotechar='|')
    for row in reader:
        latUndLong.append(row[0])

##print type(latUndLong)
##print latUndLong


lUndLInt = []
c = []
contador = 0
for i in latUndLong:
    if contador != 0 :
        c = i.split(',')
        lUndLInt.append( [float(c[0]) ,float(c[1])] )
        c = []
    contador += 1

##print lUndLInt

##print type(lUndLInt[0][0])
##print lUndLInt[0][0],lUndLInt[0][1]

#mar = 0

#f = open('nomes.txt', 'w')
nomeDasRuas = []
for coordenada in lUndLInt :
    ##print coordenada[1], coordenada[0]
#    if mar < 2 :
            # Look up an address with reverse geocoding
    reverse_geocode_result = gmaps.reverse_geocode((coordenada[1],coordenada[0]))

           ## print reverse_geocode_result[0]['address_components'][1]['long_name']
    nome = reverse_geocode_result[0]['address_components'][1]['long_name']

    nome = unicodedata.normalize('NFKD', nome).encode('ascii','ignore')
            #print type(nome)
    nomeDasRuas.append(nome)
        #f.write(nome)
        ##f.write(';')
        ##f.write(str(float(coordenada[1])))
        ##f.write(';')
        ##f.write(str(float(coordenada[0])))
        ##f.write('\n') 
#    mar += 1
#print nomeDasRuas
#f.write(nomeDasRuas)  # python will convert \n to os.linesep
#f.close()  # you can omit in most cases as the destructor will call it

#print nomeDasRuas

augusto = []
naoaguentomais = []

for i in nomeDasRuas:
     if i not in augusto:
       augusto.append(nomeDasRuas.count(i))
       naoaguentomais.append(i)

print type(augusto[0])
print type(naoaguentomais[0])


qntd = len(augusto)

fo = open('pesos.txt', 'w')
xuxa = 0
while qntd > 0 :

    fo.write(str(augusto[xuxa]))
    fo.write(';')
    fo.write(naoaguentomais[xuxa])
    fo.write('\n')
    qntd -= 1
    xuxa += 1

fo.close()
