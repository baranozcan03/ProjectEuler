'''
Question Id: 6
Question Name: Sum Square Difference
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
'''


from timeit import default_timer as timer #i want to see how much time the solution takes.
start = timer()

# Brute force method using 2 loops is obvious. But can we think smarter? Yes
# First optimisation we can use Gauss Sum to find 1+2+3..100 rather than using a loop.
# Second optimisation we know that the sum of squares of natural numbers form 1 to n
# is n(n+1)(2n+1)/6

SumOfSq = 100*(101)*(201)/6
SqOfSum = (50 * 101)**2

result = SqOfSum - SumOfSq

end = timer()

print(result)
print(end-start)

#the answer is :  25164150
#time it took : 0.0001432909998584364 seconds