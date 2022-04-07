def add():
	i=0
	while i<4:
		a=int(input('enter'))
		if a%3==0 and a%5==0:
			print('fizz Buzz')
		elif a%3==0:
			print('fizz')
		elif a%5==0:
			print('buzz')
		else:
			print(a)
		i+=1
add()   