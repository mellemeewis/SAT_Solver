import random

def random_split(clause_list):
    random_clause = clause_list[random.randint(0, (len(clause_list) - 1))]
    random_literal = random_clause[random.randint(0, len(random_clause) - 1)]
    return random_literal
