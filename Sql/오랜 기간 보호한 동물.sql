-- https://school.programmers.co.kr/learn/courses/30/lessons/59044
SELECT NAME as NAME, DATETIME as DATETIME
from ANIMAL_INS
where ANIMAL_ID not in (select ANIMAL_ID from ANIMAL_OUTS)
order by DATETIME
    limit 3