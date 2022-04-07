def fun():
    a="The quick Brow Fox"
    i=0
    count1=0
    count2=0
    while i<len(a):
        if a[i]>="a" and a[i]<"z":
            count1+=1
        if a[i]>="A" and a[i]<"Z":
            count2+=1
        i+=1
    print("count1",count1)
    print("count2",count2)
fun()
