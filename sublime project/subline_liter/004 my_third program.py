exit = []
for c in range(10,100):
	a = c //10
	b = c % 10
	i = 10*a + b
	if i - a*b == (a+b)*3:
		exit.append(i)
print(exit)