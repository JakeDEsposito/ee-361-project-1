'''
	Author: Jake D'Esposito
	Date: 2/28/2024
	Last Modified: 3/7/2024

	"Liu Hui's PI algorithm"

	Statement of Purpose: The program utilizes Liu Hui's algorithm for
	calculating an estimate of PI through the area of an N-Gon polygon

	INPUT:
		1) The accuracy of the estimate value of PI

	OUTPUT:
		1) The estimate of PI relative to the accuracy value passed

	PROCESSING:
		1) Doubles the number of sides a hypothetical N-Gon polygon until
		    input accuracy is reached to calculate the area of the N-Gon polygon
		    with a radius of 1

	ASSUMPTIONS:
		1) The radius of the N-Gon polygon will be 1
'''
from math import sqrt, pow, pi

# Creates an approximation of PI using the Liu Hui approximation method.
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
    while True:
        m = sqrt(pow(M / 2, 2) + pow(r - sqrt(pow(r, 2) - pow(M, 2) / 4), 2))
        sides *= 2
        if m * sides - M * sides / 2 < epsilon:
            break
        M = m
    return m * sides
#########################################

# Main Driver
#########################################
if __name__ == '__main__':
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
