##### https://www.codewars.com/kata/514b92a657cdc65150000006/train/python

"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, 
we get 3, 5, 6 and 9. The sum of these multiples is 23.
Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in. 
Additionally, if the number is negative, return 0 (for languages that do have them).

Note: If the number is a multiple of both 3 and 5, only count it once.
Courtesy of projecteuler.net (Problem 1)
"""

def solution(number):
    if number <= 0 :
        return 0
    else : 
        import math
        L = list(range(1,number+1))
        multiples_of_3 = []
        multiples_of_5 = []
        other = []
        for i in range(0,number-1):
            if L[i]%3 == 0:
                multiples_of_3.append(L[i])
            elif L[i]%5 == 0:
                multiples_of_5.append(L[i])
            else : other.append(L[i])
    return round(math.fsum(multiples_of_3) + math.fsum(multiples_of_5))
        
print(solution(200))    # 9168

# "Should return 3 for n=4"
# "Should return 8 for n=6"
# "Should return 60 for n=16"
# "Should return 0 for n=3"
# "Should return 3 for n=5"
# "Should return 45 for n=15"
# "Should return 0 for n=0"
# "Should return 0 for n=-1"
# "Should return 23 for n=10"
# "Should return 78 for n=20"
# "Should return 9168 for n=200"

