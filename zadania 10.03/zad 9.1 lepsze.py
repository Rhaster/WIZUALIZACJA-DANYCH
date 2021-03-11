d=input("podaj licze")
suma=0
for x in d:
    if d.isnumeric():
        suma+= int(x)
print(suma)