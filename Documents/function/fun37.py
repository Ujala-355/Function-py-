def add():
	l=[10,14,2,23,19]
	i=0
	max=0
	secondmax=0
	while i<len(l):
		if l[i]>max:
			max=l[i]
		else:
			secondmax=l[i]
		i+=1
	print('max',max)
	print('secondmax',secondmax)
	print('total',max+secondmax)
add()