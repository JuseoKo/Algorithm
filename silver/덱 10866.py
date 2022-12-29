import sys
n = int(sys.stdin.readline())

Deque = []
res = []

def de(s):
    # print(s)
    if s.find('push_front') != -1:
        c, d = s.split(' ')
        Deque.append(str(d))
    elif s.find('push_back') != -1:
        c, d = s.split(' ')
        Deque.insert(0, d)
    elif s.find('pop_front') != -1:
        if len(Deque) != 0:
            res.append(str(Deque.pop()))
        else:
            res.append(str(-1))
    elif s.find('pop_back') != -1:
        if len(Deque) != 0:
            res.append(str(Deque[0]))
            del Deque[0]
        else:
            res.append(str(-1))
    elif s.find('size') != -1:
        res.append(str(len(Deque)))
    elif s.find('empty') != -1:
        if len(Deque) == 0:
            res.append(str(1))
        else:
            res.append(str(0))
    elif s.find('front') != -1:
        if len(Deque) != 0:
            res.append(str(Deque[len(Deque)-1]))
        else:
            res.append(str(-1))
    elif s.find('back') != -1:
        if len(Deque) != 0:
            res.append(str(Deque[0]))
        else:
            res.append(str(-1))




for i in range(n):
    s = sys.stdin.readline().rstrip()
    de(s)
print('\n'.join(res))