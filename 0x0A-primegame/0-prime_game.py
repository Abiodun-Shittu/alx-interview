#!/usr/bin/python3
"""
Prime game
"""


def is_prime(num):
    """0-prime_game.py"""
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def isWinner(x, nums):
    """Determines the winner of a prime game session with `x` rounds.
    """
    maria_wins = 0
    ben_wins = 0

    for i in range(x):
        current_round = nums[i]
        numbers = list(range(1, current_round + 1))
        is_maria_turn = True

        while any(is_prime(num) for num in numbers):
            if is_maria_turn:
                prime = min(num for num in numbers if is_prime(num))
                numbers = [num for num in numbers if num % prime != 0]
            else:
                prime = min(num for num in numbers if is_prime(num))
                numbers = [num for num in numbers if num % prime != 0]
            is_maria_turn = not is_maria_turn

        if not is_maria_turn:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
