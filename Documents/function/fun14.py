def count():
    list=["gyh","xyz","aba","1221"]
    i=0
    c=1
    while i<len(list):
        if list[i]>="a" and list[i]<="z":
            list[i].split()
        if list[i]>="1" and list[i]<="9":
            c+=1
            print("count",c)
        i+=1
count()
