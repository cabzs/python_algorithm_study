N = int(input())
for i in range(N):
    print(" " * i, "*" * ((N - i) * 2 - 1), sep="")
for i in range(1, N):
    print(" " * (N - i - 1), "*" * (i * 2 + 1), sep="")