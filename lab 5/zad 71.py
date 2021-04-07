class Wspak:
    """Iterator zwracający wartości w odwróconym porządku"""
    def __init__(self, data):
        self.data = data
        self.index = -2
        self.i=len(data)-1

    def __iter__(self):
        return self
    def __next__(self):
        if self.index >= self.i:
            raise StopIteration
        self.index = self.index+2
        return self.data[self.index]
d=(["sdasda","sdasdasd","sdsad232","dasda","dsada"])
g=(2,3,4,6,7)
d = [x for x  in Wspak(d)]
for x in Wspak(g):
    print(x)
print(d)