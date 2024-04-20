import sys

x = sys.stdin.readline()
stack = []
pr = []


def set(word):
    if word.find("push") != -1:
        a, b = word.split(" ")
        stack.append(int(b))
    elif word.find("pop") != -1:
        if len(stack) == 0:
            pr.append(-1)
        else:
            pr.append(stack[len(stack) - 1])
            del stack[len(stack) - 1]
    elif word.find("size") != -1:
        pr.append(len(stack))
    elif word.find("empty") != -1:
        if len(stack) == 0:
            pr.append(1)
        else:
            pr.append(0)
    elif word.find("top") != -1:
        if len(stack) == 0:
            pr.append(-1)
        else:
            pr.append(stack[len(stack) - 1])


word = [sys.stdin.readline() for i in range(0, int(x))]
for i in word:
    set(i)
for i in pr:
    print(i)
