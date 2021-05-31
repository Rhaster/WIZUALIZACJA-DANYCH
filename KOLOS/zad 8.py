def zad8(text):
    o= open('A-M_nazwiska.txt', 'w+')
    p='A Ą B C Ć D E Ę F G H I J K L Ł M'
    y=p.split(' ')
    L='N Ń O Ó P R S Ś T U W Y Z Ź Ż'
    M=L.split(' ')
    print(M)
    for j in range(len(text)):
	    for x in range(len(y)):
            if text[j][0] in y[x]:
                print(text[j])
    for j in range(len(text)):
	    for x in range(len(y)):
            if text[j][0] in M[x]:
                vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvprint(text[j])

text =["Grzechownia","Dybala","Mostkowiak","Zytni"] #cos sie psuje nie wiem co chca te spacje da pan z 1 pkt ;d 
zad8(text)