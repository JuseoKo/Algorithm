inp = int(input())
num_list, res = [], 0

#입력
for i in range(0, inp):
    num = int(input())
    num_list.append(num)

num_list.sort()

#첫째줄 산술평균
for i in num_list:
    res += i
res = int(round(res/len(num_list), 0))
print(res)
#두번째줄 중앙값
print(num_list[round(int(len(num_list)/2), 1)])

#세번째줄 최빈값(최빈값(가장 많이 관측되는 수)이 여러개일 경우 두번째 최빈값)
def clu():
    global bin, bin_f, bin_s, f
    # print(f'헤더 -> {num_list[i]}, 카운트 : {bin_f}, f값 {f}')
    #카운트 센게 더 많으면 갱신
    if bin > bin_f[0]:
        bin_f = [bin, num_list[i]]
        # print(f'큳 -> {num_list[i]}, 카운트 : {bin}변경점 : {bin_f}')
        f, bin = 0, 0
    #카운트 센거와 같으면 세컨드
    elif bin == bin_f[0]:
        f += 1
        if f == 1:
            bin_s = [bin, num_list[i]]
        # print(f'같다 -> {num_list[i]}, 카운트 : {bin}변경점 : {bin_s}')
        bin = 0
    #카운트 센게 작을경우
    else:
        bin = 0
        #[1 1 1 2 3 3 3 4 4 4 5]
#카운트, 숫자
bin, bin_f, bin_s, f= 0, [0, num_list[0]], [0, 0], 0
for i in range(0, len(num_list)):
    bin += 1
    # 0 < i < num_list 일경우
    if i < len(num_list)-1:
        #미래값과 다를경우
        if num_list[i] != num_list[i+1]:
            clu()
        # 미래값과 같을경우 카운트 +1
        else:
            pass
    # i = num_list일경우
    elif i == len(num_list)-1:
        if num_list[i] == num_list[i-1]:
            clu()

if f >= 1:
    print(bin_s[1])
else:
    print(bin_f[1])
#네번째줄 범위
print(int(num_list[-1])-int(num_list[0]))