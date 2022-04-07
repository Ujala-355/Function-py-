def perfect_number(num):
    i=1
    while i<=num:
        b=i
        j=1
        sum=0
        while j<i:
            if b%j==0:
                sum+=j
            j+=1
        if sum==b:
            print("perfect number")
            break
        i+=1
num=int(input("enter a number"))
perfect_number(num)   
