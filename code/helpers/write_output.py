def write_output(solution, strategy, startfile, startfile_path):
    filename_output = f"results/{startfile},{strategy}.txt"
    values_pos = solution[0]
    if values_pos == None:
        values_pos = []
    values_all = solution[1]
    if values_all == None:
        values_all = []
    number_of_splits = solution[2]
    number_of_conflicts = solution[3]

    with open(filename_output, "w") as f:
        f.write(f"Startfile: {startfile_path}\n"
                f"Strategy: {strategy}\n\n")
        f.write(f"Number of splits: {number_of_splits}\n")
        f.write(f"Number of conflicts: {number_of_conflicts}\n\n")
        f.write(f"Positve truth values:\n")
        if values_pos == []:
            f.write("No solution found.")
        for value in values_pos:
            f.write(f"{value}\n")
    f.close()

    filename_dimacs = f"output/{startfile}.out"
    with open(filename_dimacs, "w") as f:
        f.write(f"p cnf {len(set(values_all))} {len(values_all)}\n")
        for value in values_all:
            f.write(f"{value} 0\n")
    f.close()
    print(f"Open {filename_output} to see results.")
    print(f"Open {filename_dimacs} to see output dimacs file.")
