import random
import time

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

    def train_core(self, training_data=None, quiet=False, delay=0):
        for i in training_data:
            try:
                target_reached_status = self.loss < self.target_loss
            except:
                target_reached_status = False
            # last_vars = None
            last_loss = None
            while not target_reached_status:
                error = None
                try:
                    higher_equation_result = self.calculate(i[0], self.higherEquation())
                    higher_equation_loss = abs(higher_equation_result - i[1])
                except:
                    error = "h"
                try:
                    lower_equation_result = self.calculate(i[0], self.lowerEquation())
                    lower_equation_loss = abs(lower_equation_result - i[1])
                except:
                    error = "l"
                if not error == None:
                    if error == "l":
                        self.variables = self.higherEquation()
                        self.loss = higher_equation_loss
                    else:
                        self.variables = self.lowerEquation()
                        self.loss = lower_equation_loss
                else:
                    if higher_equation_loss < lower_equation_loss:
                        self.variables = self.higherEquation()
                        self.loss = higher_equation_loss
                    else:
                        self.variables = self.lowerEquation()
                        self.loss = lower_equation_loss

                if self.var_to_be_changed == len(self.variables) - 1:
                    self.var_to_be_changed = 0
                # elif self.var_to_be_changed = 0:
                #     if not last_vars == None:
                #         if last_vars == self.variables:
                #             self.shift_value /= 10
                #     print(last_vars)
                #     last_vars = self.variables
                else:
                    self.var_to_be_changed += 1

                # print(last_loss)

                # if not last_loss == None:
                #     # print(abs(last_loss - self.loss))
                #     # print(self.shift_value)
                #     # if abs(last_loss - self.loss) < (self.shift_value):
                #     if self.loss < (self.shift_value):
                #         self.shift_value /= 10
                #         # print(self.shift_value)
                #     # elif last_loss == self.loss:
                #     #     self.shift_value /= 2
                #     elif self.loss > (self.shift_value * 10):
                #         self.shift_value *= 10

                if self.loss < self.shift_value:
                    self.shift_value /= 10

                last_loss = self.loss

                self.done_train_steps += 1
                if not quiet:
                    print("Step " + str(self.done_train_steps) + " done. Loss: " + str(self.loss) + " Last Loss: " + str(last_loss) + " Shift Value: " + str(self.shift_value) + " Variables: " + str(self.variables))
                    pass
                if str(self.done_train_steps)[-5:] == "00000":
                    save_file = open(self.save, "w")
                    save_file.write(str(self.variables))

                time.sleep(delay)


    def train(self, train_steps=None, traning_data=None, quiet=False, delay=0):
        # if train_steps == None:
        #     iterObj = True
        # else:
        #     iterObj = range(0, train_steps)
        # while iterObj:
        #     self.train_one(traning_data, quiet, delay)
        print(quiet)
        self.train_core(traning_data, quiet, delay)

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
