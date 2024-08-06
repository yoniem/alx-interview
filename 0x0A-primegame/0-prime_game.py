#!/usr/bin/python3
"""
Prime Game
"""


def sieve(n):
    """
    Generate a list of prime numbers up to n using the Sieve of Eratosthenes
    """
    primes = [True] * (n + 1)
    p = 2
    while (p * p <= n):
        if (primes[p] == True):
            for i in range(p * p, n + 1, p):
                primes[i] = False
        p += 1
    prime_numbers = [p for p in range(2, n + 1) if primes[p]]
    return prime_numbers


def play_game(n):
    """
    Simulate one round of the game and return the winner
    0: Maria, 1: Ben
    """
    primes = sieve(n)
    available = [True] * (n + 1)
    player = 0  # Maria starts first
    
    while True:
        move_made = False
        for prime in primes:
            if prime <= n and available[prime]:
                move_made = True
                for multiple in range(prime, n + 1, prime):
                    available[multiple] = False
                break
        if not move_made:
            break
        player = 1 - player  # Switch players
    
    return player  # 0 for Maria, 1 for Ben


def isWinner(x, nums):
    """
    Determine the winner of the game after x rounds
    """
    maria_wins = 0
    ben_wins = 0
    
    for n in nums:
        winner = play_game(n)
        if winner == 0:
            ben_wins += 1
        else:
            maria_wins += 1
    
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
