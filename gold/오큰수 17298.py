import sys

n = int(sys.stdin.readline().rstrip())
num = list(map(int, sys.stdin.readline().split()))
res = [-1] * n
stack = [0]

for i in range(1, n):
    while stack and num[stack[-1]] < num[i]:
        res[stack.pop()] = num[i]
    stack.append(i)

for i in range(len(res)):
    print(res[i], end=" ")
