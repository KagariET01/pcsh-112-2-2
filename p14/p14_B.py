def caesar(s):
	c=[]
	for x in s:
		c+=[chr(ord(x)+3)]
	print(*c,sep='')

caesar("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

"""
code output:
DEFGHIJKLMNOPQRSTUVWXYZ[\]
currect output:
DEFGHIJKLMNOPQRSTUVWXYZABC
"""
