def tri(n):
	if n!=0:
		tri(n//3)
		print(n%3,end='')

tri(10)
print()
tri(100)

"""
code & currect output:
101
10201
"""
