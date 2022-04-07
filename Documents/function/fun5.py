def num(speed):
    point=(speed-70)//5
    if speed<=70:
        print("ok")
    elif speed>=70 and speed<=130:
        print("point=",point)
    elif speed>=130:
        print("point=",point,"License suspended")
number=int(input("enter a number"))
num(number)