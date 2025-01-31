a = 0
b = 1
excute = []
for c in range(99):
	i = 10*b + a
	if a > 9:
		a = 0
		b+=1
	if (a + b)+(a*b) == i :
		excute.append(i)
	a+=1
print (excute)