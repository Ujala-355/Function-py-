def add():
	a=int(input('enter'))
	i=3
	sum=0
	while i<=a:
		if i%3==0 or i%5==0:
			sum+=i
			print(sum)
		i+=1
add()