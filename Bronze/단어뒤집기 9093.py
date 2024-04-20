import sys

n = int(sys.stdin.readline())
sr = []
for i in range(0, n):
    x = sys.stdin.readline()
    sr.append(x)
for i in range(0, len(sr)):
    sr_s = sr[i].split(" ")
    c = ""
    for j in range(0, len(sr_s)):
        if j != 0:
            c = c + " "
        for k in range(0, len(sr_s[j])):
            c = c + sr_s[j][len(sr_s[j]) - k - 1]
    print(c.replace("\n", ""))
