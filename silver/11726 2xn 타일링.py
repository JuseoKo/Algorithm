"""
n = 1 , 1
n = 2 , 2
n = 3 , 3
n = 4 , 5
n = 5 , 8
즉 N-1개일 때와 N-2개일 때를 더한 값이 나온다
다이나믹 프로그래밍(이전에 계산한 값을 이용해 재사용 하는 기법) 을 이용
"""

import sys
n = int(sys.stdin.readline())
arr = [1, 2] + [0]*1000
for i in range(2, n):
    arr[i] = arr[i-1]+arr[i-2]

print(arr[n-1]%10007)