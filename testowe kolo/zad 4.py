def znajdz(lista):
    lista.sort()
    g=len(lista)
    return lista[g:g-4:-1]
h=[1,3,4,5,8,2,6,1]
print(znajdz(h))