from collections import defaultdict

productions = defaultdict(list)
first = defaultdict(set)
follow = defaultdict(set)

def is_terminal(sym):
    return not sym.isupper() and sym != 'ε'

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

def compute_follow(start_symbol):
    follow[start_symbol].add('$')
    
    while True:
        updated = False
        for lhs, prods in productions.items():
            for prod in prods:
                for i in range(len(prod)):
                    B = prod[i]
                    if B.isupper():
                        rest = prod[i+1:]
                        temp = set()
                        for sym in rest:
                            temp |= compute_first(sym) - {'ε'}
                            if 'ε' not in compute_first(sym):
                                break
                        else:
                            temp |= follow[lhs]
                        if not temp.issubset(follow[B]):
                            follow[B] |= temp
                            updated = True
        if not updated:
            break

# Input
n = int(input("No. of productions: "))
start_symbol = ""
for _ in range(n):
   line = input().replace("->", " ")
