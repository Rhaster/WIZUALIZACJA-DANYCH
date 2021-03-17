    
d=int(input("liczba < 9 i > 3"))
f=1
u=int(d/2)
for x in range(d,u,-1):
    print(" "*int(x-u)+ "o"*f)
    f+=2
if(d%2!=0):
    f-=4
    g=2
else:
    f-=2
    g=1
for j in range(g,u+g,1):
    print(" "*j+ "o"*f)
    f-=2 
