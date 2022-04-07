def add(n):
	i=1
	c=0
	while i<=a:
		if n%i==0:
			c+=1
		i+=1
	if c==2:
		print('prime number',n)
	else:
		print('not prime number',n)
	i+=1
a=int(input('enter'))
add(a)