'''
Question Id: 8
Question Name: Largest Product in a Series
Find the thirteen adjacent digits in the 1000-digit number that have the greatest product. What is the value of this product?
'''

a_str = """
73167176531330624919225119674426574742355349194934
96983520312774506326239578318016984801869478851843
85861560789112949495459501737958331952853208805511
12540698747158523863050715693290963295227443043557
66896648950445244523161731856403098711121722383113
62229893423380308135336276614282806444486645238749
30358907296290491560440772390713810515859307960866
70172427121883998797908792274921901699720888093776
65727333001053367881220235421809751254540594752243
52584907711670556013604839586446706324415722155397
53697817977846174064955149290862569321978468622482
83972241375657056057490261407972968652414535100474
82166370484403199890008895243450658541227588666881
16427171479924442928230863465674813919123162824586
17866458359124566529476545682848912883142607690042
24219022671055626321111109370544217506941658960408
07198403850962455444362981230987879927244284909188
84580156166097919133875499200524063689912560717606
05886116467109405077541002256983155200055935729725
71636269561882670428252483600823257530420752963450
"""
a = [int(num) for num in a_str if num != "\n"]

from timeit import default_timer as timer #i want to see how much time the solution takes.
start = timer()
result = 0

#dWe can use start from the first 13 nums multiply them, and slide 1 to the right and check?
#is that smart?
#there is a slight optimisation: assume current 13 is wirtten as 
# a1 * (a2*a3*..a13), if you slide to the right 1 step it becomes (a2*a3*..a13) * a14.
# so just divide by a1 and multiply by a14 insted of  remultiplying every time.

firstPro = 1
for i in range(0,13):
  firstPro *= a[i]
result = firstPro # keep the max
current = firstPro

digit= 0

while digit < len(a) - 13:
    if a[digit + 13] == 0 or a[digit] == 0:
        digit += 14
        if digit < len(a) - 13:
            current = 1
            for i in range(digit, digit + 13):
                current *= a[i]
        result = max(result, current)
    else:
        current = current // a[digit] * a[digit + 13]
        result = max(result, current)
        digit += 1



end = timer()

print(f"Largest product: {int(result)}")
print(f"Time taken: {end - start} seconds")

#the answer is :  23514624000
#time it took : 0.0011148869998578448 seconds