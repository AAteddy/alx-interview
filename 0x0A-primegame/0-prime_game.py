#!/usr/bin/python3

def sieve_of_eratosthenes(limit):
    """Uses the Sieve of Eratosthenes to
      find all primes up to limit"""
    primes = [True] * (limit + 1)
    primes[0] = primes[1] = False  # 0 and 1 are not primes
    
    for start in range(2, int(limit**0.5) + 1):
        if primes[start]:
            for multiple in range(start*start, limit + 1, start):
                primes[multiple] = False
    
    return primes

def isWinner(x, nums):
    """Determines the winner of the prime game"""
    if not nums or x < 1:
        return None
    
    # Find the maximum number in nums to sieve
    #  primes up to that number
    max_num = max(nums)
    
    # Precompute all primes up to max_num
    #  using Sieve of Eratosthenes
    primes = sieve_of_eratosthenes(max_num)
    
    # Store the number of primes up to each number n
    prime_count = [0] * (max_num + 1)
    for i in range(1, max_num + 1):
        prime_count[i] = prime_count[i - 1] + (1 if primes[i] else 0)
    
    maria_wins = 0
    ben_wins = 0
    
    # Iterate through each round
    for n in nums:
        # Maria wins if the number of primes up to n is odd,
        #  Ben wins if it's even
        if prime_count[n] % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1
    
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None