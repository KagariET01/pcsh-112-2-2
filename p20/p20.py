k,n=map(int,input().split())
p=list(map(int,input().split()))
m=input()
t=[sum(p[x-1] for x in map(int,input().split()))
		for _ in range(n)]

"""
input:
6 3
5 10 15 20 25 30
3 4 2
1 2 3
1 2 4 5
5 6
example & currect output:
1 30
Ans:
C
"""
