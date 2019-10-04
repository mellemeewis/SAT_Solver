###############################################################################
# TASK 1: SAT solver			                                              #
# Building a SAT solver with two different heuristics      			          #
# Group 23                                                                    #
# Melle Meewis en Jikke van den Ende                                          #
###############################################################################

import os, sys
import mxklabs.dimacs

directory = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(directory, "code"))

from classes.solver import Solver
from helpers.update_clause_list import update_clause_list
from helpers.write_output import write_output
from helpers.remove_tautologies import remove_tautologies

def main():
    ARGV_LEN = len(sys.argv)
    if ARGV_LEN != 3:
        if ARGV_LEN > 0:
            print("usage error: {} S<n> <file>".format(sys.argv[0]))
        else:
            print("usage error")
        sys.exit(1)

    else:
        strategies = ["Random", "DLCS", "DLIS", "JW_onesided", "MOM"]
        strategy = int(sys.argv[1][1])
        if strategy < 1 or strategy > 5:
            print("Strategy not supported, you can choose between the following strategies:")
            for i, strategy in enumerate(strategies):
                print((i + 1), strategy)
            sys.exit(1)
        strategy = strategies[strategy - 1]
        filename = sys.argv[2]
        filename_path = f"data/sudoku's_dimac/{filename}"

        try:
            dimacs = mxklabs.dimacs.read(filename_path)
            clause_list = dimacs.clauses
        except Exception as e:
            print(e)
            sys.exit(1)

        split_limit = input("What is the maximum number of splits you would like "
                            "to allow before the program quits itself?\n"
                            "Choose -1 if you don't want to set a limit.\n")
        try:
            split_limit = int(split_limit)
        except Exception as e:
            print("No valid split limit chosen:")
            print(e)
            sys.exit(1)

        print(f"SAT Solver strated with strategy '{strategy}' and max. number of splits {split_limit}")
        solution = davis_putnam(clause_list, strategy, split_limit)
        write_output(solution, strategy, filename, filename_path)

def davis_putnam(clause_list, strategy, split_limit):
    clause_list = remove_tautologies(clause_list)
    solver = Solver()
    solution = solver.dp(update_clause_list(clause_list, None), set(), strategy, split_limit)
    return solution

if __name__ == "__main__":
    main()
