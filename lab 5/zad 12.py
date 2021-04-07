def pol(data):
    g=("styczeń","luty", "marzec", "kwiecień","maj", "czerwiec", "lipiec","sierpień",  "wrzesień", "październik","listopad","grudzień")
    h=[x for x in  g]
    d=data-1
    for x in range(12):
        if(x==d):
            yield h[d]
g=("styczeń","luty", "marzec", "kwiecień","maj", "czerwiec", "lipiec","sierpień",  "wrzesień", "październik","listopad","grudzień")
x=[x for x in  g]
y=9
print(list(pol(y)))