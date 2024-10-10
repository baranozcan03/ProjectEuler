'''
Question Id: 3
Question Name: Largest Prime Factor
What is the largest prime factor of the number 600851475143?
'''


from timeit import default_timer as timer #i want to see how much time the solution takes.
start = timer()
result = 0

#should we try all prime numbers below the sqrt of this number? Not really
#Start small, when you find a prime. Divide the big number so we get a smaller problem size in our hands
#divide. Bookkeep. Continue...

num = 600851475143

##Stolen from SymPy 1.13.3 number theory module
def isPrime(n) -> bool:
    # The point here is just to speedily handle small numbers and many
    # composites. The bigger primes wont be relevent
    if n in [2, 3, 5]:
        return True
    if n < 2 or (n % 2) == 0 or (n % 3) == 0 or (n % 5) == 0:
        return False
    if n < 49:
        return True
    if (n %  7) == 0 or (n % 11) == 0 or (n % 13) == 0 or (n % 17) == 0 or \
       (n % 19) == 0 or (n % 23) == 0 or (n % 29) == 0 or (n % 31) == 0 or \
       (n % 37) == 0 or (n % 41) == 0 or (n % 43) == 0 or (n % 47) == 0:
        return False
    if n < 2809:
        return True
    if n < 65077:
        # There are only five Euler pseudoprimes with a least prime factor greater than 47
        return pow(2, n >> 1, n) in [1, n - 1] and n not in [8321, 31621, 42799, 49141, 49981]

result = 0
factor =2
while(factor*factor < num):
  if((num%factor==0) and bool(isPrime(factor))):
    num = num / factor
    if(result < factor):
      result = factor
  factor += 1
  

if(result < num and isPrime(int(num))):
  result = num

end = timer()

print(result)
print(end-start)

#the answer is : 6857 
#time it took : 0.0016010659992389265 seconds