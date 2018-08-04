import random

class CampLuther:
    def __init__(self, input_data_num):
        self.input_data_num = input_data_num
        self.mode = None
        self.variables = []

        if not input_data_num == 1:
            var_num = self.input_data_num * 4 + 3
        else:
            var_num = 3

        for i in range(0, var_num):
            self.variables.append(random.randint(0, 10))

        self.loss = None
        self.var_to_be_changed = 0
        self.equation_structure  = self._calcEquationStructure()
        self.shift_value = 1

    def _calcEquationStructure(self):
        # for cur_len in range(1, self.input_data_num + 1):
        #     for cur_place in range(0, self.input_data_num):
        equation_structure = []
        for i in range(0, self.input_data_num):
            equation_structure.append([i])
        equation_structure.append([j[0] for j in equation_structure])
        return equation_structure


    def higherEquation(self):
        newVar = self.variables[:]
        newVar.insert(self.var_to_be_changed, newVar.pop(self.var_to_be_changed) + self.shift_value)
        return newVar

    def lowerEquation(self):
        newVar = self.variables[:]
        newVar.insert(self.var_to_be_changed, newVar.pop(self.var_to_be_changed) - self.shift_value)
        return newVar

    def train_one(self, training_data=None):
        pass

    def train(self, train_steps=None, traning_data=None):
        if train_steps == None:
            iterObj = True
        else:
            iterObj = range(0, train_steps)
        while iterObj:
            train_one(traning_data)

    def calculate(self, input_data, variables=None):
        if variables == None:
            variables = self.variables[:]
        var_scan_pos = 0
        input_data_scan_pos = 0
        final_calculation = 0

        for i in self.equation_structure[:]:
            if len(i) == 1:
                final_calculation += variables[var_scan_pos] * input_data[input_data_scan_pos] ** variables[var_scan_pos + 1]
                var_scan_pos += 2
                input_data_scan_pos += 1
            else:
                # # print(i)
                bubble_calculation = 0
                for j in i:
                    # # print(input_data_scan_pos)
                    # # print(input_data[j])
                    bubble_calculation += variables[var_scan_pos] * input_data[j] ** variables[var_scan_pos + 1]
                    # # print(bubble_calculation)
                    var_scan_pos += 2
                    input_data_scan_pos += 1
                # print(bubble_calculation)
                # print(variables[var_scan_pos + 1])
                # print(variables[var_scan_pos])
                bubble_calculation = bubble_calculation * variables[var_scan_pos] ** variables[var_scan_pos + 1]
                # print(bubble_calculation)
                final_calculation += bubble_calculation
                # print(final_calculation)

            final_calculation += variables[-1]
            # print(final_calculation)

        return final_calculation
