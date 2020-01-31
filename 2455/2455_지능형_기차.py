import sys
sys.stdin = open('2455_지능형_기차.txt')

def simulration(stop, people):
    global result
    if people > result:
        result = people
    # 1~ 3번 역에서 내리고 손님 탓음
    if stop < 3:
        for i in range(2):
            if i == 0:
                people -= station[stop][0]
            else:
                people += station[stop][1]
        if people >= 10000:
            result = people
            return
        simulration(stop + 1, people)
    elif stop == 3:
        for i in range(2):
            if i == 0:
                people -= station[stop][0]
            else:
                people += station[stop][1]
        if people >= 10000:
            result = people
            return

station = [list(map(int, input().split())) for _ in range(4)]
result = 0
simulration(0, 0)
print(result)