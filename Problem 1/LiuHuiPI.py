from math import sqrt, pow

# Incomplete
def pi_LiuHui(epsilon):
    '''
    This function utilizes Liu Hui's formula to create an accurate representation of PI based on the passed
    epsilon value
    :param epsilon: the control value for getting PI close to its true value
    :return: returns the estimation of pi
    '''
    assert epsilon > 0, "Epsilon must be greater than 0!"

    r = 1
    M = r
    sides = 3
    while M >= epsilon:
        m = sqrt(pow(M / 2, 2) + pow(r -sqrt(r - ((M**2) / 4)),2))
        M = m
        sides *= 2

    return m * sides
#########################################

# Main Driver
#########################################
if __name__ == '__main__':
    #assert pi_LiuHui(0.0001) == 3.1415838921483186

    print(pi_LiuHui(0.0001))