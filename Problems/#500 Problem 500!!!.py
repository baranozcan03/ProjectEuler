'''
Question Id: 500
Question Name: Problem 500!!!

Find the smallest number with 2^500500 divisors.
Give your answer modulo 500500507.
'''

from timeit import default_timer as timer #i want to see how much time the solution takes.

result = 0
start = timer()

import heapq

#intution: any number by FTA can be written as a product of primes.
# We know that Tao(n) is mutiplicative. So the Tao of any number is
#the product of ++1 of powers of its prime factors. 
#We start n=1. Then build a heap. Is adding a new prime chepaer? Or 
# should we 'double + 1' one of the power of the primes that we already have.


#first i think it will come in handy to have the primes. Otherwise... Its is 
#kind of necessary since we want to build a cost heap.
def primes_sieve(limit):
    a = [True] * limit                          # Initialize the primality list
    a[0] = a[1] = False
    p = []
    for (i, isprime) in enumerate(a):
        if isprime:
            p.append(i)
            for n in range(i*i, limit, i):     # Mark factors non-prime
                a[n] = False
    return p
limit = 500500 * 19
primes = primes_sieve(limit)


#well i solved this metheatically but, using hep didnt come to my mind. 
# the idea of heap came from @hickford
def solve(k, modulus=None):
    """
    Calculate the smallest number that has exactly 2^k divisors.
    
    This function constructs the smallest integer that has exactly 2^k divisors by multiplying prime numbers 
    in an optimal manner. The problem is equivalent to minimizing the product of prime powers that would yield 
    2^k divisors.

    Parameters:
    k (int): The desired number of divisors in the form of 2^k. The goal is to find the smallest number 
             that has exactly 2^k divisors.
    modulus (int, optional): If provided, the final result will be calculated modulo this value to avoid overflow.

    Returns:
    n (int): The smallest number that has exactly 2^k divisors, optionally modulo `modulus`.
    """
    
    # Step 1: Initialize the result `n` to 1 because we will build the smallest number multiplicatively.
    n = 1
    
    # Step 2: Extract the first k primes, which will be the candidates for constructing the number.
    # The list `costs` is initialized with the first `k` prime numbers.
    costs = primes[:k]  # The variable `primes` is assumed to be a precomputed list of prime numbers.
    
    # Step 3: We use a heap (min-heap) to efficiently retrieve the smallest available prime (or prime power).
    # The heap is used to always get the smallest prime factor (or its power) to multiply into the number `n`.
    # `heapq` helps us efficiently manage this list of primes and prime powers in ascending order.
    
    # Step 4: Iterate exactly `k` times since we need to make 2^k divisors.
    for i in range(k):
        # Extract the smallest "cost" prime or prime power from the heap.
        # This is the prime (or prime power) that will be multiplied next into `n`.
        cost = heapq.heappop(costs)
        
        # Step 5: Once a prime `cost` is used, we push its square back into the heap.
        # Why? Because after using a prime, we can reuse its square (prime^2), which will increase the divisor count.
        heapq.heappush(costs, cost**2)
        
        # Step 6: Multiply the result `n` by the current `cost` (which is the smallest available prime or prime power).
        n *= cost
        
        # Step 7: If a modulus is provided, apply modular reduction to prevent overflow.
        # This ensures that the result does not grow too large, which would slow down computations or cause issues.
        if modulus:
            n %= modulus

    # Step 8: After `k` iterations, the number `n` will have exactly 2^k divisors, and it will be the smallest possible.
    # The function returns the result, either as is or modulo the provided modulus.
    return n

result = solve(500500, 500500507)


end = timer()

print(f"Result: {int(result)}")
print(f"Time taken: {end - start} seconds")

#the answer is : 35407281
#time it took : 3.229457573000218 seconds