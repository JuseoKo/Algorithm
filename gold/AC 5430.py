#덱 : 양쪽으로 입출력이 가능한 자료구조
import sys
# 총 횟수
T = int(sys.stdin.readline())
com_list = []

# 명령어 반복
for i in range(T):
    # 명령 구문
    com = sys.stdin.readline().strip().split()
    # 배열 수
    n = int(sys.stdin.readline())
    #문자열 리스트화
    arr = sys.stdin.readline().rstrip().replace('[', '').replace(']', '').split(',')
    com_list.append([com, n, arr])
#에러확인
for j in range(len(com_list)):
    # print(com_list[j][0][0], com_list[j][1])
    if com_list[j][0][0].count('D') > com_list[j][1]:
        print('error')
    else:
        #명령문 수행
        L = 1
        for i in range(len(com_list[j][0][0])):
            te = com_list[j][0][0][i]
            if com_list[j][0][0][i] == 'D':
                if L%2 == 1:
                    del com_list[j][2][0]
                else:
                    del com_list[j][2][len(com_list[j][2])-1]
            else:
                L += 1
        if L%2 == 1:
            print(str(com_list[j][2]).replace(' ', '').replace('\'', ''))
        else:
            com_list[j][2].reverse()
            print(str(com_list[j][2]).replace(' ', '').replace('\'', ''))