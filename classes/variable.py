class Variable:
    def __init__(self, literal):
        self.literal = literal
        self.truth_value = None

    def __str__(self):
        s = str(self.literal) + " " + str(self.truth_value)
        return s
