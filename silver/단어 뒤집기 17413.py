import sys

word = sys.stdin.readline().rstrip('\n')
i = 0
while i <= len(word)-1:
    c = word[i]
    # 열린괄호 만나면 닫힌괄호 나올떄까지 존버
    if word[i] == '<':
        while word[i] != '>':
            i += 1
        i += 1
    #공백이면 넘어가기
    elif word[i] == ' ':
        i += 1
    #그외에는 거꾸로
    else:
        #바꿀문자 범위 구하기
        j = 0
        while word[i+j] != '<' and word[i+j] != ' ' and i+j != (len(word)-1):
            j += 1
        if i+j == (len(word)-1):
            j += 1
        #바꾸기
        word = word[:i] + word[i:i+j][::-1] + word[i+j:]
        i = i+j
print(word)