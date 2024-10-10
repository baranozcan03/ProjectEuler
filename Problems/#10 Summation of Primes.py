'''
Question Id: 10
Question Name: Summation of Primes
Find the sum of all the primes below two million.
'''

from timeit import default_timer as timer #i want to see how much time the solution takes.
start = timer()
result = 0

#sieve ? 
# maybe we got sth faster?

def primes_sieve2(limit):
    a = [True] * limit                          
    a[0] = a[1] = False
    for (i, isprime) in enumerate(a):
        if isprime:
            yield i
            for n in range(i*i, limit, i):     
                a[n] = False

pList = primes_sieve2(2000000)
for i in pList:
  result += i


end = timer()

print(f"Result: {int(result)}")
print(f"Time taken: {end - start} seconds")

#the answer is : 142913828922 
#time it took : 0.8905479449999802 seconds