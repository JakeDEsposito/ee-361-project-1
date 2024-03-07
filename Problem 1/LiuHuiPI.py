from math import sqrt, pow, pi

# Creates an approximation of PI using the Liu Hui approximation method.
def pi_LiuHui(epsilon):
    assert epsilon > 0, "Epsilon must be greater than 0!"

    r = 1
    M = r
    sides = 3
    while True:
        m = sqrt(pow(M / 2, 2) + pow(r - sqrt(pow(r, 2) - pow(M, 2) / 4), 2))
        sides *= 2
        if m * sides - M * sides / 2 < epsilon:
            break
        M = m
    return m * sides


assert pi_LiuHui(0.0001) == 3.1415838921483186

prev = None
for x in [1, 0.1, 0.01, 0.001, 0.0001, 0.00001]:
    current = pi_LiuHui(x)
    assert current <= pi, "Result of PI approximation is more than PI!"

    if prev is None:
        prev = current
    else:
        assert current - prev > 0, f"Result of PI approximation with epsilon {str(x)} is larger than previous approximation!"
        prev = current
