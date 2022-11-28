# def sugar(N):
#     mins = 3
#     max = 5
#     c = 0
#     data = 0
#     result = 0
#     while (N-data)%mins != 0:
#         if N-data < 3:
#             result = -1
#             print('2번',c)
#             return result
#         elif N-data%max == 0:
#             print('3번',c)
#             result = c
#             return result
#         else:
#             data += max
#             c += 1
#             print('1번',(N-data)%mins, N-data)
#     if N%max == 0:
#         result = N/max
#     else:
#         result = c+(N-data)/mins
#     return result
#
# #1. N값에서 5를 뺀다
# #2. 이를 N%3 = 0 이 나올때까지 반복한다
# #3. N%3 = 0이 나왔다면 지금까지 5를 더한 횟수 + N/3이 결과가 된다.
# #4. 끝까지 N%3=0이 나오지 않는다면 결과는 -1로 한다
#
# print(sugar(19))
N = input()
res = 0
while N >= 0:
    if N%5 == 0:
       res += N/5
       break
    N -= 3
    res += 1
else:
    res = -1
print(int(res))
