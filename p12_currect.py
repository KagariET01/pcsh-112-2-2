def factor(n):
	fs=[1]
	for f in range(2,int(n**0.5)+1):
		if n%f==0:
			fs+=[f]
			if(n//f!=f):
				fs+=[n//f]
			else:
				break
	print(len(fs))

factor(2401)
