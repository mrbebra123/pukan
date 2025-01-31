def supertranslate(chislo):
	cifras = []
	while chislo > 0:
		i = chislo % 10
		chislo = chislo - i
		chislo = int(chislo / 10)
		cifras.append(i)
	return(cifras)

# функ. которая 1,2,3 = 123.
def returntranslate(cifras):

	# перевернём массив чтобы легчебыло считат сумму.
	cifras = cifras[::-1]
	# перебераю разряды.

	b = 1
	exit_cifra = 0

	for cifra in cifras:
		
		exit_cifra += cifra * b
		b = b*10