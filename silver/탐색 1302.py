# 1. 첫번째줄에 N
# 2. 두번째줄부터 문자열 입력받음
# 3. 가장 많이 들어온 문자열 출력
# 4. 만약 가장 많이 팔린 책이 여러개라면 정렬(asc)하고 가장 앞에있는 데이터를 선택한다.
import sys
N = int(sys.stdin.readline().rstrip())
word_dict = {}
for i in range(0, N):
    word = sys.stdin.readline().rstrip()
    word_dict[word] = word_dict.get(word, 0) + 1

# 알파벳 순으로 정렬(기본적으로 첫번째 값을 가지고 비교함)
sorted(list(word_dict.items()))

# value값을 기준으로 재정렬 후 맨 첫번째 요소 선택
print(sorted(list(word_dict.items()), key=lambda x: x[1], reverse=True)[0][0])




