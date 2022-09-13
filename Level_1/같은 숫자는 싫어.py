def solution(arr):
    answer = []
    answer.append(arr[0])
    for i in range(1, len(arr)):
        if arr[i-1] != arr[i]:
            answer.append(arr[i])
        else:
            pass
        continue
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    return answer
print(solution([4,4,4,3,5]))
