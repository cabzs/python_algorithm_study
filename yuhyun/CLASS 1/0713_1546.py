N = int(input())

score = list(map(int, input().split()))

M = max(score)

avg = (sum(score)/M*100)/N

print(avg)