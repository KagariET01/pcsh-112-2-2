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
hack input:
3 1 -
code output:
-2
currect output:
2
Ans:
B
"""
