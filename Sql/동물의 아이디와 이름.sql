-- 문제 주소 : https://school.programmers.co.kr/learn/courses/30/lessons/59403
SELECT  ANIMAL_ID, NAME
FROM ANIMAL_INS
ORDER BY ANIMAL_ID ASC

-- 동물 수 찾기 https://school.programmers.co.kr/learn/courses/30/lessons/59041
SELECT *
FROM (SELECT  name,  COUNT(name) as COUNT
      FROM ANIMAL_INS
      WHERE NAME IS NOT NULL
      GROUP BY name
      ORDER BY name) x
WHERE COUNT > 1