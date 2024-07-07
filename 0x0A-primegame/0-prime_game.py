#!/usr/bin/python3
"""
0. Prime Game
Module for determining the winner of a prime game.
"""

def sieve_of_eratosthenes(n):
    """
    Generate a list of prime numbers up to n using the Sieve of Eratosthenes.

    Args:
    n (int): Maximum number up to which primes should be generated.

    Returns:
    list: List of prime numbers up to n.
    """
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False  # 0 and 1 are not primes
    p = 2
    while (p * p <= n):
        if is_prime[p]:
            for i in range(p * p, n + 1, p):
                is_prime[i] = False
        p += 1
    primes = [p for p in range(n + 1) if is_prime[p]]
    return primes

def isWinner(x, nums):
    """
    Determine the winner of multiple rounds of the prime game.

    Args:
    x (int): Number of rounds of the game.
    nums (list): List of integers representing different rounds.

    Returns:
    str or None: Name of the player with the most wins ('Maria' or 'Ben'), or None if no winner can be determined.
    """
    if not nums or x < 1:
        return None

    max_num = max(nums)
    primes = sieve_of_eratosthenes(max_num)
    prime_set = set(primes)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        remaining = list(range(1, n + 1))
        current_player = "Maria"

        while True:
            move_made = False
            for prime in primes:
                if prime in remaining:
                    remaining = [num for num in remaining if num % prime != 0]
                    move_made = True
                    break

            if not move_made:
                if current_player == "Maria":
                    ben_wins += 1
                else:
                    maria_wins += 1
                break

            current_player = "Ben" if current_player == "Maria" else "Maria"

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
