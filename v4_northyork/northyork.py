# TODO: Different shift value for each Variables

import random
import time
import statistics
import pprint

class NorthYork:
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
            print("write")
            save_file.write(str(self.variables))

        self.loss = None
        # self.var_to_be_changed = 0
        self.equation_structure  = self._calcEquationStructure()
        # self.shift_value = 1
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

    def breed(self, gene_one, gene_two):
        # print((gene_one, gene_two))
        new_gene = []
        for i in range(0, len(gene_one)):
            if random.getrandbits(1):
                new_gene.append(gene_one[i])
            else:
                new_gene.append(gene_two[i])
        # print(new_gene)
        return new_gene

    def mutate(self, gene, mutation_level=None):
        # print("m " + str(gene))
        if mutation_level == None:
            mutation_level = random.randint(0, 50)
        orig_mutation_level = mutation_level

        while not mutation_level <= 0:

            new_gene = []
            for j in range(0, len(gene)):
                dna_to_change = random.randint(0, len(gene))
                if dna_to_change == j:
                    change_level = random.randint(0, round(orig_mutation_level / 10))
                    mutation_level -= change_level
                    if random.getrandbits(1):
                        change_level *= -1
                    new_gene.append(mutation_level + change_level)
                else:
                    new_gene.append(gene[j])
            gene = new_gene
            # print(mutation_level)
        # print("n " + str(new_gene))
        return new_gene

    def train(self, training_data, mutation_value):
        if self.done_train_steps == 0:
            if not self.input_data_num == 1:
                var_num = self.input_data_num * 4 + 3
            else:
                var_num = 3

            variables = []
            for i in range(0, 1000):
                variable = []
                for i in range(0, var_num):
                    variable.append(random.randint(-5, 5))
                variables.append(variable)


        while True:
            # print(variables)
            variables_results = []
            for variable in variables:
                losses = []
                # print(variable)
                for j in training_data:
                    # print(variable)
                    # print(variable)
                    losses.append(abs(j[1] - self.calculate(j[0], variable)))

                variables_results.append((variable, statistics.mean(losses)))

            variables = variables_results


            variables.sort(key=lambda x: x[1])
            # variables.reverse()
            # print(len(variables))
            # pprint.pprint(variables)
            print("Step: " + str(self.done_train_steps + 1) + " Loss: " + str(variables[0][1]) + " Variable: " + str(variables[0][0]))
            continue_vars = []
            for i in range(0, len(variables)):
                if random.randint(0, len(variables)) > i:
                    continue_vars.append(variables[i])
                # print("random")
            if len(continue_vars) % 2 == 1:
                # print("reduce")
                continue_vars = continue_vars[:-1]
            new_genes = []
            # print(len(continue_vars))
            # print(continue_vars)
            for i in range(0, int(len(continue_vars) / 2)):
                gene_one = continue_vars.pop(0)[0]
                gene_two = continue_vars.pop(-1)[0]
                new_genes.append(self.breed(gene_one, gene_two))
                # print("breed")

            new_genes.append(variables[0][0])

            while len(new_genes) < 1000:
                # print(len(new_genes))
                # print("mutate")


                # mutated_variables = self.mutate(continue_vars[random.randint(0, len(continue_vars)) - 1][0], mutation_value)
                # print(mutated_variables)
                # new_genes.append(mutated_variables)

                # new_genes.append(self.mutate(new_genes[random.randint(0, len(new_genes)) - 1], mutation_value))
                new_genes.append(self.breed(new_genes[random.randint(0, len(new_genes)) - 1], new_genes[random.randint(0, len(new_genes)) - 1]))

                # print("mutated")

            # while len(new_genes) < 1000:
            #     # print(len(new_genes))
            #     variable = []
            #     for i in range(0, var_num):
            #         variable.append(random.randint(-5, 5))
            #     new_genes.append(variable)

            variables = new_genes
            # pprint.pprint(variables)
            self.done_train_steps += 1
            # print("done")


    def calculate(self, input_data, variables=None):
        if variables == None:
            variables = self.variables[:]
        var_scan_pos = 0
        input_data_scan_pos = 0
        final_calculation = 0

        for i in self.equation_structure[:]:
            if len(i) == 1:

                # final_calculation += variables[var_scan_pos] * input_data[input_data_scan_pos] ** variables[var_scan_pos + 1]
                # print(variables)
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

        # print("calc")
        return final_calculation
