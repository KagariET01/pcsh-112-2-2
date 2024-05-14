def caesar(s):
	c=[]
	for x in s:
		c+=[chr(((ord(x)-65+3)%26)+65)]
	print(*c,sep='')

caesar("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

"""
code & currect output:
DEFGHIJKLMNOPQRSTUVWXYZABC
"""
