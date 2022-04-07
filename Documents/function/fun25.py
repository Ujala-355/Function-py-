def num():
	number=[1,4,5,0]
	i=0
	n=[]
	while i<len(number):
		if number[i]!=0:
			n.append(number[i])
		i=i+1
	print(n)
num()