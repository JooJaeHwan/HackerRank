```
The PADS
https://www.hackerrank.com/challenges/the-pads/problem?isFullScreen=true
```

SELECT CONCAT(O.NAME, '(',SUBSTR(O.Occupation,1,1),')') 
FROM OCCUPATIONS O
ORDER BY O.NAME;

SELECT CONCAT('There are a total of ', COUNT(O.Occupation), ' ', LOWER(O.Occupation),'s.')
FROM OCCUPATIONS O
GROUP BY O.Occupation
ORDER BY COUNT(O.Occupation), O.Occupation;