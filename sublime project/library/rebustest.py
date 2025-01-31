# входные
rebus = "ВАНЯ+МАК=УЖАС"
makes = ["-","+","="]
# программа
havemakes = []
simvols = []
words = []

thinkstr = ""
for simvol in rebus:
	if simvol not in makes:
		# если перед нами буква
		thinkstr = thinkstr+simvol
		if simvol not in simvols:
			# если сивол еще не в массиве символов
			simvols.append(simvol)
	else:
		# если перед нами действие
		words.append(thinkstr)
		thinkstr = ""
		havemakes.append(simvol)
words.append(thinkstr)
# выход
print(simvols)
print(words)
print(havemakes)