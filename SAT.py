import sys
from helpers.read_dimacs import read_dimacs

if __name__ == "__main__":
  ARGV_LEN = len(sys.argv)
  if ARGV_LEN == 2:
      filename = sys.argv[1]
      filename = f"sodoku's_dimac/{filename}"
      clause_list = read_dimacs(filename)[0]
      variable_list = read_dimacs(filename)[1]
      
  else:
    if ARGV_LEN > 0:
      print("usage error: {} <file>".format(sys.argv[0]))
    else:
      print("usage error")
