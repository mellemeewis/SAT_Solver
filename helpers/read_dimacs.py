import mxklabs.dimacs
from classes.literal import Literal
from classes.clause import Clause
from classes.variable import Variable

def read_dimacs(filename):
    try:
        # Read the DIMACS file "simple.cnf".
        dimacs = mxklabs.dimacs.read(filename)
        # Print some stats.
        print("num_vars=%d, num_clauses=%d" % (dimacs.num_vars, dimacs.num_clauses))
        # Iterate over clauses.
        clause_list = []
        variable_list = []
        literal_values_list = []
        for clause in dimacs.clauses:
            new_clause = Clause()
            for literal in clause:
                new_literal = Literal(literal)
                new_clause.list.append(new_literal)
                if abs(literal) not in literal_values_list:
                     literal_values_list.append(abs(literal))
                     new_variable = Variable(abs(literal))
                     variable_list.append(new_variable)
            clause_list.append(new_clause)
        return_list = [clause_list, variable_list]
        return return_list

    except Exception as e:
      # Report error.
      print(e)
