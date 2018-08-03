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

    def train_core(self, training_data=None, quiet=False, delay=0):
        try:
            target_reached_status = self.loss < self.target_loss
        except:
            target_reached_status = False
        # last_vars = None
        last_loss = None
        last_checkpoint_loss = None
        locked_var = []
        while not target_reached_status:
            error = ""
            try:
                higher_equation_losses = []
                for i in training_data:
                    higher_equation_result = self.calculate(i[0], self.higherEquation())
                    higher_equation_losses.append(abs(higher_equation_result - i[1]))
                higher_equation_loss = statistics.mean(higher_equation_losses)
            except:
                error = error + "h"
            try:
                lower_equation_losses = []
                for i in training_data:
                    lower_equation_result = self.calculate(i[0], self.lowerEquation())
                    lower_equation_losses.append(abs(lower_equation_result - i[1]))
                lower_equation_loss = statistics.mean(lower_equation_losses)
            except:
                error = error + "l"
            # print(error)
            # if self.loss == None:
            #     self.loss = statistics.mean((higher_equation_loss, lower_equation_loss)) ** 2
            #
            # if higher_equation_loss > self.loss and lower_equation_loss > self.loss and self.var_to_be_changed not in locked_var:
            #     # self.shift_value /= 10
            #     locked_var.append(self.var_to_be_changed)
            if False:
                pass
            elif not error == "":
                if error == "l":
                    self.variables = self.higherEquation()
                    self.loss = higher_equation_loss
                elif error == "h":
                    self.variables = self.lowerEquation()
                    self.loss = lower_equation_loss
                else:
                    self.shift_value /= 10
                    locked_var = []
            else:
                if not self.var_to_be_changed in locked_var:
                    if higher_equation_loss < lower_equation_loss:
                        self.variables = self.higherEquation()
                        self.loss = higher_equation_loss
                    else:
                        self.variables = self.lowerEquation()
                        self.loss = lower_equation_loss

            if not last_loss == None:
                if self.loss - last_loss > 0 and not self.var_to_be_changed in locked_var:
                    locked_var.append(self.var_to_be_changed)
                    self.shift_value /= 1

            if self.var_to_be_changed == len(self.variables) - 1:
                self.var_to_be_changed = 0

                if not last_loss == None:
                    # if abs(self.loss) < self.shift_value :
                    # if round(self.loss, len(str(1 / self.shift_value))) - round(last_loss, len(str(1 / self.shift_value))) == float(0):
                    if self.loss < self.shift_value:
                        self.shift_value /= 10
                        self.loss == None
                        locked_var = []

            if len(locked_var) == len(self.variables):
                locked_var = []
                self.shift_value /= 10
                self.loss == None

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

            last_loss = self.loss

            print(locked_var)


            self.done_train_steps += 1
            if not quiet:
                # print("Step " + str(self.done_train_steps) + " done. Loss: " + str(self.loss) + " Last Loss: " + str(last_loss) + " Shift Value: " + str(self.shift_value) + " Variables: " + str(self.variables))
                print("Step " + str(self.done_train_steps) + " done. Loss: " + str(self.loss) + " Last Loss: " + str(last_loss) + " Shift Value: " + str(self.shift_value) + " Variables: " + str(self.variables))
            if str(self.done_train_steps)[-5:] == "00000":
                save_file = open(self.save, "w")
                save_file.write(str(self.variables))

            # if str(self.done_train_steps)[-5:] == "00000":
            #     if not last_checkpoint_loss == None:
            #         # if last_checkpoint_loss - self.loss < self.shift_value * 10:
            #         if self.loss > 0.5:
            #         # if False:
            #             if not self.input_data_num == 1:
            #                 var_num = self.input_data_num * 4 + 3
            #             else:
            #                 var_num = 3
            #
            #             self.variables = []
            #             for i in range(0, var_num):
            #                 self.variables.append(random.randint(0, 50))
            #             last_checkpoint_loss = None
            #             # pass
            #         else:
            #             last_checkpoint_loss = self.loss
            #     else:
            #         last_checkpoint_loss = self.loss

            if str(self.done_train_steps)[-3:] == "000":
                # if self.var_to_be_changed == 0 and not last_checkpoint_loss == 0:
                if not last_checkpoint_loss == None:
                    print(self.loss)
                    print(last_checkpoint_loss)
                    if last_checkpoint_loss - self.loss < self.shift_value:
                        print("locked var reset")
                        locked_var = []

                last_checkpoint_loss = self.loss

                # time.sleep(3)


            time.sleep(delay)

    def trainRough(self, training_data):
        record_loss = (None, self.variables)
        while True:
            for k in range(0, 1000):
                if not self.input_data_num == 1:
                    var_num = self.input_data_num * 4 + 3
                else:
                    var_num = 3

                variables = []
                for i in range(0, var_num):
                    variables.append(random.randint(-5, 6))

                equation_losses = []
                for i in training_data:
                    equation_result = self.calculate(i[0], variables)
                    equation_losses.append(abs(equation_result - i[1]))
                equation_loss = statistics.mean(equation_losses)

                if record_loss[0] == None:
                    record_loss = (equation_loss, variables)
                    self.variables = variables
                    print(record_loss)
                elif record_loss[0] > equation_loss:
                    record_loss = (equation_loss, variables)
                    self.variables = variables
                    print(record_loss)

                save_file = open(self.save, "w")
                save_file.write(str(self.variables))

    def maybeRough():
        pass


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
