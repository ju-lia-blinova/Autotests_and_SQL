Работа с базой данных
Задание 1

SELECT login, COUNT(o."inDelivery") 
FROM "Couriers" AS c INNER JOIN "Orders" AS o ON c.id = o."courierId" 
WHERE o."inDelivery" IS true 
GROUP BY login;


Задание 2

SELECT track, 
    CASE 
        WHEN finished = true THEN 2 
        WHEN cancelled = true THEN -1 
        WHEN "inDelivery" = true THEN 1 
    END 
FROM "Orders";
