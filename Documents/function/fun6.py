def character(a,b):
    i=0
    while i<len(a) and i<len(b):
        if len(a)>len(b):
            print(a)
            break
        elif len(a)<len(b):
            print(b)
            break
        else:
            print(a,b)
            break
        i+=1
character(input("enter a first name"),input('enter a secod name'))
    