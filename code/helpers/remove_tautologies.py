def remove_tautologies(clause_list):
    clause_list = [clause for clause in clause_list if not is_tautology(clause)]
    return clause_list

def is_tautology(clause):
    for literal in clause:
        if -literal in clause:
            return True
    return False
