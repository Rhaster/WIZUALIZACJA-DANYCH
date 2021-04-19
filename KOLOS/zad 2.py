def zad2(a=(input("podaj"))):
    txt_list=a.replace(",",'').replace(".",'').split(" ")
    print(txt_list)
    txt_list.sort()
    print(txt_list)
zad2()