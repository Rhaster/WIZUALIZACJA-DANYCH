def diament(levels=3, symbol='o'): 
    ciag = [x for x in range(1, levels+1, 2)]
    ciag += ciag[-2::-1]
    for elem in ciag:
        print(f'{​​​​​symbol * elem:^9}​​​​​')
print(diament())
