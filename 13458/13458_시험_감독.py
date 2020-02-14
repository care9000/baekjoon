import sys
sys.stdin = open('13458_시험_감독.txt')

N = int(input())
A = list(map(int, sys.stdin.readline().split()))
B, C = map(int, input().split())

# 시험장 내의 응시자 수
cnt = 0
if B < max(A):
    memo = [0 for _ in range(max(A) + 1)]
    for i in range(1, B + 1):
        memo[i] = 1

    tem = 1
    memo[B + 1] = memo[B] + 1
    for i in range(B + 2, len(memo)):
        if (tem * C) + B < i:
            memo[i] = memo[i - 1] + 1
            tem += 1
        else:
            memo[i] = memo[i - 1]

    result = 0



else:
    memo = [0 for _ in range(B + 1)]
    for i in range(1, B + 1):
        memo[i] = 1
    result = 0
for people in A:
    result += memo[people]

print(result)



