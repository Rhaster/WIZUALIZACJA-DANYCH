import sys
d=int(input("podaj pierwsza liczbe napisz ale nie wiecej niz 10"))
while(d>10):
    d=int(input("podaj pierwsza liczbe napisz ale nie wiecej niz 10"))
    if d>10:
        print("do widzenia")
for x in range(1,d,1):
    print("A")
    for y in range(x,0,-1):
        sys.stdout.write('A')
 #       :D 