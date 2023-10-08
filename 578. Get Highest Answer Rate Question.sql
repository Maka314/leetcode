-- not a really good slution
SELECT
    *
FROM
    (
        SELECT
            MIN(survey_log) AS survey_log
        FROM
            (
                SELECT
                    ShowCount.question_id AS survey_log,
                    AnswerCount.c / ShowCount.c AS Rate
                FROM
                    (
                        SELECT
                            question_id,
                            COUNT(*) AS c
                        FROM
                            SurveyLog
                        WHERE
                            action = 'show'
                        GROUP BY
                            question_id
                    ) AS ShowCount
                    LEFT JOIN (
                        SELECT
                            question_id,
                            COUNT(*) AS c
                        FROM
                            SurveyLog
                        WHERE
                            action = 'answer'
                        GROUP BY
                            question_id
                    ) AS AnswerCount ON ShowCount.question_id = AnswerCount.question_id
            ) AS temp1
        WHERE
            Rate = (
                SELECT
                    MAX(AnswerCount.c / ShowCount.c)
                FROM
                    (
                        SELECT
                            question_id,
                            COUNT(*) AS c
                        FROM
                            SurveyLog
                        WHERE
                            action = 'show'
                        GROUP BY
                            question_id
                    ) AS ShowCount
                    LEFT JOIN (
                        SELECT
                            question_id,
                            COUNT(*) AS c
                        FROM
                            SurveyLog
                        WHERE
                            action = 'answer'
                        GROUP BY
                            question_id
                    ) AS AnswerCount ON ShowCount.question_id = AnswerCount.question_id
            )
    ) AS Res
WHERE
    survey_log IS NOT NULL;

-- batter slution with sort and limit
select
    AnswerCnt.question_id as survey_log
from
    (
        select
            question_id,
            count(*) as answer_cnt
        from
            survey_log
        where
            action = "answer"
        group by
            question_id
    ) as AnswerCnt
    join (
        select
            question_id,
            count(*) as action_cnt
        from
            survey_log
        where
            action = "show"
        group by
            question_id
    ) as ShowCnt on AnswerCnt.question_id = ShowCnt.question_id
order by
    AnswerCnt.answer_cnt / ShowCnt.action_cnt desc
limit
    1;