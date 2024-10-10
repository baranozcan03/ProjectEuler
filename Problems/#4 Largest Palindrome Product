'''
Question Id: 4
Question Name: Palindrome Product
Find the largest palindrome made from the product of two 3-digit numbers.
'''


from timeit import default_timer as timer #i want to see how much time the solution takes.
start = timer()


#should we go through all 3 digit numbers? Not really. 
#lets ask a question. IF you can find a palindrom at high 3 digit factors...
#wht try the lover ones

result = 0 

#start big and get small, why start big? we will see
for i in range(1000,100,-1):
  if (result > i*999):#biggest possible num is smaller than our max. No need to check
      break
  for j in range(1000,100,-1):
    num = i*j
    if (num <= result): #if the current number is smaller than our max, exist
    #as numbers will only get smaller, and this optimisaiton is why we start big
      break
    numStr = str(num)
    if numStr[0] == numStr[-1] and numStr == numStr[::-1]:  
            result = num

end = timer()

print(result)
print(end-start)

#the answer is :  906609
#time it took : 0.007296916999962377 seconds