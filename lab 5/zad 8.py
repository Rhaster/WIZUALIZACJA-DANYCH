
class Wspak:
    def __init__(self, data):
        self.data = data
        self.index = 0
        self.d=len(data)-1
    def __iter__(self):
        return self
    def __next__(self):
        samogloski = ('a', 'e', 'i', 'y', 'o', 'u')
        if isinstance(self.data,str)=="false":
            raise StopIteration
        if self.index > self.d:
            raise StopIteration
        if (self.data[self.index] in samogloski)==1: 
            self.index+=1
            return self.data[self.index-1]
        self.index+=1
##g=("dasdadasdayu")
##d = [x for x  in Wspak(g)]
##print(d)
d=Wspak("gggayuga")
for x in d:
    print(x) 