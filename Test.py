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
bin = set(num_list)
bin_s = []
c = 0
p = 0
for i in bin:
    bin_s.append(num_list.count(i))
# print(sum(bin_s[:2]))
for i in range(0, len(bin_s)):
    if bin_s[i] > bin_s[i-1]:
        c = sum(bin_s[:i])
        p = 0
    elif bin_s[i] == bin_s[i-1]:
        if p == 0:
            c = sum(bin_s[:i+1])
            p = 1
        else:
            pass
if len(num_list) == 1:
    print(num_list[0])
else:
    print(num_list[c])


#네번째줄 범위
print(int(num_list[-1])-int(num_list[0]))
