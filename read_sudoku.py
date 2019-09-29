import sys
import math


def main():
    ARGV_LEN = len(sys.argv)
    if ARGV_LEN == 2:
        filename = sys.argv[1]
        filename = "sudoku's_raw/" + filename
        read_sudoku(filename)
    else:
      if ARGV_LEN > 0:
        print("usage error: {} <file>".format(sys.argv[0]))
      else:
        print("usage error")


def read_sudoku(filename):
    with open(filename, "r") as f:
        data = f.readlines()
        sudoku_number = 0
        for sudoku in data:
            sudoku = sudoku.strip()
            sudoku_size = int(math.sqrt(len(sudoku)))
            dimac_list = []
            row = 1
            column = 1
            for character in sudoku:
                if character != ".":
                    clause = str(row) + str(column) + character
                    dimac_list.append(clause)
                column += 1
                if column > sudoku_size:
                    column %= sudoku_size
                    row += 1
            sudoku_number += 1
            write_sudoku_dimac(sudoku_number, sudoku_size, dimac_list)
    f.close()


def write_sudoku_dimac(sudoku_number, sudoku_size, dimac_list):
        filename_writing = f"sudoku's_dimac/sudoku{sudoku_size}x{sudoku_size}_{sudoku_number}"
        filename_reading = f"sudoku's_raw/sudoku_rules{sudoku_size}x{sudoku_size}.txt"
        with open(filename_reading, "r") as f:
            clauses_rules = f.readlines()
        with open(filename_writing, "w") as f:
            f.write(f"p cnf {sudoku_size}{sudoku_size}{sudoku_size} {len(clauses_rules) + len(dimac_list)}\n")
            for clause in dimac_list:
                f.write(f"{clause} 0\n")
            for clause in clauses_rules:
                f.write(clause)
        f.close()


if __name__ == "__main__":
    main()
