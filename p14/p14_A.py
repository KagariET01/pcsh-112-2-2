def caesar(s):
	c=[]
	for x in s:
		c+=[chr(x+3)]
	print(*c,sep='')

caesar("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

"""
code output:
[RUNTIME ERROR]
PS /home/kagariet01/worksp/bugs> python3 p14/p14_A.py
Traceback (most recent call last):
  File "/home/kagariet01/worksp/bugs/p14/p14_A.py", line 7, in <module>
    print(caesar("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
  File "/home/kagariet01/worksp/bugs/p14/p14_A.py", line 4, in caesar
    c+=[chr(x+3)]
TypeError: can only concatenate str (not "int") to str
currect output:
DEFGHIJKLMNOPQRSTUVWXYZABC
"""
