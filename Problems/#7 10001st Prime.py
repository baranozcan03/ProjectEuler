'''
Question Id: 7
Question Name: 10001st Prime
What is the 10001 st prime number?
'''


from timeit import default_timer as timer #i want to see how much time the solution takes.
start = timer()

# So, do we use the sieve of eratosthenes? Sure.
#got this from https://stackoverflow.com/questions/3939660/sieve-of-eratosthenes-finding-primes-python
def primes_sieve2(limit):
    a = [True] * limit                          # Initialize the primality list
    a[0] = a[1] = False

    for (i, isprime) in enumerate(a):
        if isprime:
            yield i
            for n in range(i*i, limit, i):     # Mark factors non-prime
                a[n] = False
#but this requires a limit which we frankly dont know... 
#or ? maybe we can estimate a limit
# it truns out that nth prime is aproximetly n*logn th natural number.

#we will get the ceiling of log just in case
limit = 10001 * 17

result = 0
counter = 0
primes = primes_sieve2(limit)
for i in primes:
  counter += 1
  if (counter ==10001):
    result = i

end = timer()

print(result)
print(end-start)

#the answer is :  104743
#time it took : 0.03903304799951002 seconds