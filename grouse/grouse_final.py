import statistics

def learn(data):
	a = []
	m = []
	for example, target in data:
		m.append(example // target)
		a.append(example - (example // target) * target)
	return statistics.harmonic_mean(m), statistics.harmonic_mean(a)

def grouse(data, choices, inputData):
	d, s = learn(data)
	if d == 0:
		d = 1
	calc = inputData / d - s
	# print(calc)
	answer = min(choices, key=lambda x: abs(x - calc))
	# print()
	diff = (list(choices)[1] - list(choices)[0])
	return answer, (abs(answer - calc) / diff) * 100

# inputData = int(input("Input data: "))