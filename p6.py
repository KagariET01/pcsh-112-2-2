def g(a):
	if a>1:
		return g(a-2)+3
	return a

print(g(12))

"""
output:
18
Ans:
B
"""
