"""
n = 1 , 1
n = 2 , 3
n = 3 , 5
n = 4 , 11
즉 점화식은 (n-1)+2*(n-2)
다이나믹 프로그래밍을 이용해 이전 계산 결과를 활용하면 다음과 같음
"""
import sys

n = int(sys.stdin.readline())
arr = [1, 3] + [0] * 1000
for i in range(2, n):
    arr[i] = arr[i - 1] + 2 * arr[i - 2]

print(arr[n - 1] % 10007)
