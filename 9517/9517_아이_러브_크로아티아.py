import sys
sys.stdin = open('9517_아이_러브_크로아티아.txt')
import collections

def simulation():
    time = 0
    for t in range(info_num):
        # 만약 시간이 210초를 넘기게 되면 그사람이 터지므로 조건문 걸어줌
        if time + int(info[t][0]) < 210:
            time += int(info[t][0])
            # 맞췃을 경우에는 다음 사람으로 넘기고 아니면 그사람이 한번더 문제를 품
            if info[t][1] == 'T':
                q.append(q.popleft())

        else:
            return q[0]


q = collections.deque([i for i in range(1, 9)])
start_num = int(input())
# 시작 숫자와 q[0]의 숫자를 맞춰 주기 위하여
while start_num != q[0]:
    q.append(q.popleft())

info_num = int(input())
info = [list(input().split()) for _ in range(info_num)]
print(simulation())