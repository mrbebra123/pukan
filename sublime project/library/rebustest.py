# входные
from pickle import NONE


rebus = "ВАНЯ+МАК=УЖАС"
makes = ["-","+","="]
# программа
havemakes = []
simvols = []
words = []
first_simvols = []
b = 0

# первый символ!!!!!!!!!!!!!!!!!!!!
first_simvols.append(rebus[0])

# переменная добавдения в массив слов/(временная)
thinkstr = ""
for i in range(len(rebus)):
	simvol = rebus[i]
	if simvol not in makes:
		# если перед нами буква
		thinkstr = thinkstr+simvol
		if simvol not in simvols:
			# если сивол еще не в массиве символов
			simvols.append(simvol)
	else:
		# если перед нами действие
		first_simvols.append(rebus[i+1])
		words.append(thinkstr)
		thinkstr = ""
		havemakes.append(simvol)
words.append(thinkstr)

# перебор on!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# создаю массив, который будет наполнен чисслами
def magic(path):
	# если массив достаточной длины, останови перебор
	if len(path) == len(simvols):
		return
	# иначе дополни массив всеми возможными вариантами
	else:
		for i in range(10):
			path.append(i)
			print(path)
			magic(path)
			path.pop()

magic([])

# выход

print(rebus)
print(simvols)
print(havemakes)
print(words)
print(first_simvols)