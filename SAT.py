import sys
from read_dimacs import read_dimacs
from dp import dp
from dp import update_clause_list
from transform_clauses import transform_clauses


def main():
    ARGV_LEN = len(sys.argv)
    if ARGV_LEN == 2:
        filename = sys.argv[1]
        filename = f"sudoku's_dimac/{filename}"
        clause_list = read_dimacs(filename)
        # clause_list = transform_clauses(clause_list)
        solution = dp(update_clause_list(clause_list, None), set())
        print("Solution = ", solution)
    else:
        if ARGV_LEN > 0:
            print("usage error: {} S<n> <file>".format(sys.argv[0]))
        else:
            print("usage error")


if __name__ == "__main__":
    main()