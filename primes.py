"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""
import math


# Function to return the first 'number_of_primes' prime numbers
def primes(number_of_primes):
    list = []
    num = 0  

    while len(list) < number_of_primes:
        if is_prime(num):
            list.append(num)
        num += 1
    
    return list


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


print(primes(15))