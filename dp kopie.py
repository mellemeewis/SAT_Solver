import copy
import random

def dp(func, variable_values):
    clause_list = func
    variable_values = copy.deepcopy(variable_values)

    advance = True
    while advance == True:
        advance = False
        for clause in [*clause_list]:
            if len(clause) == 1:
                advance = True
                clause_list = test(clause_list, clause[0])
                variable_values.add(clause[0])
                if clause_list == -1:
                    variable_values.remove(clause[0])
                    return None
                elif len(clause_list) == 0:

                    print("FAKA KLAaR")
                    vara = list(variable_values)
                    v = []
                    for var in vara:
                        if var > 0:
                            v.append(var)
                    v.sort()
                    print(v)
                    return True

    split_value = clause_list[0][0]

    variable_values.add(split_value)
    solution = dp(test(clause_list, split_value), variable_values)

    if not solution:
        variable_values.remove(split_value)

        variable_values.add(-split_value)
        dp(test(clause_list, -split_value), variable_values)
    return variable_values

def test(clause_list, value):
    if value == None or value == 0:
        return clause_list

    clause_list = [clause for clause in clause_list if value not in clause]
    for i, clause in enumerate([*clause_list]):
        clause = [literal for literal in clause if -value != literal]
        clause_list[i] = clause
    if [] in clause_list:
        return -1
    return clause_list
