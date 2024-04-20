import sys

n = int(sys.stdin.readline())
balloon = list(enumerate(map(int, sys.stdin.readline().strip().rsplit(" "))))

burst_order = []

next_index = 0
for _ in range(n):
    burst_order.append(balloon[next_index][0] + 1)
    move = balloon[next_index][1]
    balloon.pop(next_index)
    if not balloon:  # 리스트가 비어있을 경우 루프를 빠져나감
        break
    if move > 0:
        next_index = (next_index + move - 1) % len(balloon)
    else:
        next_index = (next_index + move) % len(balloon)

print(" ".join(map(str, burst_order)))
