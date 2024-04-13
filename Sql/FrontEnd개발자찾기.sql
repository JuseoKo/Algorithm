SELECT DISTINCT a.ID, a.EMAIL, a.FIRST_NAME, a.LAST_NAME
FROM DEVELOPERS a
         JOIN SKILLCODES b
              ON (a.SKILL_CODE & b.CODE) = b.CODE
WHERE b.CATEGORY = 'Front End'
ORDER BY a.ID ASC;