import sys
num = int(sys.stdin.readline())
data_list = []

def quick_sort(ar):
    if len(ar) <= 1:
        return ar
    pivot, data = ar[0], ar[1:]
    left = [x for x in data if x <= pivot]
    right = [x for x in data if x > pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)

#입력
for i in range(0, num):
    data_list.append(int(sys.stdin.readline()))
res = quick_sort(data_list)
for i in res:
    print(int(i))