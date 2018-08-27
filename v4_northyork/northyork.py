# TODO: Different shift value for each Variables

import random
import time
import statistics

class CampLuther:
    def __init__(self, input_data_num, save, target_loss=1):
        self.input_data_num = input_data_num

        try:
            save_file = open(save, "r")
            self.variables = eval(save_file.read())
        except Exception as e:
            print(str(e))
            self.variables = []

            if not input_data_num == 1:
                var_num = self.input_data_num * 4 + 3
            else:
                var_num = 3

            for i in range(0, var_num):
                self.variables.append(random.randint(0, 50))
                # self.variables.append(0)

            save_file = open(save, "w")
            save_file.write(str(self.variables))

        self.loss = None
        self.var_to_be_changed = 0
        self.equation_structure  = self._calcEquationStructure()
        self.shift_value = 1
        self.done_train_steps = 0
        self.target_loss = target_loss
        self.save = save

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

    def train(self):
        pass

    def calculate(self, input_data, variables=None):
        if variables == None:
            variables = self.variables[:]
        var_scan_pos = 0
        input_data_scan_pos = 0
        final_calculation = 0

        for i in self.equation_structure[:]:
            if len(i) == 1:

                # final_calculation += variables[var_scan_pos] * input_data[input_data_scan_pos] ** variables[var_scan_pos + 1]
                final_calculation += variables[var_scan_pos] * input_data[input_data_scan_pos]

                var_scan_pos += 2
                input_data_scan_pos += 1
            else:
                # # print(i)
                bubble_calculation = 0
                for j in i:
                    # # print(input_data_scan_pos)
                    # # print(input_data[j])


                    # bubble_calculation += variables[var_scan_pos] * input_data[j] ** variables[var_scan_pos + 1]
                    bubble_calculation += variables[var_scan_pos] * input_data[j]

                    # # print(bubble_calculation)
                    var_scan_pos += 2
                    input_data_scan_pos += 1
                # print(bubble_calculation)
                # print(variables[var_scan_pos + 1])
                # print(variables[var_scan_pos])


                # bubble_calculation = bubble_calculation * variables[var_scan_pos] ** variables[var_scan_pos + 1]
                bubble_calculation = bubble_calculation * variables[var_scan_pos]


                # print(bubble_calculation)
                final_calculation += bubble_calculation
                # print(final_calculation)

            final_calculation += variables[-1]
            # print(final_calculation)

        return final_calculation
