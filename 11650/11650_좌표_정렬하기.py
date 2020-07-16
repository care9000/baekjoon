import sys
sys.stdin = open('11650_좌표_정렬하기.txt')

N = int(input())
data = [list(map(int, input().split())) for _ in range(N)]
data = sorted(data)
for d in data:
    print(d[0], d[1])