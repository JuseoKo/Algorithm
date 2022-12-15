import sys

n = int(sys.stdin.readline())
data = []
re = ''

for i in range(0, n):
    x = sys.stdin.readline().strip('\n')
    data.append(x)

for i in data:
    #남은 글자가 2개 미만일경우까지 반복
    while len(i) >= 1:
        if i.find('()') != -1:
            i = i.replace('()', '')
        else:
            break

    if len(i) == 0 :
        print('YES')
    else:
        print('NO')