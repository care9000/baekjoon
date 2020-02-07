import sys
sys.stdin = open('3678_카탄의_개척자.txt')






N = int(input())
info = list(int(input()) for _ in range(N))
data = [0, 1, 2, 3, 4, 5, 2, 3]
uses = [0, 1, 2, 2, 1, 1]
max_num = max(info)

i = 1
num = 2
while i < max_num:
    i += 1
    tem = 987654321
    tem_use = 987654321
    for k in range(1, 6):
        if k != data[-1] and tem > k and uses[k] < tem_use:
            tem = k
            tem_use = uses[k]

    data.append(tem)
    uses[tem] += 1
    start = len(data)
    for j in range((6 * i) - 2):
        if i % 2 == 0:

            if (len(data) - 1) % 2 == 1 :
                tem = 987654321
                tem_use = 987654321
                for k in range(1, 6):
                    if k != data[-1] and k != data[num] and uses[k] < tem_use:
                        tem = k
                        tem_use = uses[k]
                data.append(tem)
                uses[tem] += 1
            else:
                tem = 987654321
                tem_use = 987654321
                for k in range(1, 6):
                    if k != data[-1] and k != data[num] and k != data[num + 1] and uses[k] < tem_use:
                        tem = k
                        tem_use = uses[k]
                        num += 1
                data.append(tem)
                uses[tem] += 1

        else:
            if i % 2 == 0:
                tem = 987654321
                tem_use = 987654321
                for k in range(1, 6):
                    if k != data[-1] and k != data[num] and k != data[num + 1] and uses[k] < tem_use:
                        tem = k
                        tem_use = uses[k]
                        num += 1
                data.append(tem)
                uses[tem] += 1
            else:
                if (len(data) - 1) % 2 == 1:
                    tem = 987654321
                    tem_use = 987654321
                    for k in range(1, 6):
                        if k != data[-1] and k != data[num] and uses[k] < tem_use:
                            tem = k
                            tem_use = uses[k]
                    data.append(tem)
                    uses[tem] += 1
    for k in range(1, 6):
        if kk != data[-1] and k != data[num] and k != data[num + 1] and uses[k] < tem_use:
            tem = k
            tem_use = uses[k]
            num += 1
    data.append(tem)
    uses[tem] += 1
print(data[4])