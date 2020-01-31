import sys
sys.stdin = open('16673_고려대학교에는_공식_와인이_있다.txt')

C, K, P = map(int, input().split())

data = []
for i in range(1, C + 1):
    data.append((K * i) + P * (i ** 2))
print(sum(data))
