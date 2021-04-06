class Wspak:
    def __init__(self, data):
        self.data = data
        self.index = len(data)
    def __iter__(self):
        if self.index %2 == 0:
            return self
    def __next__(self):
        if self.index == 0:
            raise StopIteration
        elif self.index %2 == 0:
            return self.data[self.index]
d=("sdasda","sdasdasd","sdsad232")
print([a for a in Wspak(d)])
print([a for a in Wspak("hodaa")])