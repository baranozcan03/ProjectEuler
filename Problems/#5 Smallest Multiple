'''
Question Id: 5
Question Name: Smallest Multiple
What is the smallest positive number that is evenly divisible (convergent to 0)
by all of the numbers from 1 to 20.
'''


from timeit import default_timer as timer #i want to see how much time the solution takes.
start = timer()

# multiplying 1 * 2 * 3 * 4 ... * 20 wont work. For example onece you multiply by 16,
# it is now divisible to 1,2,4,8. But this try gives us an idea.
# start from 20, gather prime numbers. The max number of power you will need,
# will come form the numbers that are powers of the primes. 
# ie: nothing will need more 2 than 16.

#Intution. we will collect primes. then multiply these primes. The reason we collect
# primes is to make sure that we divide these numbers, at the same time we want,
# to collect least amount of it.


result = 1

# 1 is redundent.
# 2 , 4, 8 ,16 -> 2^4
# 3 , 9, -> 3^2
# go on this fashion 

# in order they are powers for 2: 2,3,5,7,11,13,17,19 
primes = [[2,4],[3,2],[5,1],[7,1],[11,1],[13,1],[17,1],[19,1]]

for i in primes:
  result = result * pow(i[0],i[1])

end = timer()

print(result)
print(end-start)

#the answer is :  232792560
#time it took : 0.00021323099986148009 seconds