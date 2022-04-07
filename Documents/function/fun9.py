def unique(n):
    i=0
    l=[]
    while i<len(n):
        if n[i] not in l:
            l.append(n[i])
        i+=1
    print(l)
list=[1,2,3,3,3,4,5]
unique(list)

