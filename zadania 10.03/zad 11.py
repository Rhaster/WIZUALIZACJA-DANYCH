
d=int(input("liczba < 9 i > 3"))
while d>9 or d<3:
    d=int(input("liczba < 9 i > 3"))
f=1
u=int(d/2)
for x in range(d,int(d/2),-1):
    print(" "*int(x-u)+ "o"*f)
    f+=2
if(d%2!=0):
    f-=4
    for j in range(2,int(d/2)+2,1):
        print(" "*j+ "o"*f)
        f-=2 
else:
    f-=2
    for j in range(1,int(d/2)+1,1):
        print(" "*j+ "o"*f)
        f-=2 
        
