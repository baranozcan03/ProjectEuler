'''
Question Id: 2
Question Name: Even Fibonacci Numbers
By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
'''


from timeit import default_timer as timer #i want to see how much time the solution takes.
start = timer()
result = 0

# Observe the following pattern, O representing odd, E representing even numbers.
# F -> O,O,E,O,O,E,O,O,E,O,O,E.... so if f(n) is Even, the next even is f(n+3).
# an easy calculation shows that for the kth even Fibonacci number
# k+1th even Fibonacci number can be calculated as -> f(k+1) = 4f(k) + f(k-1)  

result = 10
f1=2
f2=8
while(f2 < 4e6):
  temp = f1
  f1 = f2
  f2 = 4*f2 + temp
  result = result + f2
result -= f2

end = timer()

print(result)
print(end-start)

#the answer is : 4613732
#time it took : 0.00034799000013663317 seconds