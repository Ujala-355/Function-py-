def num(user):
    i=0
    while i<=user:
        if i%2==0:
            print(i,"even number")
        else:
            print(i,"odd number")
        i+=1
number=int(input("enter a number"))
num(number)