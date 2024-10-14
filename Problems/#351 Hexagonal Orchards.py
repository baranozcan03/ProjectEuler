'''
Question Id: 351
Question Name: Hexagonal Orchards

Let H(n) be the number of points hidden from the center in a hexagonal orchard of order n.
Find H(1000000)
'''

from timeit import default_timer as timer #i want to see how much time the solution takes.

result = 0
start = timer()

n = 1000000

#the hexagonal is symettrical in 1/6 ratio, so if i find the result in one of 
#the triangles i can multiply it by 6.
#we notice that once you index the dots. as n = the layer number, i = the index
#at that layer; (1,1) / (1,2)  (2,2) .... If gcd(i,n) = 1 we will call that dot a prime dot 
#notice that once a dot can be factorised (ie. (4,6)) it will be blocked by its primeDot -> (2,3)  
#therefore within a layer we look for the number of dots(i,n), where gcd(i,n) =1
#if we subtract the number of blocked dots from the n, we get the visible dots.

#Now, we know that within a layer n, all the dots will have the same n. and 0< i < n+1
#Thre fore we actually look for the amount of coprimes of n that are positive and smaller
#than n. Which is phi(n).

# now all we need (6 * [n*(n+1)/2 - Sigma(n=0 to 1000000)phi(n)]) 

#I used GTP 4-0 to document the function below....
#aint regretting
def compute_totients(N):
    """
    Compute the Euler's Totient (φ) values for all integers from 1 to N using a modified Sieve of Eratosthenes.
    
    Euler's Totient function φ(n) is the number of integers from 1 to n that are coprime with n.
    This function uses an efficient sieve-based approach to calculate the Totient values for all numbers 
    from 1 to N in O(N log log N) time complexity.

    Parameters:
    N (int): The upper bound up to which Totient values are calculated (inclusive).

    Returns:
    phi (list): A list where phi[i] gives the Totient value for the integer i (i.e., φ(i)).
    """

    # Step 1: Initialize required arrays
    # 'v' array is used to mark whether a number has been processed as a multiple of primes
    # 'phi' array will store the Totient values for each number from 1 to N
    v = [0] * (N + 1)      # v[i] will store the smallest prime divisor of i (0 means unvisited)
    phi = [0] * (N + 1)    # phi[i] will store the Euler's Totient value for i
    pr = []                # pr will store the list of primes we encounter during the sieve

    # Step 2: Initialize the Totient value for 1 manually
    # φ(1) is 1 because the only integer coprime with 1 is 1 itself
    phi[1] = 1

    # 'm' will be the number of primes found (used for iterating over primes)
    m = 0

    # Step 3: Sieve to calculate the Totient values for numbers from 2 to N
    for i in range(2, N + 1):
        if v[i] == 0:  # If v[i] is 0, then i is a prime (unmarked, i.e., not a multiple of any smaller prime)
            # Mark the number i as visited (i.e., its smallest prime divisor is itself, since it's prime)
            v[i] = i
            # The Totient function for a prime p is φ(p) = p - 1, since all numbers less than p are coprime with p
            phi[i] = i - 1
            # Add the prime i to the list of primes 'pr'
            pr.append(i)
            # Increment the prime counter 'm'
            m += 1

        # Step 4: For each prime pr[j] found so far, update the Totient values for its multiples
        # Iterate over the primes and update the values for multiples of i
        for j in range(m):
            # Check if the current prime pr[j] is larger than the smallest prime divisor of i (v[i])
            # or if the multiple exceeds the limit N
            if pr[j] > v[i] or pr[j] * i > N:
                break  # Stop if the current prime exceeds the constraints

            # Mark v[i * pr[j]] with the smallest prime divisor (i.e., pr[j])
            v[i * pr[j]] = pr[j]

            # Step 5: Update the Totient value for the number i * pr[j]
            # Case 1: If i is divisible by pr[j], we are dealing with powers of the prime pr[j]
            if v[i] == pr[j]:
                # When i is divisible by pr[j], the Totient value is updated as φ(i * pr[j]) = φ(i) * pr[j]
                phi[i * pr[j]] = phi[i] * pr[j]
            else:
                # Case 2: If i is not divisible by pr[j], then we apply the Totient multiplication property:
                # φ(i * pr[j]) = φ(i) * (pr[j] - 1)
                phi[i * pr[j]] = phi[i] * (pr[j] - 1)

    # Return the final list of Totient values from 1 to N
    return phi

#The time complexity is 𝑂(𝑁log⁡log⁡𝑁)

N = int(1e8)
# Compute phi values
phi = compute_totients(N)

sum_phi = sum(phi[1:N+1])
total_sum = N * (N + 1) // 2
result = (total_sum - sum_phi) * 6

end = timer()

print(f"Result: {int(result)}")
print(f"Time taken: {end - start} seconds")

#the answer is : 11762187201804552
#time it took : 131.79274886400003 seconds