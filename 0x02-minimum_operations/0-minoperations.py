#!/usr/bin/python3
"""
Module for Minimum Operations problem.
"""


def minOperations(n):
    """
    Calculates the fewest number of operations needed to result in exactly n H characters in the file.

    Args:
        n (int): The target number of characters.

    Returns:
        int: The minimum number of operations required.
             Returns 0 if n is impossible to achieve.
    """
    if n <= 1:
        return 0
    operations = 0
    divisor = 2
    while n > 1:
        if n % divisor == 0:
            operations += divisor
            n //= divisor
        else:
            divisor += 1
    return operations


if __name__ == "__main__":
    n_values = [4, 12, 21, 19170307, 972, 1, 0, -12, 2147483640]
    for n in n_values:
        print(f"Min # of operations to reach {n} char: {minOperations(n)}")
