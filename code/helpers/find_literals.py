def find_literals(clause_list):
    literals = []
    for clause in clause_list:
        for literal in clause:
            if abs(literal) not in literals:
                literals.append(abs(literal))
    return literals
