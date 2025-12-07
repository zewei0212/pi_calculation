"""A way to estimate the value of the pi constant using NumPy."""

import argparse
import timeit

import numpy as np

from utils import format_time

def point_in_circle(x, y, radius=1):
    """
    Checks whether a point (x, y) is part of a circle with a set radius.

    example
    -------
    >>> point_in_circle(0, 0)
    True

    """
    return x**2 + y**2 <= radius**2

def calculate_pi_timeit(points):
    """
    Wrapper function to build calculate_pi with a particular number of points
    and returns the function to be timed.
    """
    def calculate_pi():
        """
        Calculates an approximated value of pi by the Monte Carlo method.
        """
        x = np.random.uniform(-1.0, 1.0, size=points)
        y = np.random.uniform(-1.0, 1.0, size=points)
        inside = x**2 + y**2 <= 1.0
        n_inside = np.count_nonzero(inside)
        pi_estimate = 4.0 * n_inside / points

        return pi_estimate
    return calculate_pi


def command():
    """
    entry point of the script to accept arguments
    """

    parser = argparse.ArgumentParser(description="Calculates an approximate value of PI and how long it takes using NumPy",
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('--npoints', '-np', default=10_000, type=int, help="Number of random points to use")
    parser.add_argument('--number', '-n', default=100, type=int, help="Number of times to execute the calculations")
    parser.add_argument('--repeat', '-r', default=5, type=int, help="How many times to repeat the timer")

    arguments = parser.parse_args()

    calc_pi = calculate_pi_timeit(arguments.npoints)
    print(f"pi = {calc_pi()} (with {arguments.npoints})")
    result = timeit.repeat(calc_pi, number=arguments.number, repeat=arguments.repeat)
    best = min(result) / arguments.number
    print(f"{arguments.number} loops, best of {arguments.repeat}: {format_time(best)} per loop")


if __name__ == '__main__':
    command()
