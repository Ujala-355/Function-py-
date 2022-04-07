def max_num(a,b,c):
    if b<a>c:
        print("max",a)
    elif a<b>c:
        print("max",b)
    elif a<c>b:
        print("max",c)
a=int(input("enter a num"))
b=int(input("enter a num"))
c=int(input("enter a num"))
max_num(a,b,c)
