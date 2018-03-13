sepal_len = [(6.4, 3), (5.0, 2), (4.9, 3), (4.9, 1), (5.7, 1)]
sepal_wid = [(2.8, 3), (2.3, 2), (2.5, 3), (3.1, 1), (3.8, 1)]
petal_len = [(5.6, 3), (3.3, 2), (4.5, 3), (1.5, 1), (1.7, 1)]
petal_wid = [(2.2, 3), (1.0, 2), (1.7, 3), (0.1, 1), (0.3, 1)]
choices = {1: "setosa", 2: "versicolor", 3: "virginica"}

import sys
import statistics
sys.path.insert(0, '..')

import grouse_final as gf
# print(gf.grouse(sepal_len, [1, 2, 3], float(input("Sepal length: "))))
# print(gf.grouse(sepal_wid, [1, 2, 3], float(input("Sepal width: "))))
# print(gf.grouse(petal_len, [1, 2, 3], float(input("Petal length: "))))
# print(gf.grouse(petal_wid, [1, 2, 3], float(input("Petal width: "))))

predict_x = [
	[5.1, 5.9, 6.9],
	[3.3, 3.0, 3.1],
	[1.7, 4.2, 5.4],
	[0.5, 1.5, 2.1]
]

for i in range(0, len(predict_x[0])):
	responses = []
	responses.append(gf.grouse(sepal_len, [1, 2, 3], predict_x[0][i]))
	responses.append(gf.grouse(sepal_wid, [1, 2, 3], predict_x[1][i]))
	responses.append(gf.grouse(petal_len, [1, 2, 3], predict_x[2][i]))
	responses.append(gf.grouse(petal_wid, [1, 2, 3], predict_x[3][i]))
	responses_abstract = [i[0] for i in responses]
	chosen = statistics.mode(responses_abstract)
	sure = [i[1] for i in responses if chosen == i[0]]
	# print(responses)
	# print(responses_abstract)
	print(choices[chosen] + " - " + str(statistics.mean(sure)) + "% sure.")