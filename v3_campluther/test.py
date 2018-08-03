from campluther import CampLuther
import random

def gen_train_set():
    total_train_set = []
    for i in range(0, 2):
        current_train_set = []
        for j in range(0, 3):
            current_train_set.append(random.randint(1, 1000))
        total_train_set.append([current_train_set, current_train_set[0]])
    return total_train_set

ML = CampLuther(3, "./testSave", 100)
print(ML.equation_structure)
print(ML.variables)
# print(gen_train_set())
print(ML.train(None, gen_train_set(), delay=0, quiet=False))
print(ML.calculate([1, 2, 3]))
print(ML.calculate([9, 2, 3]))
