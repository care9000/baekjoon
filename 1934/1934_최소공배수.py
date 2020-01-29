import sys
sys.stdin = open('1934_최소공배수.txt')

def gcd(a, b):
    while (b > 0):
        temp = b
        b = a % b
        a = temp
    return a


T = int(input())
for tc in range(1, T + 1):
    num_1, num_2 = map(int, input().split())

    a = max(num_1, num_2)
    b = min(num_1, num_2)

    gcd_num = (gcd(a, b))
    print((a * b) //gcd_num)