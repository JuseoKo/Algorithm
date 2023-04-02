-- https://school.programmers.co.kr/learn/courses/30/lessons/131117
SELECT b.PRODUCT_ID, a.PRODUCT_NAME, sum(AMOUNT) * a.PRICE as 'TOTAL_SALES'
from FOOD_PRODUCT a
         join FOOD_ORDER b
              on a.PRODUCT_ID = b.PRODUCT_ID
where b.PRODUCE_DATE >= '2022-05-01' and b.PRODUCE_DATE < '2022-06-01'
group by a.PRODUCT_NAME
order by TOTAL_SALES desc, b.PRODUCT_ID