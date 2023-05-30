import nashpy as nash

A = [[3, 0], [5, 1]]
B = [[3, 5], [0, 1]]

prisoner_dilemma = nash.Game(A, B)
equilibria = prisoner_dilemma.support_enumeration()
for eq in equilibria:
    print(eq)
