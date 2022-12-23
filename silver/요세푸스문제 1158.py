import sys
n, k = map(int, sys.stdin.readline().split(' '))
it = [i for i in range(1, n+1)]
res = []
c = 0

for i in range(n):
    c += k-1
    if c >= len(it):
        c = c % len(it)

    res.append(str(it.pop(c)))
print('<'+', '.join(res)+'>')