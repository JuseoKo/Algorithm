-- https://school.programmers.co.kr/learn/courses/30/lessons/131535
SELECT count(AGE) as USERS
FROM USER_INFO
WHERE AGE >= 20 ANd AGE <= 29 AND JOINED < '2022-01-01' and JOINED >= '2021-01-01'