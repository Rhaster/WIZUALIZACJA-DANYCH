A=[1/x for x in range(1,10)]
B=[2**i for i in range(int(0.5), 11)]
C=[ i for i in B if i % 4 == 0]
print(A)
print(B)
print(C)