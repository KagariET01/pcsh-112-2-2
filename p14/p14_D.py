def caesar(s):
	c=[]
	for x in s:
		c+=[chr(((ord(x)-65)%26+3)+65)]
	print(*c,sep='')

caesar("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

"""
code output:
DEFGHIJKLMNOPQRSTUVWXYZ[\]
currect output:
DEFGHIJKLMNOPQRSTUVWXYZABC
"""
