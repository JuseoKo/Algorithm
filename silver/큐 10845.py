import sys
n, order, q, res = int(sys.stdin.readline()), [], [], []
def queue(order, num):
    global res, q
    if order == 'push':
        q.append(num)
    elif order == 'pop':
        if len(q) == 0:
            res.append(-1)
        else:
            res.append(q[0])
            del q[0]
    elif order == 'size':
        res.append(len(q))
    elif order == 'empty':
        if len(q) == 0:
            res.append(1)
        else:
            res.append(0)
    elif order == 'front':
        if len(q) == 0:
            res.append(-1)
        else:
            res.append(q[0])
    elif order == 'back':
        if len(q) == 0:
            res.append(-1)
        else:
            res.append(q[len(q)-1])


for i in range(0, n):
    code = sys.stdin.readline().strip()
    if code.find('push') != -1:
        order, num = code.split(' ')
    else:
        order, num = str(code), None
    queue(order, num)

for i in res:
    print(i)