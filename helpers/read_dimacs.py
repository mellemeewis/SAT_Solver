import mxklabs.dimacs

def read_dimacs(filename):
    try:
      # Read the DIMACS file "simple.cnf".
      dimacs = mxklabs.dimacs.read(filename)
      # Print some stats.
      print("num_vars=%d, num_clauses=%d" % (dimacs.num_vars, dimacs.num_clauses))
      # Iterate over clauses.
      for clause in dimacs.clauses:
        # Print them out.
        print(clause)

    except Exception as e:
      # Report error.
      print(e)
