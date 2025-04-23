from collections import defaultdict

productions = defaultdict(list)
first = defaultdict(set)

def is_terminal(symbol):
    return not symbol.isupper() and symbol != 'ε'

def compute_first(X):
    if is_terminal(X):
        return {X}
    if first[X]:
        return first[X]
    for prod in productions[X]:
        for sym in prod:
            sym_first = compute_first(sym)
            first[X] |= sym_first - {'ε'}
            if 'ε' not in sym_first:
                break
        else:
            first[X].add('ε')
    return first[X]

n = int(input("No. of productions: "))
for _ in range(n):
    line = input().replace("->", " ").split()
    lhs = line[0]
    rhs_parts = " ".join(line[1:]).split('|')
    for part in rhs_parts:
        productions[lhs].append(part.strip().split())

non_terminals = list(productions.keys())
