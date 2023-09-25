-- 这是一个错误答案
SELECT A1.player_id,
    A1.event_date AS first_login,
    RankResult.HigherRank
FROM Activity A1,
    (
        SELECT A2.player_id,
            A2.event_date,
            COUNT(*) AS HigherRank
        FROM Activity A2,
            Activity A3
        WHERE A3.player_id = A2.player_id
            AND A3.event_date > A2.event_date
    ) AS RankResult
WHERE A1.player_id = RankResult.player_id
    and A1.event_date = RankResult.event_date
    and RankResult.HigherRank = 0;
-- 使用GROUP BY的正确答案
SELECT A.player_id,
    MIN(A.event_date) AS first_login
FROM Activity A
GROUP BY A.player_id;