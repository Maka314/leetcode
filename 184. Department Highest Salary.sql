-- Can work but not will
SELECT Res.Department,
    Res.Employee,
    Res.Salary
FROM (
        SELECT d.name as Department,
            e.name as Employee,
            e.salary as Salary,
            (
                SELECT COUNT(*)
                FROM Employee e2
                WHERE e2.salary > e.salary
                    and e2.departmentId = e.departmentId
            ) AS Count
        FROM Employee e
            JOIN Department d ON e.departmentId = d.id
    ) AS Res
WHERE Res.Count = 0;