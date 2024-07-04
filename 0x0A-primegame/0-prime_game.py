#!/usr/bin/python3

def sieve_of_eratosthenes(max_num):
    """Generate a list of primes up to max_num using the Sieve of Eratosthenes."""
    is_prime = [True] * (max_num + 1)
    is_prime[0] = is_prime[1] = False  # 0 and 1 are not primes
    p = 2
    while (p * p <= max_num):
        if is_prime[p]:
            for i in range(p * p, max_num + 1, p):
                is_prime[i] = False
        p += 1
    primes = [p for p in range(max_num + 1) if is_prime[p]]
    return primes

def isWinner(x, nums):
    """Determine the winner of the game."""
    if not nums or x < 1:
        return None

    # Find the maximum value in nums to limit the sieve
    max_num = max(nums)
    primes = sieve_of_eratosthenes(max_num)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        primes_set = set(primes[:n + 1])
        current_player = "Maria"
        while primes_set:
            prime_to_remove = min(primes_set)
            primes_set -= set(range(prime_to_remove, n + 1, prime_to_remove))
            current_player = "Ben" if current_player == "Maria" else "Maria"
        
        if current_player == "Ben":
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
