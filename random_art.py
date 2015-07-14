import random
from math import sin,cos,pi, sqrt
import statistics

# Your job is to create better version of create_expression and
# run_expression to create random art.
# Your expression should have a __str__() function defined for it.


def create_expression():
    """This function takes no arguments and returns an expression that
    generates a number between -1.0 and 1.0, given x and y coordinates."""
    # expr = lambda x, y: (random.random() - 2 * 81) - 1
    # expr_dict= {'A': lambda x, y: sin(sin(sin(cos(x * y)))),
    #             'B': lambda x, y: sin(pi) * 2,
    #             'C': lambda x, y: sin(3 * pi(sin(21))),
    #             'D': lambda x, y: (cos(sin((pi * 8)))),
    #             'E': lambda x, y: cos(cos(sin(7)))
    #             }
    # expr_dict = {'sure': lambda x, y: sin(sin(sin(cos(pi)))),
    #              'the': lambda x, y: random.triangular(0.2, 0.9),
    #              'dang': lambda x, y: sin(pi(sin(pi(sin(cos(-1)))))),
    #              'should': lambda x, y: cos(x * cos(sin(pi))),
    #              'make': lambda x, y: random.uniform(1278, 900000),
    #              'art': lambda x, y: random.gauss(x, y)}

    expr_list = [lambda x, y: (random.random() * 21) - 1 / 3,
                 lambda x, y: (random.triangular(0, 1) * 2) - 1,
                 lambda x, y: (random.uniform(x, y) * 2) - 1,
                 lambda x, y: ((x**3) - sin(3)),
                 lambda x, y: (random.triangular(0.2, 0.8) / 2) - 1,
                 lambda x, y: sin(pi * 2) - 3 / 4,
                 lambda x, y: sqrt(sin(pi / 2) * cos(x)),
                 lambda x, y: sin(cos(sin(cos(sin(cos(sin(cos(pi)))))))),
                 lambda x, y: 7 + sin(pi) / sqrt(2**4),
                 lambda x, y: sqrt(3) * sin(sin(sin(pi) - 1)),
                 lambda x, y: (random.random() * 8) + sqrt(66) / 2,
                 lambda x, y: sin(sin(sin(sin(sin(sin(sin(sin(sin(7 * x - y))))))))),
                 lambda x, y: random.uniform(sin(1), pi) **8 / 2]



    return random.choice(expr_list)


def run_expression(expr, x, y):
    """This function takes an expression created by create_expression and
    an x and y value. It runs the expression, passing the x and y values
    to it and returns a value between -1.0 and 1.0."""
    return expr(x, y)
