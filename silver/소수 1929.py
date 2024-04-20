m, n = map(int, input().split(" "))
data = [True] * int(n + 1)
for i in range(
    2, int(n**0.5) + 1
):  # 2부터 n의 제곱근까지, n = x*y 라면 x나 y 중 하나는 n의 제곱근 이하여야 하므로 제곱근까지만 구하면된다
    if data[i] == True:  # i가 소수인 경우 (남은 수인 경우)
        # i를 제외한 i의 모든 배수를 지우기 위해 j를 2로 설정한다
        j = 2
        while i * j <= n:
            data[i * j] = False
            j += 1

# 모든 소수 출력
for i in range(m, n + 1):
    if data[i]:
        if i != 1:
            print(i)
