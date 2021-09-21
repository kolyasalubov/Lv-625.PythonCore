def solution(number):
    counter = 0
    for num in range(number):
        if num%3 == 0 or num%5 == 0:
            counter += num
    return counter