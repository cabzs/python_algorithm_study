# 개구리

def solution(stones):
    cnt = 0
    current = 0
    n = len(stones)
    while current < n:
        current += stones[current]

        cnt += 1
    return cnt

print(solution([2,5,1,3,2,1]))