import mxklabs.dimacs


def read_dimacs(filename):
    try:
        # Read the DIMACS file
        dimacs = mxklabs.dimacs.read(filename)
        # Iterate over clauses.

        return dimacs.clauses

    except Exception as e:
      # Report error.
      print(e)
