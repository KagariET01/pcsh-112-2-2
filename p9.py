def G(n,m):
	if n<10:
		if m<10:
			return n+m
		else:
			return G(n,m-2)+m
	else:
		return G(n-1,m)+n
	
print(G(11,12))

"""
output:
60
Ans:
A
"""
