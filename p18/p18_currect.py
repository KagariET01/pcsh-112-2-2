n=int(input())
s=[]
check=14*60+20
for _ in range(n):
	name=input()
	time=list(map(int,input().split()))
	st=time[0]*60+time[1]
	if st>check:
		t=(time[2]-time[0])*60+(time[3]-time[1])
		s+=[name,t]
print(*s,sep='\n')

"""
input:
3
KUNG FU PANDA 4
13 30 12 10
Godzilla x Kong
15 20 17 20
The Cat Returns
17 10 18 30
example output:
Godzilla x Kong
125
The Cat Returns
73
code & currect output:
Godzilla x Kong
120
The Cat Returns
80
"""
