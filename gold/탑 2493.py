# 입력 : 탑의 수 N, 각 탑의 높이
# 출력 : 각 탑의 수신 탑의 번호

import sys

N = sys.stdin.readline()
top = list(map(int, input().split()))
# 첫번째 탑이 보낸 신호는 누구도 받을 수 없으므로 무조건 0이다.
result = [0]
stack = []

for i in range(int(N)):
    while stack:
        if stack[-1][1] > int(top[i]):
            result.append(stack[-1][0] + 1)
            break
        else:
            stack.pop()
            if len(stack) == 0:
                result.append(0)
                break

    stack.append([i, int(top[i])])


print(" ".join(map(str, result)))
