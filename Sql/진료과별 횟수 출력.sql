-- https://school.programmers.co.kr/learn/courses/30/lessons/132202
SELECT MCDP_CD as '진료과코드', count(MCDP_CD) as '5월예약건수'
fROM APPOINTMENT
WHERE APNT_YMD like '2022-05%'
GROUP by MCDP_CD
order by 5월예약건수 asc, 진료과코드 asc