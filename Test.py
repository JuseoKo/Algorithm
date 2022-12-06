N, M = map(int, input().split(' '))
N_l = []
M_l = []
for i in range(0, N):
    insert = input().split(' ')
    M_l.append(insert)
for i in range(0, N):
    insert = input().split(' ')
    N_l.append(insert)

for i in range(0, N):
    for j in range(0, M):
        M_l[i][j] = str(int(M_l[i][j])+int(N_l[i][j]))

for i in range(0, len(M_l)):
    print(' '.join((M_l[i])))



#split(슬라이싱할 문자) : 슬라이싱할 문자 사이에 있는 모든 문자열을 슬라이싱해서 리스트로 만들어
#map(변환할 자료형, 변수) : 자료형을 바꿔주는 함수
#insert(위치, 값) : 리스트의 해당 위치에 값 삽입
#'구분자'.join(리스트) : 해당 리스트를 [0]구분자[1]구분자 ... 식으로 반환한다, 리스트의 요소는 str이여야함
