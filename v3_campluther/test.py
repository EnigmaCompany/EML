from campluther import CampLuther
import random

def gen_train_set():
    total_train_set = []
    for i in range(-5, 6):
        current_train_set = []
        for j in range(0, 3):
            current_train_set.append(random.randint(1, 5000))
        total_train_set.append([current_train_set, current_train_set[0]])
    return total_train_set

ML = CampLuther(3, "./testSave", 100)
print(ML.equation_structure)
print(ML.variables)
# print(gen_train_set())
# print(ML.train(None, gen_train_set(), delay=0, quiet=False))
# print(ML.trainRough(gen_train_set()))
print(ML.calculate([1, 2, 3], [-4, 1, 1, 2, 2, 4, -5, -2, 1, -1, 2, -5, -1, 1, 0]))
print(ML.calculate([9, 2, 3], [-4, 1, 1, 2, 2, 4, -5, -2, 1, -1, 2, -5, -1, 1, 0]))
correct_and_false = [0, 0]
# [1, -4, 2, -2, 6, -5, 0, 2, -1, -1, -3, 5, 2, -3, 0]
# [-4, 1, 1, 2, 2, 4, -5, -2, 1, -1, 2, -5, -1, 1, 0]

for i in gen_train_set():
    if ML.calculate(i[0], [1, -4, 2, -2, 6, -5, 0, 2, -1, -1, -3, 5, 2, -3, 0]) == i[1]:
        correct_and_false = [correct_and_false[0] + 1, correct_and_false[1]]
    else:
        correct_and_false = [correct_and_false[0], correct_and_false[1] + 1]


print(ML.calculate([1234567890, 2, 3]))


print(correct_and_false)
