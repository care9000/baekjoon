import sys
sys.stdin = open('1963_소수_경로.txt')
import collections
def simulation(i):
    if i == end_num:
        return 0
    q = collections.deque([])
    q.append([i, 0])
    while len(q):
        num, cnt = q.popleft()
        print(prime_number_list)
        if num == end_num:
            return cnt
        if len(str(num)) == 4:
            for j in range(4):
                if j == 0:
                    for k in range(1, 10):
                        tem_num = str(num)
                        tem_num = str(k) + tem_num[1:]
                        tem_num = int(tem_num)
                        if tem_num not in prime_number_list and is_primenumber(tem_num):
                            prime_number_list.append(tem_num)
                            q.append([tem_num, cnt + 1])

                elif j == 1:
                    for k in range(10):
                        tem_num = str(num)
                        tem_num = tem_num[0] + str(k) + tem_num[2:]
                        tem_num = int(tem_num)
                        if tem_num not in prime_number_list and is_primenumber(tem_num):
                            prime_number_list.append(tem_num)
                            q.append([tem_num, cnt + 1])

                elif j == 2:
                    for k in range(10):
                        tem_num = str(num)
                        tem_num = tem_num[0:1] + str(k) + tem_num[3]
                        tem_num = int(tem_num)
                        if tem_num not in prime_number_list and is_primenumber(tem_num):
                            prime_number_list.append(tem_num)
                            q.append([tem_num, cnt + 1])

                else:
                    for k in range(10):
                        tem_num = str(num)
                        tem_num = tem_num[:3] + str(k)
                        tem_num = int(tem_num)
                        if tem_num not in prime_number_list and is_primenumber(tem_num):
                            prime_number_list.append(tem_num)
                            q.append([tem_num, cnt + 1])





    return ('impossble')


def is_primenumber(num):
    square_root = round(num ** 0.5) + 1
    for i in range(2, square_root):
        if num % square_root == 0:
            return False
    return True


T = int(input())
for tc in range(T):
    prime_number_list = []
    start_num, end_num = map(int, input().split())
    prime_number_list.append(start_num)
    print(simulation(start_num))
