class Literal:
    def __init__(self, value):
        self.value = value
        if self.value < 0:
            self.direction = 0
        else:
            self.direction = 1

    def __str__(self):
        return str(self.value)
