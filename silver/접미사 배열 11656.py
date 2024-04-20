import sys

s = sys.stdin.readline().strip()
s_list = []
for i in range(len(s)):
    s_list.append(s[i : len(s)])
s_list.sort()
for i in s_list:
    print(i)
