import random

class Whiterock:
    def __init__(self, data, equation):
        self.data = data
        self.equation = equation # &*@+@

    def train(self, save):
        try:
            trainFile = open("save/" + save, "r")
            trainData = trainFile.read()
            trainFile.close()
            trainData = eval(trainData)
        except:
            trainData = []
            for i in self.equation.count("@"):
                trainData.append(random.randint(-9, 10))
            trainFile = open("save/" + save, "w")
            trainFile.write(trainData)
            trainFile.close()
        
