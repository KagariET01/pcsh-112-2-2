num=[3,1,4,1,5,9,2,6,5,3,5]
for i,n in enumerate(num):
	for k in range(5):
		if i-k==n:
			print('PCSH')

"""
output:
PCSH
PCSH
PCSH
PCSH
PCSH
Ans:
D
"""
