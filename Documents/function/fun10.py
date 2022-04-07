def reverse_fun(a):
    i=0
    while i<len(a):
        print(a[-1::-1])
        i+=1
        break
a="1234abcd"
reverse_fun(a)