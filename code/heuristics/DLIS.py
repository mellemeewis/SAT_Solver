from helpers.find_literals import find_literals
from helpers.counter import counter


def DLIS(clause_list):
    # Finding all possible literals
    literals = find_literals(clause_list)
    literals.sort()
    cp_list, cn_list, cp_cn_list = counter(clause_list, literals)

    if max(cp_list) > max(cn_list):
        index = cp_list.index(max(cp_list))
    else:
        index = cn_list.index(max(cn_list))
    cp = cp_list[index]
    cn = cn_list[index]
    if cp > cn:
        return literals[index]
    else:
        return 0 - literals[index]
