def caesar(s):
	c=[]
	for x in s:
		c+=[chr((ord(x)+3)%26)]
	print(*c,sep='')

caesar("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

"""
code output:
 	


currect output:
DEFGHIJKLMNOPQRSTUVWXYZABC
"""
