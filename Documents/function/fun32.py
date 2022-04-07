def add(l):
	i=0
	c=0
	c1=0
	while i<len(l):
		if l[i]>0:
			c+=1
		else:
			c1+=1
		i+=1
	print(c,'positive')
	print(c1,'negative')
l=[2,-7,5,-64,-14]
add(l)