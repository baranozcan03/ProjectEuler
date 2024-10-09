'''
Question Id: 1
Question Name: Multiples of 3 or 5
Question: Find the sum of all the multiples of 3 or 5 below 1000.
'''
# Suprisingly, no loops needed!
# Intuition, find the sum of series (3,6,9...999). They are the multiple of 3.
# find the sum of series (5,10,15,20...995). Add them. Remove the sum (15,30..990).

from timeit import default_timer as timer #i want to see how much time the solution takes.
start = timer()

sOneNumberOfTerms = (999-3)/3 +1
sOneSum = (sOneNumberOfTerms * (999 + 3)) / 2

sTwoNumberOfTerms = (995-5)/5 +1
sTwoSum = (sTwoNumberOfTerms * (995 + 5)) / 2

sThreeNumberOfTerms = (990-15)/15 +1
sThreeSum = (sThreeNumberOfTerms * (990 + 15)) / 2

sum = sOneSum + sTwoSum - sThreeSum


end = timer()

print(sum)
print(end-start)

#the answer is : 233168
#time it took : 0.0003621930000008433 seconds