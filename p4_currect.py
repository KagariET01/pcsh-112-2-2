s=input().split()
st=[]
for x in s:
	if x=='+':
		st+=[st.pop()+st.pop()]
	elif x=='-':
		st+=[-(st.pop()-st.pop())]
	elif x=='*':
		st+=[st.pop()*st.pop()]
	elif x=='/':
		st+=[st.pop()/st.pop()] #before: st+=[st.pop()/st.pop())]
	else:
		st+=[int(x)]
print(st.pop())
