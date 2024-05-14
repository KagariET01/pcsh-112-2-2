def factor(n):
	fs=[1]
	for f in range(2,int(n**0.5)+1):
		if n%f==0:
			fs+=[f,n//f]
	print(len(fs))

factor(2401)

"""
code output:
5
currect output:
4
Ans:
A
"""
