import sys
sys.stdin = open('1932_정수_삼각형.txt')

n = int(input())
triangle = [list(map(int, input().split())) for _ in range(n)]

for i in range(1, n):
    for j in range(i + 1):
        if j == 0:
            triangle[i][j] += triangle[i - 1][0]
        elif j == i:
            triangle[i][j] += triangle[i - 1][j - 1]
        else:
            triangle[i][j] += max(triangle[i - 1][j - 1], triangle[i - 1][j])
print(max(triangle[-1]))
print(triangle)