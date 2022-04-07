def add(l):
	i=0
	m=[]
	while i<len(l):
		a=l[i]%10
		b=l[i]//10
		d=a+b
		m.append(d)
		i+=1
	print(m)
k=[12,67,98,34]
add(k)