SELECT
    YEAR(b.SALES_DATE) as YEAR,
    MONTH(b.SALES_DATE) as MONTH,
    count(distinct b.USER_ID) as PUCHASED_USERS,
    round(count(distinct b.USER_ID)/(
    select
    count(distinct user_id)
    from user_info
    where JOINED like '2021-%'
    ), 1) as PUCHASED_RATIO
FROM USER_INFO a
    JOIN ONLINE_SALE b
ON a.USER_ID=b.USER_ID
WHERE a.JOINED like '2021-%'
GROUP BY YEAR, MONTH
ORDER BY MONTH ASC