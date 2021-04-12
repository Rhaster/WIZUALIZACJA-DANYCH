def fun(lista):
    temp = lista[2]
    temp2=lista[3]
    g=len(lista)
    for x in range(g):
        if temp>lista[x]:
            temp=lista[x]
    for x in range(g):
        if temp2>lista[x] and lista[x]>temp:
            temp2=lista[x]
    a = [x for x in lista if x != temp and x!=temp2]
    wynik=temp*temp2
    print(wynik)
    return a
d=[5,8,4,7,6]
print(fun(d))