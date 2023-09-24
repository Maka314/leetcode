-- 解法1
SELECT S.score,
    DENSE_RANK() OVER(
        ORDER BY S.score DESC
    ) AS 'rank'
FROM Scores AS S;
-- 解法2
SELECT S1.score,
    (
        SELECT COUNT(DISTINCT S2.score)
        FROM Scores S2
        WHERE S2.score >= S1.score
    ) AS 'rank'
FROM Scores S1
ORDER BY S1.score DESC;