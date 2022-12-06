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