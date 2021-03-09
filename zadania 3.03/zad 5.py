x = int(input("podaj a")) # zad 5
if x > 10 and x > 0:
    print("liczba jest spoza przedzialu")
    k=0
else:
    k=1
y = int(input("podaj liczbe 2"))
z = int(input("podaj liczbe 3")) 
if x >y and y>z and k==1 :
    print("warujek jest spelniony")
else:
    print("wszystkie warunki nie sa spelnione")