N = input()
res = 0
while N >= 0:
    if N%5 == 0:
        res += N/5
        break
    N -= 3
    res += 1
else:
    res = -1
print(int(res))