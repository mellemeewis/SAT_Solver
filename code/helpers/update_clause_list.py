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
