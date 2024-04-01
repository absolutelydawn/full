CREATE TABLE HR.buytbl2 AS (SELECT * FROM HR.buytbl);

SELECT * FROM HR.buytbl2;

CREATE TABLE HR.buytbl3 AS (SELECT userid, prodname FROM hr.buytbl);

SELECT * FROM HR.buytbl3;

SELECT userid AS "사용자명", sum(amount) AS "총 구매량" FROM hr.buytbl GROUP BY userid;

SELECT userid AS "사용자명", sum(amount * PRICE) AS "총 구매액" FROM HR.BUYTBL GROUP BY USERID;

SELECT CAST(AVG(amount) AS number(5,3)) AS "평균 구매 수량" FROM HR.BUYTBL;

SELECT userid, CAST(AVG(amount) AS number(5,3)) AS "평균 구매 수량" FROM HR.BUYTBL;

SELECT userid AS "사용자명", sum(amount * PRICE) AS "총 구매액"
FROM HR.BUYTBL
GROUP BY USERID
HAVING SUM(PRICE * AMOUNT) > 1000;

SELECT userid AS "사용자명", sum(amount * PRICE) AS "총 구매액"
FROM HR.BUYTBL
GROUP BY USERID
HAVING SUM(PRICE * AMOUNT) > 1000
ORDER BY SUM(PRICE * AMOUNT);