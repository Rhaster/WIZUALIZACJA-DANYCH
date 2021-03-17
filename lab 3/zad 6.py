def row(a = 1, b = 1, x = 1, y = 1):
    return ((x-a)**2+(y-b)**2)**0.5

a=int(input("podaj a"))
b=int(input("podaj b"))
x=int(input("podaj x"))
y=int(input("podaj y"))
print(row(float(a),float(b),float(x),float(y)))