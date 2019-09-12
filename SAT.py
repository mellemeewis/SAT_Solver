import sys
from helpers.read_dimacs import read_dimacs

if __name__ == "__main__":
  ARGV_LEN = len(sys.argv)
  if ARGV_LEN == 2:
      filename = sys.argv[1]
      filename = f"sodoku's_dimac/{filename}"
      read_dimacs(filename)
  else:
    if ARGV_LEN > 0:
      print("usage error: {} <file>".format(sys.argv[0]))
    else:
      print("usage error")

      # hoi
