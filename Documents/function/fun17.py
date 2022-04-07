def function():
    l=["shubhkirti","vikas","vishal"]
    i=0
    while i<len(l):
        j=0
        c=0
        while j<len(l[i]):
            c+=1
            j+=1
        print(l[i],c)
        i+=1
function()