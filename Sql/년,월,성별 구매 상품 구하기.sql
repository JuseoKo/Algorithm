-- https://school.programmers.co.kr/learn/courses/30/lessons/131532
SELECT YEAR(SALES_DATE) as YEAR, MONTH(SALES_DATE) as MONTH, USER_INFO.GENDER, COUNT(DISTINCT USER_INFO.USER_ID) AS USERS
from USER_INFO, ONLINE_SALE
where USER_INFO.USER_ID = ONLINE_SALE.USER_ID and not GENDER is null
group by YEAR, MONTH, GENDER

-- https://school.programmers.co.kr/learn/courses/30/lessons/59412
SELECT HOUR(DATETIME) as HOUR, count(*) as COUNT
from ANIMAL_OUTS
group by HOUR
having HOUR > 8 and HOUR < 20
order by HOUR