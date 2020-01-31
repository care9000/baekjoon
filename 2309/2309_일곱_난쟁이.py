import sys
sys.stdin = open('2309_일곱_난쟁이.txt')
def Powerset(m, Person_sum, Person_height):
    global flag
    # 한번만 결과나오면 나머지는 안해도됨
    if flag:
        if Person_height > 100:
            return
        elif Person_sum > 7:
            return
        elif m == 9:
            if Person_sum == 7 and Person_height == 100:
                for i in range(9):
                    if A[i]:
                        print(dwarf_list[i])
                        flag = 0

        else:
            A[m] = 1
            Powerset(m + 1, Person_sum + 1, Person_height + dwarf_list[m])
            A[m] = 0
            Powerset(m + 1, Person_sum, Person_height)



dwarf_list = [int(input()) for _ in range(9)]
dwarf_list = sorted(dwarf_list)

A = [0 for _ in range(9)]
flag = 1
Powerset(0, 0, 0)
