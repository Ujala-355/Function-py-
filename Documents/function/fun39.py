def add():
	l=[4,6,2,1,9,63,-134,566]
	i=0
	max=0
	while i<len(l):
		if l[i]>max:
			max=l[i]
		i+=1
	print(max)
add()