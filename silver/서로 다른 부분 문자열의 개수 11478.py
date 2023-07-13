# 서로 다른 문자열의 갯수를 구하는 알고리즘
import sys

_set = set()
x = sys.stdin.readline().rstrip('\n')
for i in range(1, len(x) + 1):
    for j in range(len(x)):
        _set.add(x[j:i + j])
print(len(_set))
