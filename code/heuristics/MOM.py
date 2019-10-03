from helpers.find_literals import find_literals

def MOM(clause_list):
    lengths = []
    for clause in clause_list:
        lengths.append(len(clause))
    minimum = min(lengths)

    small_clauses = []
    for clause in clause_list:
        if len(clause) == minimum:
            small_clauses.append(clause)

    literals = find_literals(small_clauses)
    literals.sort()
    MOMs = []
    for literal in literals:
        fx = 0
        f_x = 0
        for clause in small_clauses:
            if literal in clause:
                fx = fx + 1
            if 0 - literal in clause:
                f_x = f_x + 1
        mom = (fx + f_x) * 2**2 + fx + f_x
        MOMs.append(mom)
    maximum = max(MOMs)
    index = MOMs.index(maximum)
    return literals[index]
