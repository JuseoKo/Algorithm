# n = 배열의 수 nxn
# arr1 = 첫번째 지도 , 2진수로 주어짐
# arr2 = 두번째 지도
# 결과는 1 = # , 0 = 공백  으로 이루어진 지도를 리스트 형식으로 나타내야함


def solution(n, arr1, arr2):
    # 2진수 복호기
    answer = []
    lists = []
    lists1 = []
    kL = []
    Te = ""
    for i in range(0, n):
        d = format(arr1[i], "0b")
        for j in range(0, n):
            try:
                if d[j] == "1":
                    lists.append("#")
                else:
                    lists.append(" ")
            except:
                lists.insert(0, " ")
        for b in range(0, n):
            Te += lists[b]
        answer.append(Te)
        Te = ""
        lists = []

    for i in range(0, n):
        d1 = format(arr2[i], "0b")
        for j in range(0, n):
            try:
                if d1[j] == "1":
                    lists.append("#")
                else:
                    lists.append(" ")
            except:
                lists.insert(0, " ")
        for b in range(0, n):
            Te += lists[b]
        lists1.append(Te)
        Te = ""
        lists = []

    for k in range(0, n):
        if answer[k] == lists1[k]:
            pass
        else:
            for l in range(0, n):
                if answer[k][l] != lists1[k][l]:
                    kL.insert(l, "#")
                else:
                    kL.insert(l, answer[k][l])

            for b in range(0, n):
                Te += kL[b]
            answer[k] = Te
            Te = ""

    return answer


print(solution(4, [20, 28, 18, 11], [21, 17, 28, 3]))
# print(format(9, '0b'))
