'''
Question Id: 9
Question Name: Special Pythagorean Triplet
There exists exactly one Pythagorean triplet for which a+b+c=1000. Find a*b*c
'''

from timeit import default_timer as timer #i want to see how much time the solution takes.
start = timer()
result = 0

#temptation is to go for 3 nested loops and try every a,b,c combination. since we have 1000
#posibilities for each we would have 1000000000 iterations.
# but we can optimise -> we can use 2 loops for a and c. since b = 1000-a-c. 
# 1000000 iterations.
# we are not done yet. we know c > b > a : a can at most be 332, because 
#332+333+334 = 999. otherwise we breach the limit   
# 331668 iterations
# we are not done yet. we also know that c cant be smaller than 335 since:
# 332 +333 + 334 = 999
# 220780 iterations
# now we know that the resulting triplet represents a triangle, so we can limit
# the ranges with that as well. since this is a triangle with right angle.
# the lest c can be is when a,b is maximum, allow them to be the same for this
# a = b = c / sqrt(2). c = 1000 * sqrt(2)* (2 + sqrt(2))-> apprxmt 412.
# also c < a+b a simple triangle constraint. then c < 1000-c.... c <500.
# so ------> 335 =< c < 500
# 54780 iterations
####.... we are not done yet.since c is in the outer loop. calculate it once.
# we are still not done.
#range(max(1, 1000 - c - (c - 1)), min(332, (1000 - c) // 2) + 1)  is the optimal range for a. 
# b cant be equal to c -> so b is at most c -1 so a is at least-> 1000 - c - c +1. 
# 1000-c at most can be evenly distirubted between a and b with b is being +1 more.
# so a at max --> 1000 -c //2, since its a range we add+1 because that is not included. 
# 20666 iterations

for c in range(335,500):
  cSqr = c**2
  for a in range(max(1, 1000 - c - (c - 1)), min(332, (1000 - c) // 2) + 1):
    b = 1000 - a - c
    if a**2 + b**2 == cSqr:
      result = a*b*c




end = timer()

print(f"Result: {int(result)}")
print(f"Time taken: {end - start} seconds")

#the answer is : 31875000 
#time it took : 0.017758416999868132 seconds