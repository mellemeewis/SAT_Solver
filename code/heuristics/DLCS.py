from helpers.find_literals import find_literals
from helpers.counter import counter

def DLCS(clause_list):
    # Finding all possible literals
    literals = find_literals(clause_list)
    literals.sort()
    cp_list, cn_list, cp_cn_list = counter(clause_list, literals)
    maximum = max(cp_cn_list)
    index = cp_cn_list.index(maximum)
    CPv = cp_list[index]
    CNv = cn_list[index]
    if CPv > CNv:
        return literals[index]
    else:
        return 0 - literals[index]
