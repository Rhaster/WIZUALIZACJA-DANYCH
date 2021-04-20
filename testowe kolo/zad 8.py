def goha(a=(input("podaj"))):
    d=input("podaj nazwe")
    open(d,"w")
    text=a.lower()
    txt_list=text.replace(",",'').replace(".",'').split(" ")
    j=str
    t=len(txt_list)
    print(t)
    print(txt_list)
    for x in range(0,-1):
        for j in range(1,t-1):
            print(txt_list[j])
            print(txt_list[x])
            if txt_list[x]==txt_list[j]:
                txt_list.pop(j)
    with open(d,"w") as g:
        g.writelines('/n'.join([word for word in txt_list if txt_list.count(word)==1]))
    print(txt_list)
goha()
