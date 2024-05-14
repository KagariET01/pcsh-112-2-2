n=int(input())
for _ in range(n):
	c=[0]*4
	for x in map(int,input().split()):
		c[x-1]+=1
		print(min(c))

"""
input:
3
1 2 3 4 1 2 4 1
2 2 2 3 1 4 4 3 3 1
1 1 1 4 4 3 1
code output:
0
0
0
1
1
1
1
1
0
0
0
0
0
1
1
1
1
2
0
0
0
0
0
0
0
example & currect output:
1
2
0
"""
