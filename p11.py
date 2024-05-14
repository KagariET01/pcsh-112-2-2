def gcd(a,b):
	if a<b:
		a,b=b,a
	r=a%b
	if b==0:
		return a
	return gcd(b,r)

print(gcd(2,1))

"""
hack:
gcd(2,1)
code output:
[RUNTIME ERROR]
PS /home/kagariet01/worksp/bugs> python3 p11.py
Traceback (most recent call last):
  File "/home/kagariet01/worksp/bugs/p11.py", line 9, in <module>
    gcd(2,1)
  File "/home/kagariet01/worksp/bugs/p11.py", line 7, in gcd
    return gcd(b,r)
  File "/home/kagariet01/worksp/bugs/p11.py", line 4, in gcd
    r=a%b
ZeroDivisionError: integer division or modulo by zero
currect output:
1
Ans:
B
"""
