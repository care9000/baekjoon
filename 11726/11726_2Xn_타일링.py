import sys
sys.stdin = open('11726_2Xn_타일링.txt')

n = int(input())

fibo = [1, 2]

if n > 2:
    for i in range(n - 2):
        fibo.append((fibo[i] + fibo[i + 1]) % 10007)
    print(fibo[n - 1])
else:
    print(fibo[n - 1])