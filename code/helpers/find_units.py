def find_units(clause_list):
    if clause_list == -1:
        return []
    units = [clause[0] for clause in clause_list if len(clause) == 1]
    return units
