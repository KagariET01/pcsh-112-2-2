def G(a,x):
	if x==0:
		return 2
	else:
		return a*G(a,x-1)
	
print(G(2,6))

"""
output:
128
Ans:
C
"""
