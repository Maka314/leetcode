SELECT
    MIN(survey_log) AS survey_log
FROM
    (SELECT
        ShowCount.question_id AS survey_log,
        AnswerCount.c / ShowCount.c AS Rate
    FROM
            (SELECT
                question_id,
                COUNT(*) AS c
            FROM
                SurveyLog
            WHERE
                action = 'show'
            GROUP BY
                question_id) AS ShowCount
        LEFT JOIN
            (SELECT
                question_id,
                COUNT(*) AS c
            FROM
                SurveyLog
            WHERE
                action = 'answer'
            GROUP BY
                question_id) AS AnswerCount
        ON ShowCount.question_id = AnswerCount.question_id) AS temp1
WHERE
    survey_log is not null
    and
    Rate = (SELECT
                MAX(AnswerCount.c / ShowCount.c)
            FROM
                    (SELECT
                        question_id,
                        COUNT(*) AS c
                    FROM
                        SurveyLog
                    WHERE
                        action = 'show'
                    GROUP BY
                        question_id) AS ShowCount
                LEFT JOIN
                    (SELECT
                        question_id,
                        COUNT(*) AS c
                    FROM
                        SurveyLog
                    WHERE
                        action = 'answer'
                    GROUP BY
                        question_id) AS AnswerCount
                ON ShowCount.question_id = AnswerCount.question_id)