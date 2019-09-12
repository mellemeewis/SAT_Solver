import sys
import math

def main():
    ARGV_LEN = len(sys.argv)
    if ARGV_LEN == 2:
        filename = sys.argv[1]
        filename = "sodoku's_raw/" + filename
        read_sodoku(filename)
    else:
      if ARGV_LEN > 0:
        print("usage error: {} <file>".format(sys.argv[0]))
      else:
        print("usage error")


def read_sodoku(filename):
    with open(filename, "r") as f:
        data = f.readlines()
        sodoku_number = 0
        for sodoku in data:
            sodoku = sodoku.strip()
            sodoku_size = int(math.sqrt(len(sodoku)))
            dimac_list = []
            row = 1
            column = 1
            for charachter in sodoku:
                if charachter != ".":
                    clause = str(row) + str(column) + charachter
                    dimac_list.append(clause)
                column += 1
                if column > sodoku_size:
                    column %= sodoku_size
                    row += 1
            sodoku_number += 1
            write_sodoku_dimac(sodoku_number, sodoku_size, dimac_list)
    f.close()

def write_sodoku_dimac(sodoku_number, sodoku_size, dimac_list):
        filename_writing = f"sodoku's_dimac/sodoku{sodoku_size}x{sodoku_size}_{sodoku_number}"
        filename_reading = f"sodoku's_raw/sodoku_rules{sodoku_size}x{sodoku_size}.txt"
        with open(filename_reading, "r") as f:
            clauses_rules = f.readlines()
        with open(filename_writing, "w") as f:
            f.write(f"p cnf {sodoku_size}{sodoku_size}{sodoku_size} {len(clauses_rules) + len(dimac_list)}\n")
            for clause in dimac_list:
                f.write(f"{clause} 0\n")
            for clause in clauses_rules:
                f.write(clause)
        f.close()





if __name__ == "__main__":
    main()
