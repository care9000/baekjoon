n, m = map(int, input().split())
result = 1
for cnt in range(1, m + 1):
    result *= n - (cnt - 1)
    result /= cnt
print(int(result))