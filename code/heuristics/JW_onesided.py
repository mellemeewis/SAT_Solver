from helpers.find_literals import find_literals

def JW_onesided(clause_list):
    literals = find_literals(clause_list)
    literals.sort()
    all_J = []
    for literal in literals:
        j = 0
        for clause in clause_list:
            if literal in clause:
                j = j + (2**(0 - len(clause)))
        all_J.append(j)
    max_j = max(all_J)
    index = all_J.index(max_j)
    return literals[index]
