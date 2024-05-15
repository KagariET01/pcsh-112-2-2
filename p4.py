s=input().split()
st=[]
for x in s:
	if x=='+':
		st+=[st.pop()+st.pop()]
	elif x=='-':
		st+=[st.pop()-st.pop()]
	elif x=='*':
		st+=[st.pop()*st.pop()]
	elif x=='/':
		st+=[st.pop()/st.pop()] #before: st+=[st.pop()/st.pop())]
	else:
		st+=[int(x)]
print(st.pop())

"""
hack input 1:
3 1 -
code output 1:
-2
currect output 1:
2
hack input 2:
3 1 /
code output 2:
0.3333333333333333
currect output 2:
3
Ans:
C
"""
