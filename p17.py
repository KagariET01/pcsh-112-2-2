def fibonacci(n):
	fibonacci.i+=1
	if n==0 or n==1:
		return n
	return fibonacci(n-1)+fibonacci(n-2)
fibonacci.i=0
fibonacci(8)
print(fibonacci.i)

"""
output:
67
Ans:
C
"""
