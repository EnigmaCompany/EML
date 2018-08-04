"""
This is a Python implementation of the Iris classification problem.
The problem could be found here: https://www.tensorflow.org/get_started/get_started_for_beginners
This program doesn't use Tensorflow or any other machine learning libraries other than Grouse.
Comments start with '##'

2018 Mar 13 Paul Lee (Enigma, Xx-Enigma-xX, wole07)
"""

import requests, pprint

# sepal_len = [(6.4, 3), (5.0, 2), (4.9, 3), (4.9, 1), (5.7, 1)]
# sepal_wid = [(2.8, 3), (2.3, 2), (2.5, 3), (3.1, 1), (3.8, 1)]
# petal_len = [(5.6, 3), (3.3, 2), (4.5, 3), (1.5, 1), (1.7, 1)]
# petal_wid = [(2.2, 3), (1.0, 2), (1.7, 3), (0.1, 1), (0.3, 1)]

## get data from online source
choices = {1: "Iris-setosa", 2: "Iris-versicolor", 3: "Iris-virginica"}

inv_choices = {v: k for k, v in choices.items()}
lists = [[], [], [], []]
data = requests.get('https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data').text
data = [i.split(",") for i in data.strip("\n").split("\n")]
# print(data)
for i in range(0, len(data[0]) - 1):
	for j in data:
		lists[i].append((float(j[i]), int(inv_choices[j[4]])))

# for i in lists:
# 	pprint.pprint(i)
# 	print("====================")

## put the data into four lists
sepal_len = lists[0]
sepal_wid = lists[1]
petal_len = lists[2]
petal_wid = lists[3]

import sys
import statistics
sys.path.insert(0, '..')

## imports the grouse lib
import grouse_final as gf
# print(gf.grouse(sepal_len, [1, 2, 3], float(input("Sepal length: "))))
# print(gf.grouse(sepal_wid, [1, 2, 3], float(input("Sepal width: "))))
# print(gf.grouse(petal_len, [1, 2, 3], float(input("Petal length: "))))
# print(gf.grouse(petal_wid, [1, 2, 3], float(input("Petal width: "))))

## test cases
predict_x = [
	[5.1, 5.9, 6.9],
	[3.3, 3.0, 3.1],
	[1.7, 4.2, 5.4],
	[0.5, 1.5, 2.1]
]

predict_x = [
	[6.3],
	[2.5],
	[5.0],
	[1.9]
]

## iterate over test cases' columns
for i in range(0, len(predict_x[0])):
	## get prdictions from grouse lib
	responses = []
	responses.append(gf.grouse(sepal_len, [1, 2, 3], predict_x[0][i]))
	responses.append(gf.grouse(sepal_wid, [1, 2, 3], predict_x[1][i]))
	responses.append(gf.grouse(petal_len, [1, 2, 3], predict_x[2][i]))
	responses.append(gf.grouse(petal_wid, [1, 2, 3], predict_x[3][i]))
	responses_abstract = [i[0] for i in responses]
	# chosen = statistics.mode(responses_abstract)

	## if the response was [(2, 2), (1, 4), (2, 3)]
	## after this the new_responses will be [(2, 2.5), (1, 4)]
	computed = []
	new_responses = []
	for i in responses:
		computed.append(i[0])
		filtered = [j for j in responses if j[0] == i[0]]
		filtered_pos = [i[1] for i in filtered]
		for i in filtered:
			responses.remove(i)
		new_responses.append((i[0], statistics.mean(filtered_pos)))
	new_responses.sort(key=lambda x: x[1])
	## select the item with the biggest possibility
	chosen = new_responses[-1]
	# sure = [i[1] for i in responses if chosen == i[0]]
	# print(responses)
	# print(responses_abstract)
	# print(choices[chosen] + " - " + str(statistics.mean(sure)) + "% sure.")

	## print results
	print(choices[chosen[0]] + " - " + str(chosen[1]) + "% sure.")