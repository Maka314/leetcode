SELECT
    name
FROM
    (SELECT
        # candidateId,
        COUNT(*) AS VoteCount,
        Candidate.name
    FROM
        Vote JOIN
            Candidate ON candidateId = Candidate.id
    GROUP BY
        candidateId) AS VoteRes2
WHERE
    VoteCount = (SELECT
                    MAX(VoteCount)
                FROM
                    (SELECT
                        # candidateId,
                        COUNT(*) AS VoteCount,
                        Candidate.name
                    FROM
                        Vote JOIN
                            Candidate ON candidateId = Candidate.id
                    GROUP BY
                        candidateId) AS VoteRes)