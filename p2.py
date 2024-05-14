for _ in range(int(input())):
	s=[]
	c=0
	for x in input():
		if x=='(':
			s+=[x]
		elif s:
			s.pop()
			c+=1
	if not s:
		print(c)
	else:
		print(0)

"""
input:
3
()()
(()))
((())
code output:
2
2
0
currect output:
2
0
0
Ans:
B
"""
