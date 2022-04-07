def add():
	l=[[0],[1,3],[5,7],[9,11],[13,15,17]]
	i=0
	count=0
	while i<len(l):
		j=1
		while j<len(l):
			if len(l[i])>len(l[j]):
				max=(l[i])
				count+=1
			j+=1
		i+=1
	i=0
	mini=0
	count1=0
	while i<len(l):
		k=0
		while k<len(l):
			if l[i]<l[i]:
				mini=l[i]
			k+=1
		i+=1
	print((count,max))
	print((count1,[mini]))
add()