-- # Write your MySQL query statement below
-- Answer V1
SELECT DISTINCT P1.email AS Email
FROM Person as P1
    CROSS JOIN Person as P2
WHERE P1.email = P2.email
    and P1.id != P2.id;
-- Answer v2
SELECT DISTINCT Person.email AS Email
FROM Person
    JOIN (
        SELECT id,
            count(email) AS num
        FROM Person
        GROUP BY email
    ) AS result ON Person.id = result.id
WHERE result.num > 1;