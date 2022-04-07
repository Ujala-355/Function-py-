from re import I


def add(a,b):
    c=a+b
    return c
def sub(d,e):
    i=d-e
    return i
def add_sub():
    k=add(10,15)
    g=sub(78,90)
    return k,g
print(add_sub())