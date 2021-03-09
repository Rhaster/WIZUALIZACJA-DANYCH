import sys
a = input("podaj zdanie kappa") #zad 1
print(a.count(" "))
b = int(input("podaj a"))  #zad 2 bez readline i write
c = int(input("podaj b"))
g = c*b 
print(g)
s = int(sys.stdin.readline())#zad 2 z readline
t = int(sys.stdin.readline())
h=s*t
sys.stdout.write("Value is %s" % h)
h = int(input("podaj h wartosc bezwzgledna")) #zad 3 
print(abs(h))
