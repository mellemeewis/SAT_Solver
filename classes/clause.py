class Clause:
    def __init__(self):
        self.list = []

    def __str__(self):
        s = ""
        for literal in self.list:
            s = s + str(literal.value) + " "
        return s

    def contains_varible(self, literal):
        if literal_value in self.list or abs(literal.value) in self.list:
            return True
        else:
            return False
