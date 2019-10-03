def find_pure_literals(clause_list):
    if clause_list == -1:
        return []
    all_literals = []
    for clause in clause_list:
        all_literals += clause
    pure_literals = set([literal for literal in all_literals if -literal not in all_literals])
    return list(pure_literals)
