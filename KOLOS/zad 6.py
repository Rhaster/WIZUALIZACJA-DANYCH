def zad6(n,symbol):
    if(n%2==0):
        return
    f=1
    for x in range(0,n):
        print("_"*x+ symbol*1)
        f+=1
    f-=3
    for x in range(n-1,0,-1):
        print("_"*f+ symbol*1)
        f-=1
n=int(input(" liczba"))
u=input("podaj znak")
zad6(n,u)