from math import sqrt, pow

# Incomplete
def pi_LiuHui(epsilon):
    assert epsilon > 0, "Epsilon must be greater than 0!"

    r = 1
    M = r
    sides = 3
    while M >= epsilon:
        m = sqrt(pow(M / 2, 2) + pow(r - sqrt(pow(r, 2) - pow(M, 2) / 4), 2))
        M = m
        sides *= 2

    return m * sides

#assert pi_LiuHui(0.0001) == 3.1415838921483186

print(pi_LiuHui(0.0001))