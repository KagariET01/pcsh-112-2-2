k,n=map(int,input().split())
p=list(map(int,input().split()))
m=input()
t=[sum(p[x-1] for x in map(int,input().split()))
		for _ in range(n)]
print(t.index(min(t)-1),min(t))

"""
input:
6 3
5 10 15 20 25 30
3 4 2
1 2 3
1 2 4 5
5 6
code output:
[RUNTIME ERROR]
kagariet01@server2:~/worksp/bugs/p20$ python3 p20_B.py < p20.in
Traceback (most recent call last):
  File "/home/kagariet01/worksp/bugs/p20/p20_B.py", line 6, in <module>
    print(t.index(min(t)-1),min(t))
ValueError: 29 is not in list
example & currect output:
1 30
"""
