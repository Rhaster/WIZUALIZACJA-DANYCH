def cos(data):
    d=len(data)-1
    h=data
    samogloski = ('a', 'e', 'i', 'y', 'o', 'u')
    if isinstance(h,str)=="false":
        yield "none"
    for x in range(d+1):
        if (h[x] in samogloski)==1: 
            yield h[x]

##g=("dasdadasdayu")
##d = [x for x  in Wspak(g)]
##print(d)
gen = cos("adaFau")
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
