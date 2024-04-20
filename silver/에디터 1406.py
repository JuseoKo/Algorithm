import sys

base, base1 = list(sys.stdin.readline().rstrip()), []

for i in range(int(sys.stdin.readline().rstrip())):
    ed = sys.stdin.readline().rstrip()
    # P가 존재하면 삽입
    if ed[0] == "P":
        base.append(ed[2])
    # 커서를 왼쪽으로 옮김
    elif ed[0] == "L" and base:
        base1.append(base.pop())
    # 커서를 오른쪽으로 옮김
    elif ed[0] == "D" and base1:
        base.append(base1.pop())
    # 커서 왼쪽 문자 삭제
    elif ed[0] == "B" and base:
        base.pop()
    # print(base, base1, ed[0])
# 출력
base1.reverse()
print("".join(base + base1))
