DELETE p1
FROM Person p1,
    Person p2
WHERE p1.Email = p2.Email
    AND p1.Id > p2.id -- 要求原地修改，所以使用DELETE