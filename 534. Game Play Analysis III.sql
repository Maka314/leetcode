SELECT A1.player_id,
    A1.event_date,
    SUM(A1.games_played) as games_played_so_far
FROM Activity A1
    inner join Activity A2 on A1.player_id = A2.player_id
    and A1.event_date <= A2.event_date
GROUP BY A2.player_id,
    A2.event_date;
SELECT *
FROM Activity A1
    inner join Activity A2 on A1.player_id = A2.player_id
    and A1.event_data <= A2.event_data
GROUP BY A2.player_id,
    A2.event_date;