class Clause:
    def __init__(self):
        self.list = []
        
    def __str__(self):
        s = ""
        for literal in self.list:
            s = s + str(literal.value) + " "
        return s
