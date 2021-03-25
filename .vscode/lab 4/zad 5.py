class ciagi():
    def __init__(self,a1,r,ile):
        self.a=a1
        self.r=r
        self.n=ile
    def wyświetl_dane(self):
        print(self.a,self.a+self.r,self.a+2*self.r)
    def pobierz_elementy(self):
        lista=[]
        g=self.a
        for x in range(0,self.n):
            lista.append(g)
            g+=self.r 
        print(lista)
    def policzsume(self): 
        j=self.a
        suma=0
        for x in range (0,self.n):
            suma+=j
            j+=self.r         
        print(suma)
d=ciagi(1,2,3)
print(d.pobierz_elementy())
print(d.policzsume())
print(d.wyświetl_dane())