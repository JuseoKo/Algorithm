[![Solved.ac
프로필](http://mazassumnida.wtf/api/v2/generate_badge?boj=mariat1717)](https://solved.ac/mariat1717)

# 평소에 안쓰던 함수
1. split(슬라이싱할 문자) : 슬라이싱할 문자 사이에 있는 모든 문자열을 슬라이싱해서 리스트로 만들어
2. map(변환할 자료형, 변수) : 자료형을 바꿔주는 함수
3. insert(위치, 값) : 리스트의 해당 위치에 값 삽입
4. '구분자'.join(리스트) : 해당 리스트를 [0]구분자[1]구분자 ... 식으로 반환한다, 리스트의 요소는 str이여야함
5. round(값, 자리수) : 반올림 하는 함수
6. sys.stdin.readline() : input함수에 비해 빠르다, 원인은 prompt message와 개행문자 연산때문
7. sort(key=기준값) : key값을 기준으로 정렬된다. 보통 람다와 같이쓰임

# pypy3 vs python3

>### 1. pypy3
>실행시 자주 쓰이는 코드를 캐싱, 실행속도 빠름, 메모리효율 낮음
>### 2. python3
>캐싱을 안함, 실행속도 느림, 메모리효율 좋음 
