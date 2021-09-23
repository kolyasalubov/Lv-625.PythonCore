def solution(number):
    return sum([a for a in range(number) if a % 3 == 0 or a % 5 == 0])

print(solution(20))
