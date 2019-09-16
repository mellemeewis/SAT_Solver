import sys
from helpers.read_dimacs import read_dimacs

if __name__ == "__main__":
  main()

#   hoiiii

def main():
     ARGV_LEN = len(sys.argv)
     if ARGV_LEN == 2:
         filename = sys.argv[1]
         filename = f"sodoku's_dimac/{filename}"
         input = read_dimacs(filename)
         clause_list = input[0]
         variable_list = input[1]
         sat_solver(clause_list, variable_list)

     else:
       if ARGV_LEN > 0:
         print("usage error: {} <file>".format(sys.argv[0]))
       else:
         print("usage error")

def sat_solver(clause_list, variable_list):
    check_for_unit_clauses(clause_list, variable_list)



def check_for_unit_clauses(clause_list, variable_list):
    for clause in clause_list:
        if len(clause.list) == 1:
            literal = clause.list[0].value
            if literal < 0:
                for variable in variable_list:
                    if abs(literal) == variable.literal:
                        variable.truth_value = False
            else:
                for variable in variable_list:
                    if literal == variable.literal:
                        variable.truth_value = True
            clause_list.remove(clause)
