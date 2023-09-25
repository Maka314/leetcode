SELECT A2.player_id,
    A2.device_id
FROM Activity A2,
    (
        SELECT A1.player_id,
            MIN(A1.event_date) as first_date
        FROM Activity A1
        GROUP BY A1.player_id
    ) AS f
WHERE A2.event_date = f.first_date
    AND A2.player_id = f.player_id