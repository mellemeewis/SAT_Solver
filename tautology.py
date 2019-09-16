def check_for_tautology(clause_list):
    clauses_to_be_removed = []
    for clause in clause_list:
        present_literals = []
        for literal in clause.list:
            if literal.value > 0:
                if (0 - literal.value) in present_literals:
                    clauses_to_be_removed.append(clause)
                else:
                    present_literals.append(literal.value)
            else:
                if abs(literal.value) in present_literals:
                    clauses_to_be_removed.append(clause)
                else:
                    present_literals.append(literal.value)

    for clasue in clauses_to_be_removed:
        print(clasue)
    for clause in clauses_to_be_removed:
        clause_list.remove(clause)
