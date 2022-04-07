def fun():
    b="hello my"," name is ujala"
    k="".join(b)
    f=k.split()
    i=0
    while i<len(f):
        j=0
        while j<len(f[i]):
            print(f[i],len(f[i]))
            break
        i+=1
    print("Total length:",i)
fun()
