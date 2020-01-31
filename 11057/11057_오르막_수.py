import sys
sys.stdin = open('11057_오르막_수.txt')
N = int(input())
dummy = 10
result = 1
for i in range(N):
    result *= dummy
    dummy += 1

for i in range(1, N + 1):
    result //= i
print(result % 10007)