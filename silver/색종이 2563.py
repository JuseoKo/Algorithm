# 색종이
# 기본 False, 색종이가 올라가면 True로 바뀜
back_paper = [[False]*100]
for i in range(0,99):
    back_paper += [[False]*100]
#색종이수
num =  int(input())

#색종이 크기
size_list = []
for i in range(0, num):
    size_x, size_y = map(int, input().split(' '))

    #페이지 설정
    # y축 설정
    paper = [[False]*100]
    for i in range(0,99):
        paper += [[False]*100]
        #y축설정
    for j in range(size_y, size_y+10):
        #x축 설정
        for k in range(size_x, size_x+10):
            paper[-(k+1)][j] = True
    #계산
    for q in range(0, len(paper)):
        for w in range(0, len(paper)):
            back_paper[q][w] = back_paper[q][w] or paper[q][w]

res = 0
for i in range(0, len(back_paper)):
    res += sum(back_paper[i])
print(res)