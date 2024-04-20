import sys

# 입력
N = sys.stdin.readline()
table = []
sort = ""
for i in range(0, len(N)):
    table.append(N[len(N) - i - 1])
table.sort()

for i in range(0, len(table)):
    sort += table[len(table) - i - 1]

print(sort)
