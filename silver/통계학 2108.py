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
#카운트, 숫자
bin_f, bin_s, bin, p = [0, num_list[0]], [0, 0], 0, 0

if len(num_list) != 1:
    bin_f = [0, num_list[1]]

for i in range(0, len(num_list)):
    #카운트 증가
    bin += 1
    if num_list[i] != num_list[i-1]:
        #최빈값이 업데이트 된다면
        if bin_f[0] < bin:
            #두개 이상일 경우를 대비해 따로 저장
            bin_s = bin_f
            #업데이트
            bin_f = [bin, num_list[i]]
            p, bin = 2, 0
            # print(bin_f, bin_s)
        #최빈값이 여러개라면
        elif bin_f[0] == bin:
            p, bin = 1, 0
    else:
        #같다면 패스
        pass
#모두 한개씩만 존재한다면
#최빈값이 여러개
if p == 1:
    print(bin_s[1])
#최빈값이 한개
else:
    print(bin_f[1])

#최빈값 판별
#1. 같은 숫자가 몇번 반복되는지 센다
#2. 센 숫자를 저장한다
#3. 최빈값이 업데이트 될 경우 갈아끼우고 최빈값이 두개 이상일 경우를 대비해 따로 저장해둔다
#4. 만약 최빈값이 두개 이상이라면 두번째로 작은 수를 출력한다

#네번째줄 범위
print(num_list[-1], num_list[0])
print(int(num_list[-1])-int(num_list[0]))