import sys
sys.stdin = open('1351_무한수열.txt')


def dfs(num):
    if num == 0:
        return 1
    elif num < 1000000:
        if A[num]:
            return A[num]

        else:
            A[num] = dfs(num // P) + dfs(num // Q)
            return A[num]
    else:
        return dfs(num // P) + dfs(num // Q)


N, P, Q = map(int, input().split())
i = 1
A = [0 for _ in range(1000000)]
A[0] = 1

print(dfs(N))