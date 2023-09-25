-- 错误代码
SELECT w1.id AS Id
FROM Weather w1
    JOIN Weather w2 ON w1.recordDate = w2.recordDate + 1
WHERE w1.temperature > w2.temperature;
-- 正确代码
-- 实际上Date函数和datediff函数存在一些本质上的区别
SELECT w1.id AS Id
FROM Weather w1,
    Weather w2
WHERE DATEDIFF(w1.recordDate, w2.recordDate) = 1
    and w1.temperature > w2.temperature;