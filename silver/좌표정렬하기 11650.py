import sys
n = int(sys.stdin.readline())
num = []
for i in range(0, n):
    n_x, n_y = map(int, sys.stdin.readline().split(' '))
    num.append([n_x, n_y])

num.sort(key=lambda x:(x[0], x[1]))

for i in num:
    print(i[0], i[1])