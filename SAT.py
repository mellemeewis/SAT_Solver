import sys
from read_dimacs import read_dimacs
from dp import dp
from dp import test

def main():
     ARGV_LEN = len(sys.argv)
     if ARGV_LEN == 2:
         filename = sys.argv[1]
         filename = f"sodoku's_dimac/{filename}"
         clause_list = read_dimacs(filename)
         solution = dp(test(clause_list, None), set())
         print("Solution = ", solution)

     else:
       if ARGV_LEN > 0:
         print("usage error: {} <file>".format(sys.argv[0]))
       else:
         print("usage error")

if __name__ == "__main__":
    main()
