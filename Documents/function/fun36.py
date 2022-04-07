def add(a):
	i=1
	count=0
	while i<a:
		j=1
		c=0
		while j<=i:
			if i%j==0:
				c+=1
			j+=1
		if c==2:
			print(i,'prime')
			count+=1
		i+=1
n=int(input('enter'))
add(n)