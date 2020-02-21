import sys
sys.stdin = open('10775_공항.txt')

G = int(input())
P = int(input())
gates = [0 for _ in range(G + 1)]
cnt = 0
max_plane = G
while 1:
    flag = 0
    plane = int(input())
    if max_plane < plane:
        plane = max_plane

        if gates[plane] == 0:
            cnt += 1
            flag = 1
            max_plane -= 1
            gates[plane] = 1
        else:
            for i in range(plane - 1, 0, -1):
                if gates[i] == 0:
                    gates[i] = 1
                    flag = 1
                    cnt += 1
                    break

    else:
        for i in range(plane, 0, -1):
            if gates[i] == 0:
                gates[i] = 1
                flag = 1
                cnt += 1
                break

    if flag == 0:
        break

print(cnt)
