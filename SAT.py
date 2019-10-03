import sys
import mxklabs.dimacs
import datetime

from read_dimacs import read_dimacs
from dp import Solver
from dp import update_clause_list
from transform_clauses import transform_clauses


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
        filename_path = f"sudoku's_dimac/{filename}"


        try:
            dimacs = mxklabs.dimacs.read(filename_path)
            clause_list = dimacs.clauses
        except Exception as e:
            print(e)
            sys.exit(1)
        print("SAT Solver strated with strategy:", strategy)
        solution = davis_putnam(clause_list, strategy)
        write_output(solution, strategy, filename, filename_path)


def write_output(solution, strategy, startfile, startfile_path):
    filename_output = f"results/{startfile},{strategy}.txt"
    values_pos = solution[0]
    if values_pos == None:
        values_pos = []
    values_all = solution[1]
    if values_all == None:
        values_all = []
    number_of_splits = solution[2]
    number_of_conflicts = solution[3]

    with open(filename_output, "w") as f:
        f.write(f"Startfile: {startfile_path}\n"
                f"Strategy: {strategy}\n\n")
        f.write(f"Number of splits: {number_of_splits}\n")
        f.write(f"Number of conflicts: {number_of_conflicts}\n\n")
        f.write(f"Positve truth values:\n")
        if values_pos == []:
            f.write("No solution found.")
        for value in values_pos:
            f.write(f"{value}\n")
    f.close()

    filename_dimacs = f"output/{startfile}.out"
    with open(filename_dimacs, "w") as f:
        f.write(f"p cnf {len(set(values_all))} {len(values_all)}\n")
        for value in values_all:
            f.write(f"{value} 0\n")
    f.close()
    print(f"Open {filename_output} to see results.")
    print(f"Open {filename_dimacs} to see output dimacs file.")

def davis_putnam(clause_list, strategy):
    clause_list = remove_tautologies(clause_list)
    solver = Solver()
    solution = solver.dp(update_clause_list(clause_list, None), set(), strategy)
    print("Solution = ", solution)
    return solution

def remove_tautologies(clause_list):
    clause_list = [clause for clause in clause_list if not is_tautology(clause)]
    return clause_list

def is_tautology(clause):
    for literal in clause:
        if -literal in clause:
            return True
    return False


if __name__ == "__main__":
    main()
