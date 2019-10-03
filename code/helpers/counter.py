def counter(clause_list, literals):
    list_of_cp = []
    list_of_cn = []
    list_of_cp_and_cn = []
    for literal in literals:
        CP = 0
        CN = 0
        for clause in clause_list:
            for clause_literal in clause:
                if clause_literal == literal:
                    CP = CP + 1
                if clause_literal == (0 - literal):
                    CN = CN + 1
        list_of_cp.append(CP)
        list_of_cn.append(CN)
        combined = CP + CN
        list_of_cp_and_cn.append(combined)

    return list_of_cp, list_of_cn, list_of_cp_and_cn
