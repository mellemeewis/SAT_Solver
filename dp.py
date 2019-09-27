import copy
import random

def dp(func, variable_values):
    clause_list = func
    variable_values = copy.deepcopy(variable_values)

    if clause_list == -1:
        return None
    elif len(clause_list) == 0:
        answer = [var for var in list(variable_values) if var > 0]
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
                return None
            elif len(clause_list) == 0:
                answer = [var for var in list(variable_values) if var > 0]
                return answer

    # pure_literals = find_pure_literals(clause_list)
    # for literal in pure_literals:
    #     clause_list = update_clause_list(clause_list, literal)
    #     variable_values.add(literal)
    #     if clause_list == -1:
    #         variable_values.remove(literal)
    #         return None
    #     elif len(clause_list) == 0:
    #         answer = [var for var in list(variable_values) if var > 0]
    #         return answer
    #
    # units = find_units(clause_list)
    # for unit in units:
    #     clause_list = update_clause_list(clause_list, unit)
    #     variable_values.add(unit)
    #     if clause_list == -1:
    #         variable_values.remove(unit)
    #         return None
    #     elif len(clause_list) == 0:
    #         answer = [var for var in list(variable_values) if var > 0]
    #         return answer

    # advance = True
    # while advance == True:
    #     advance = False
    #     for clause in [*clause_list]:
    #         if len(clause) == 1:
    #             advance = True
    #             clause_list = update_clause_list(clause_list, clause[0])
    #             variable_values.add(clause[0])
    #             if clause_list == -1:
    #                 variable_values.remove(clause[0])
    #                 return None
    #             elif len(clause_list) == 0:
    #                 answer = [var for var in list(variable_values) if var > 0]
    #                 return answer

    # split_value = clause_list[0][0]
    split_value = DLIS(clause_list)
    variable_values.add(split_value)
    solution = dp(update_clause_list(clause_list, split_value), variable_values)
    if not solution:
        variable_values.remove(split_value)
        variable_values.add(-split_value)
        solution = dp(update_clause_list(clause_list, -split_value), variable_values)
    return solution

def find_pure_literals(clause_list):
    if clause_list == -1:
        return []
    all_literals = []
    for clause in clause_list:
        all_literals += clause
    pure_literals = set([literal for literal in all_literals if -literal not in all_literals])
    return list(pure_literals)

def find_units(clause_list):
    if clause_list == -1:
        return []
    units = [clause[0] for clause in clause_list if len(clause) == 1]
    return units

def update_clause_list(clause_list, value):
    if value is None or value == 0:
        return clause_list
    clause_list = [clause for clause in clause_list if value not in clause]
    for i, clause in enumerate([*clause_list]):
        clause = [literal for literal in clause if -value != literal]
        clause_list[i] = clause
    if [] in clause_list:
        return -1
    return clause_list

def random_split(clause_list):
    random_clause = clause_list[random.randint(0, (len(clause_list) - 1))]
    random_literal = random_clause[random.randint(0, len(random_clause) - 1)]
    return random_literal

def findliterals(clause_list):
    literals = []
    for clause in clause_list:
        for literal in clause:
            if abs(literal) not in literals:
                literals.append(literal)
    return literals


def counter(clause_list, literals):
    list_of_cp = []
    list_of_cn = []
    list_of_cp_and_cn = []
    for literal in literals:
        CP = 0
        CN = 0
        for clause in clause_list:
            for clause_literal in clause:
                if clause_literal == literal:
                    CP = CP + 1
                if clause_literal == (0 - literal):
                    CN = CN + 1
        list_of_cp.append(CP)
        list_of_cn.append(CN)
        combined = CP + CN
        list_of_cp_and_cn.append(combined)

    return list_of_cp, list_of_cn, list_of_cp_and_cn

def DLCS(clause_list):
    # Finding all possible literals
    literals = findliterals(clause_list)
    literals.sort()
    cp_list, cn_list, cp_cn_list = counter(clause_list, literals)
    maximum = max(cp_cn_list)
    index = cp_cn_list.index(maximum)
    CPv = cp_list[index]
    CNv = cn_list[index]
    if CPv > CNv:
        return literals[index]
    else:
        return 0 - literals[index]


def DLIS(clause_list):
    # Finding all possible literals
    literals = findliterals(clause_list)
    literals.sort()
    cp_list, cn_list, cp_cn_list = counter(clause_list, literals)
    if max(cp_list) > max(cn_list):
        index = cp_list.index(max(cp_list))
    else:
        index = cn_list.index(max(cn_list))
    cp = cp_list[index]
    cn = cn_list[index]
    if cp > cn:
        return literals[index]
    else:
        return 0 - literals[index]
