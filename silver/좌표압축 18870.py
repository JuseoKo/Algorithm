import sys

n = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))
# 정렬
num1 = list(sorted(set(num)))
# 해당 정렬을 딕셔너리로 바꿔서 시간복잡도를 줄임
dic = {num1[i]: i for i in range(len(num1))}

for i in num:
    print(dic[i], end=" ")
