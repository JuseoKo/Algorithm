-- https://school.programmers.co.kr/learn/courses/30/lessons/59044
SELECT NAME as NAME, DATETIME as DATETIME
from ANIMAL_INS
where ANIMAL_ID not in (select ANIMAL_ID from ANIMAL_OUTS)
order by DATETIME
limit 3

-- https://school.programmers.co.kr/learn/courses/30/lessons/59045
SELECT ANIMAL_INS.ANIMAL_ID, ANIMAL_INS.ANIMAL_TYPE, ANIMAL_INS.NAME
FROM ANIMAL_INS, ANIMAL_OUTS
WHERE ANIMAL_INS.ANIMAL_ID = ANIMAL_OUTS.ANIMAL_ID and ANIMAL_INS.SEX_UPON_INTAKE != ANIMAL_OUTS.SEX_UPON_OUTCOME
ORDER BY ANIMAL_INS.ANIMAL_ID

-- https://school.programmers.co.kr/learn/courses/30/lessons/59411
SELECT i.ANIMAL_ID, o.NAME
from ANIMAL_INS i, ANIMAL_OUTS o
where i.ANIMAL_ID = o.ANIMAL_ID
order by i.DATETIME - o.DATETIME
limit 2


-- https://school.programmers.co.kr/learn/courses/30/lessons/144856
SELECT a.AUTHOR_ID, b.AUTHOR_NAME, a.CATEGORY, sum((a.PRICE*c.	SALES)) as 	TOTAL_SALES
from BOOK a, AUTHOR b, BOOK_SALES c
where a.AUTHOR_ID = b.AUTHOR_ID and a.BOOK_ID = c.BOOK_ID and SALES_DATE like '2022-01%'
group by a.CATEGORY ,b.author_name
order by a.AUTHOR_ID, a.CATEGORY desc