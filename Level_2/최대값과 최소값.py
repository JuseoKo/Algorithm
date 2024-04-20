def solution(s):
    data = s.split()
    datas = []
    for i in range(0, len(data)):
        datas.append(int(data[i]))
    answer = f"{min(datas)} {max(datas)}"
    return answer


print(solution("-1 -2 -3 4"))
