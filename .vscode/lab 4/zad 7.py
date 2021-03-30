class robot():
    def __init__(self,x,y):
        self.x=x
        self.y=y
        krok=1
        self.k=krok
    def idzwgore(self,ile):
        g=self.k*ile
        self.y=self.y+g
    def idzwdol(self,ile):
        g=self.k*ile
        self.y=self.y-g
    def idzwprawo(self,ile):
        g=self.k*ile
        self.x=self.x+g
    def idzwlewo(self,ile):
        g=self.k*ile
        self.x=self.x-g
    def pokaz_gdzie_jestes(self):
        print(self.x,self.y)
    def __del__(self):
        print("SYSTEMY W STANIE KRYTYCZNYM")
x=robot(0,0)
print(x.idzwdol(3))
print(x.pokaz_gdzie_jestes())
print(x.idzwlewo(4))
print(x.pokaz_gdzie_jestes())
print(x.idzwlewo(1))
print(x.pokaz_gdzie_jestes())
print(x.idzwprawo(6))
print(x.pokaz_gdzie_jestes())
print(x.idzwgore(4))
print(x.pokaz_gdzie_jestes())
print(x.idzwgore(4))
print(x.pokaz_gdzie_jestes())