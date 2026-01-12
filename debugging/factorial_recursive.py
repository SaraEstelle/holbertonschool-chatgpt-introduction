#!/usr/bin/python3
import sys

def factorial(n):
    """
    Function Description:
        Recursively calculates the factorial of a non-negative integer n.
        The factorial of n (denoted as n!) is the product of all positive integers
        less than or equal to n. By definition, factorial(0) is 1.

    Parameters:
        n (int): A non-negative integer whose factorial is to be computed.

    Returns:
        int: The factorial of the given number n.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Get the number from the command line arguments and calculate its factorial
f = factorial(int(sys.argv[1]))
print(f)
