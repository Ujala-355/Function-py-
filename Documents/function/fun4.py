def parameter(limet):
    i=0
    sum=0
    while i<=limet:
        if i%3==0 or i%5==0:
            sum+=i
            print(sum)
        i+=1
limet=int(input("enter a limet"))
parameter(limet)