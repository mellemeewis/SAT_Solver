def check_for_pure_literals(clause_list, variable_list):
    changes_made = 0
    pure_literals = []
    for variable in variable_list:
        if variable.truth_value != None:
            continue
        direction_found = None
        is_pure_literal = True
        for clause in clause_list:
            if clause.contains_varible:
                for literal in clause.list:
                    if abs(literal.value) == variable.literal:
                        if direction_found == None:
                            direction_found = literal.direction
                        elif direction_found != literal.direction:
                            is_pure_literal = False
            if is_pure_literal == False:
                break
        if is_pure_literal == True:
            changes_made = 1
            if direction_found == 0:
                pure_literals.append(0 - variable.literal)
            else:
                pure_literals.append(variable.literal)

    for literal in pure_literals:
        if literal < 0:
            for variable in variable_list:
                if abs(literal) == variable.literal:
                    variable.truth_value = False
        else:
            for variable in variable_list:
                if literal == variable.literal:
                    variable.truth_value = True
    return changes_made
