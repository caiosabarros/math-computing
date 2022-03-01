from polynomial import Polynomial
from polynomial import ZERO
import math

#first: points, 0
#first: points, 1
def single_term(points, i):
    """Return one term of an interpolated polynomial.

    This method computes one term of the sum from the proof of Theorem 2.2.
    In particular, it computes:

      y_i \product_{j=0}^n (x - x_i) / (x_i - x_j)

    The encapsulating `interpolate` function sums these terms to construct
    the final interpolated polynomial.

    Arguments:
      - points: a list of (float, float)
      - i: an integer indexing a specific point

    Returns:
      A Polynomial instance containing the desired product.
    """
    the_term = Polynomial([1.])
    # For point 0, define 1,1
    # For point 1, define 2,2
    xi, yi = points[i]

    for j, p in enumerate(points):
        #for j == 0, skip
        if j == i:
            continue
        #for j == 1 and mor e, do it:
        #for j == 1, xj == 2
        xj = p[0]

        """
        The inlined Polynomial instance below is how we represent

          (x - x_j) / (x_i - x_j)

        using our Polynomial data type (where t replaces x as the variable, and
        x_i, x_j are two x-values of data points):

          (x - x_j) / (x_i - x_j) = (-x_j / (x_i - x_j)) * t^0
                                  +    (1 / (x_i - x_j)) * t^1
        """
        #x-xj xi -xj
        the_term = the_term * Polynomial([-xj / (xi - xj), 1.0 / (xi - xj)])

    # Polynomial([yi]) is a constant polynomial, i.e., we're scaling the_term
    # by a constant.
    return the_term * Polynomial([yi])


def interpolate(points):
    """Return the unique polynomial of degree at most n passing through the given n+1 points."""
    if len(points) == 0:
        raise ValueError('Must provide at least one point.')

    x_values = [p[0] for p in points]
    if len(set(x_values)) < len(x_values):
        raise ValueError('Not all x values are distinct.')

    terms = [single_term(points, i) for i in range(0, len(points))]
    return sum(terms, ZERO)



#Polynomial([2,3])
# 2 + 3x
print(math.sqrt(2)+math.sqrt(3))
# It looks like the function does not work if we give only the solutions
points = [(2,0), (1,0), (3,0)] 
print(interpolate(points))
#-23.0 + 38.666666666666664 x^1 + -17.0 x^2 + 2.3333333333333335 x^3

# Funcitonality:
# Builds the polynomial, given the coeficients.
# Builds the polynomial, given the roots
# The inverse is not true: If I give the polynomial, It wont give the me roots (Think of roots in complex number set)

# Understanding:
# The function interpolate calls the funciton single_term len(points) times. Each time, a point is the main one.

# The function single_term gives the productory (x-xj)/(xi-xj) = (x-x2)(x-x3)/(x1-x2)(x1-x3)...for the first point.
# To do it, (xi == x1, for example) it gets the point (xi,yi), goes through all the xj when j != 1, and makes the product (x-xj)/(x1-xj) for all j's
# It multiples that by y1 
# It adds this multiplication to an array
# Everything is done with all the points
# The terms are summed up 

#Exercise: implement sum and productory of polynomial

