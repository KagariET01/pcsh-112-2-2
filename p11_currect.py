def gcd(a,b):
	if a<b:
		a,b=b,a
	if b==0:
		return a
	r=a%b
	return gcd(b,r)

print(gcd(2,1))
