"""
5. 다음과 같은 문자열의 배열을 입력받아 모든 문자열에 공통으로 포함된 가장 긴 접두사를 반환하는 함수를 작성하세요
input = ["flower", "flow", "flight", "fli12345", "fli@31"]
output = "fl"
5번 문제, "모든 문자열에 공통으로" 포함된 접두사라고 한다면 fl가 아닌 f가 나와야하는거 아닐까요?
"""


def solution5(input: list) -> str:
    from collections import Counter

    result = []

    # 1.모든 문자열의 prefix를 구합니다.
    for i in input:
        one_text = i
        for j in range(1, len(one_text)):
            result.append(one_text[:j])

    # 2. Counter를 사용하여 prefix의 빈도를 계산합니다.
    counter = Counter(result)

    # 3. 가장 많이 중복된 값을 찾습니다.
    max_count = max(counter.values())

    # 4. 중복된 값들 중에서 최대 빈도수를 가진 값들을 구합니다.
    most_prefixes_list = [
        prefix for prefix, count in counter.items() if count == max_count
    ]

    # 5. 최대 빈도수를 가진 값중 가장 긴 문자열을 반환합니다.
    return max(most_prefixes_list)


input = ["flower", "flow", "flight", "fi12345", "fi@31"]
print(solution5(input))
"""
6번 문제
"""
# def solution6(input: str) -> str:
#     # 1. 결과를 담을 리스트를 선언합니다.
#     result = []
#
#     # 2. 중복문자가 나타날 때 까지 result리스트에 적재합니다. 시간복잡도는 O(N)
#     for i in range(len(input)):
#         if input[i] not in result:
#             result.append(input[i])
#         else:
#             break
#
#     # 결과를 출력합니다.
#     text = ''.join(result)
#     return f'"{text}"길이는 {len(result)}'
#
# input = "abcabcbb"
# solution6(input)

"""
7번 문제
"""


def solution7(nums1: list, nums2: list) -> list:
    # 1. set 함수는 중복을 허용하지 않는점을 이용하여 중복을 제거합니다.
    nums1 = set(nums1)
    nums2 = set(nums2)
    # 2. 교집합을 리턴합니다.
    return list(nums1.intersection(nums2))


# nums1 = [1,2,2,1]
# nums2 = [2,2]
# print(solution7(nums1, nums2))

"""
8번 문제
8. a_info, b_info 테이블에 등록된 모든 사업자번호를 기준으로 사업자번호당 a매체 등록여부, b매체 등록여부를 조회하는 쿼리를 작성하세요.
-- 조회결과의 항목:  사업자번호, A매체 등록여부(O/X), B매체 등록여부(O/X)
"""
sql_8 = """
SELECT "사업자번호",
       MIN(CASE WHEN "A"='O' THEN 'O' ELSE 'X' END) AS "A매체 등록여부(O/X)",
       MIN(CASE WHEN "B"='O' THEN 'O' ELSE 'X' END) AS "B매체 등록여부(O/X)"
FROM (
         SELECT REPLACE(a."사업자번호", '-', '') AS "사업자번호",
                'O' AS "A",
                'X' AS "B"
         FROM a_info AS a
         UNION
         SELECT REPLACE(b."사업자번호", '-', '') AS "사업자번호",
                'X' AS "A",
                'O' AS "B"
         FROM b_info AS b
     ) AS c
GROUP BY "사업자번호"
ORDER BY "사업자번호";
"""

"""
9. 8번 문제에서 조회한 모든 사업자번호의 담당자 및 A매체의 월평균, B매체의 월평균을 조회하는 쿼리를 작성하세요.
-- 담당자가 여러명 일 경우 ,(콤마)로 연결하여 한 문자열로 표시할 것
-- 조회결과의 항목: 사업자번호, A매체 월평균 매출, B매체 월평균 매출, 담당자명
= 해당 사업자번호에 대한 A매체, B매체 월펻균 매출과 담당자명
"""
sql_9 = """
create view view_1 as SELECT 사업자번호,
       STRING_AGG(담당자사번, ', ') AS 담당자사번
FROM (
         SELECT REPLACE(a."사업자번호", '-', '') AS "사업자번호",
                담당자사번
         FROM a_info AS a
         UNION
         SELECT REPLACE(b."사업자번호", '-', '') AS "사업자번호",
                담당자사번
         FROM b_info AS b
     ) AS c
GROUP BY 사업자번호


SELECT
    a.사업자번호,
    b."A매체 월평균 매출",
    c."B매체 월평균 매출",
    a.담당자사번
from view_1 a
left join (
    SELECT AVG(CAST(광고매출 AS numeric)) AS "A매체 월평균 매출", 대상월, 사업자번호
    FROM total_pay
    WHERE 매체코드='A'
    GROUP BY 사업자번호, 대상월
) AS b
on a.사업자번호 = b.사업자번호
left join (
    SELECT AVG(CAST(광고매출 AS numeric)) AS "B매체 월평균 매출", 대상월, 사업자번호
    FROM total_pay
    WHERE 매체코드='B'
    GROUP BY 사업자번호, 대상월
) AS c
on a.사업자번호 = c.사업자번호;
"""

"""
10. 2023년 1월 매출 금액이 존재하는 사업자번호의 2022년도 총매출과 월별 평균 매출을 구하는 쿼리를 작성하세요.
-- 월 매출 평균은 월 매출이 있는 월만 계산하세요
-- 조회결과의 항목 : 사업자번호, 2023년1월 매출, 2022년 총매출, 2022년 월평균매출
"""
sql_10 = """
SELECT
    a.사업자번호,
    b."2023년1월 매출",
    c."2022년 총매출",
    d."2022년 월평균매출"
FROM (
SELECT 사업자번호
FROM total_pay
WHERE 대상월='202301' AND CAST(광고매출 AS integer) > 0
) AS a
LEFT JOIN (
    SELECT
        사업자번호,
        대상월,
        SUM(CAST(광고매출 AS INTEGER)) AS "2023년1월 매출"
    FROM total_pay
    WHERE 대상월='202301'
    GROUP BY 사업자번호, 대상월
) AS b
ON a.사업자번호=b.사업자번호
LEFT JOIN (
    SELECT
        사업자번호,
        대상월,
        SUM(CAST(광고매출 AS INTEGER)) AS "2022년 총매출"
    FROM total_pay
    WHERE 대상월 like '2022%'
    GROUP BY 사업자번호, 대상월
) AS c
ON a.사업자번호=c.사업자번호
LEFT JOIN (
    SELECT
        사업자번호,
        대상월,
        AVG(CAST(광고매출 AS INTEGER)) AS "2022년 월평균매출"
    FROM total_pay
    WHERE 대상월 like '2022%'
    GROUP BY 사업자번호, 대상월
) AS d
ON a.사업자번호=d.사업자번호;
"""
"""
11. 부서별로 2022년도 총매출을 구하고, 각 부서별 최고 매출을 달성한 담당자 이름을 구하시오
-- 부서 총매출이 높은 순서로 정렬할 것
-- 조회결과의 항목 : 소속코드, 2022년 총매출, 최고 매출 달성자
"""
sql_11 = """
create view view_2 as
    SELECT 사업자번호,
           담당자사번,
           소속코드,
           담당자명
    FROM (SELECT REPLACE(a."사업자번호", '-', '') AS "사업자번호",
             담당자사번
      FROM a_info AS a
      UNION
      SELECT REPLACE(b."사업자번호", '-', '') AS "사업자번호",
             담당자사번
      FROM b_info AS b) as a
    LEFT JOIN agent_info  AS b
    ON a.담당자사번=b.담당자사번

SELECT
    a.소속코드,
    SUM(CAST(b.광고매출 AS integer)) AS "2022년 총매출",
    MAX(c.최고_매출_달성자) AS "최고 매출 달성자"
FROM view_2 AS a
LEFT JOIN total_pay b 
ON a.사업자번호 = b.사업자번호
LEFT JOIN (
        SELECT
            a.소속코드,
            a.담당자명 AS 최고_매출_달성자,
            SUM(CAST(b.광고매출 AS integer)) AS 매출액
        FROM
            view_2 AS a
                LEFT JOIN
            total_pay b ON a.사업자번호 = b.사업자번호
        WHERE
            b.대상월 LIKE '2022%'
        GROUP BY
            a.소속코드, a.담당자명
    ) AS c ON a.소속코드 = subquery.소속코드
WHERE
    b.대상월 LIKE '2022%'
GROUP BY
    a.소속코드;
"""
