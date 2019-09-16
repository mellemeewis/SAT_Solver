import sys
from helpers.read_dimacs import read_dimacs

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
    set_literal_truth_values(clause_list, variable_list)
    for clause in clause_list:
        print(clause)



def check_for_unit_clauses(clause_list, variable_list):
    clauses_to_remove = []
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
            clauses_to_remove.append(clause)

    for clause in clauses_to_remove:
        clause_list.remove(clause)


def set_literal_truth_values(clause_list, variable_list):
    clauses_to_remove = []
    for variable in variable_list:
        if variable.truth_value == False:

            for clause in clause_list:
                literals_to_remove = []
                for literal in clause.list:
                    if abs(literal.value) == variable.literal:
                        if literal.value < 0:
                            clauses_to_remove.append(clause)
                        else:
                            literals_to_remove.append(literal)
                for literal in literals_to_remove:
                    clause.list.remove(literal)

        elif variable.truth_value == True:
            for clause in clause_list:
                literals_to_remove = []
                for literal in clause.list:
                    if abs(literal.value) == variable.literal:
                        if literal.value < 0:
                            literals_to_remove.append(literal)
                        else:
                            clauses_to_remove.append(clause)
                for literal in literals_to_remove:
                    clause.list.remove(literal)

    for clause in clauses_to_remove:
        clause_list.remove(clause)


if __name__ == "__main__":
    main()
