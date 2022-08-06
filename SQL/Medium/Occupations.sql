```
Occupations
https://www.hackerrank.com/challenges/occupations/problem?isFullScreen=true
```


SELECT
    MAX(CASE WHEN OCCUPATION = 'Doctor' THEN NAME END) AS 'Doctor',
    MAX(CASE WHEN OCCUPATION = 'Professor' THEN NAME END) AS 'Professor',
    MAX(CASE WHEN OCCUPATION = 'Singer' THEN NAME END) AS 'Singer',
    MAX(CASE WHEN OCCUPATION = 'Actor' THEN NAME END) AS 'Actor'
FROM (SELECT *, ROW_NUMBER() OVER (PARTITION BY OCCUPATION ORDER BY NAME) RN
      FROM OCCUPATIONS) TEMP
GROUP BY RN;