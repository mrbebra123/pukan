exit = []
p = 1000
for c in range(1,p):
	a = c //10
	b = c % 10
	i = 10*a + b
	
	if i == (a+b)*2:
		exit.append(i)
print(exit)