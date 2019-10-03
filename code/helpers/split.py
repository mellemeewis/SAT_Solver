from heuristics.DLCS import DLCS
from heuristics.DLIS import DLIS
from heuristics.JW_onesided import JW_onesided
from heuristics.MOM import MOM
from heuristics.random import random_split

def split(clause_list, strategy):
    if strategy == "DLCS":
        return DLCS(clause_list)
    if strategy == "DLIS":
        return DLIS(clause_list)
    if strategy == "Random":
        return random_split(clause_list)
    if strategy == "JW_onesided":
        return JW_onesided(clause_list)
    if strategy == "MOM":
        return MOM(clause_list)
