import statistics

# data = [(100, 1), (150, 1), (200, 2), (250, 2), (300, 3), (350, 3), (300, 3)]
# choices = {1: "Skinny", 2: "Normal", 3: "Fat"}

# data = [(12, 1), (18, 1), (23, 1), (33, 2), (38, 2), (29, 2), (43, 3), (47, 3), (60, 3), (50, 3), (55, 3)]
# choices = {1: "Young", 2: "Middle", 3: "Old"}

data = [(60, 2), (70, 2), (80, 2), (40, 1), (45, 1), (50, 1)]
choices = {1: "Light", 2: "Heavy"}

def learn(data):
	# if a == None and m == None:
	#
	# elif not (a == None or m == None):
	# 	pass
	# else:
	# 	raise ValueError("I need both Addition and Multiply lists.")
	a = []
	m = []
	for example, target in data:
		m.append(example // target)
		a.append(example - (example // target) * target)
	# print(m)
	# print(a)
	# return [(m[i], a[i])for i in range(0, len(a))]
	return statistics.harmonic_mean(m), statistics.harmonic_mean(a)

d, s = learn(data)
inputData = int(input("Input data: "))
calc = inputData / d - s
# print(calc)
answer = min(choices, key=lambda x:abs(x-calc))
print(choices[answer])
diff = (list(choices.keys())[1] - list(choices.keys())[0])
print(str(((abs(answer - calc) / diff) * 100)) + "% Sure")

# print(choices.keys())
# print(list(choices.keys())[1] - list(choices.keys())[0])