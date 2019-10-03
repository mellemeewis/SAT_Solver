import copy
import random
import sys

from helpers.find_units import find_units
from helpers.find_pure_literals import find_pure_literals
from helpers.update_clause_list import update_clause_list
from helpers.split import split

class Solver():
    def __init__(self):
        self.splits = 0
        self.conflicts = 0
# Davis Putnam algorithm based on certain heuristic that determines how to split
    def dp(self, func, variable_values, strategy):
        print("Start new recursion")
        print("Splits:", self.splits)
        if self.splits == 1000:
            print("NO SOLUTION FOUND")
            print("Splits:", self.splits)
            print("Conflicts:", self.conflicts)
            sys.exit(1)
        clause_list = func
        variable_values = copy.deepcopy(variable_values)

        if clause_list == -1:
            return [None, None, self.splits, self.conflicts]
            return None
        elif len(clause_list) == 0:
            answer_all = list(variable_values)
            answer_pos = [var for var in answer_all if var > 0]
            answer = [answer_pos, answer_all, self.splits, self.conflicts]
            return answer

        advance = True
        while advance == True:
            advance = False
            units = find_units(clause_list)
            pure_literals = find_pure_literals(clause_list)
            literals = units + pure_literals
            for literal in literals:
                advance = True
                clause_list = update_clause_list(clause_list, literal)
                variable_values.add(literal)
                if clause_list == -1:
                    variable_values.remove(literal)
                    return [None, None, self.splits, self.conflicts]
                    return None
                elif len(clause_list) == 0:
                    answer_all = list(variable_values)
                    answer_pos = [var for var in answer_all if var > 0]
                    answer = [answer_pos, answer_all, self.splits, self.conflicts]
                    return answer

        split_value = split(clause_list, strategy)
        # print('Split value is', split_value)
        self.splits += 1

        variable_values.add(split_value)
        solution = self.dp(update_clause_list(clause_list, split_value), variable_values, strategy)

        if not solution[0]:
            # print('Conflict!')
            self.conflicts += 1
            variable_values.remove(split_value)
            variable_values.add(-split_value)
            solution = self.dp(update_clause_list(clause_list, -split_value), variable_values, strategy)
        return solution
