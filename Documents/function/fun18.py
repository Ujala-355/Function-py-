from re import I


def square():
    i=1
    m1=[]
    m2=[]
    while i<=5:
        a=i*i
        m1.append(a)
        i+=1
    j=26
    while j<=30:
        b=j*j
        m2.append(b)
        j+=1
    print(m1,m2)
square()