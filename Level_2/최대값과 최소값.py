import re
def solution(s):
    data = s.split()
    datas = []
    for i in range(0, len(data)):
        datas.append(int(data[i]))
    answer = f'{min(datas)} {max(datas)}'
    return answer

# map(타입, 파라미터) : 리스트나 튜플을 지정된 타입으로 만들어주는 함수.

print(solution('-1 -2 -3 4'))