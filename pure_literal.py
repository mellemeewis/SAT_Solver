def check_for_pure_literals(clause_list, variable_list):
    pure_literals = []
    for clause in clause_list:
        for literal in clause.list:
            is_pure_literal = True
            i = 0
            while is_pure_literal == True and i < len(clause_list):
                for clause_1 in clause_list:
                    i += 1
                    if clause_1.contains_varible:
                        for literal_1 in clause_1.list:
                            if literal.direction != literal_1.direction and abs(literal.value) == abs(literal_1.value):
                                is_pure_literal = False
            if is_pure_literal == True:
                pure_literals.append(literal.value)
    pure_literals = set(pure_literals)

    for literal in pure_literals:
        if literal < 0:
            for variable in variable_list:
                if abs(literal) == variable.literal:
                    variable.truth_value = False
        else:
            for variable in variable_list:
                if literal == variable.literal:
                    variable.truth_value = True
