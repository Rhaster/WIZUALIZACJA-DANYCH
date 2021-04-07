def fibo(data):
    ile=data
    a=0
    b=1
    for x in range(ile):
        yield a
        a=a+b
        yield b
        b=b+a
print(list(fibo(int(6/2))))
    
