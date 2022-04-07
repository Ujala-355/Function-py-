def vote(user):
	if user>=18:
		print('eligible vote')
	else:
		print('not eligible')
a=int(input('enter'))
vote(a)