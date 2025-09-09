USE restaurant_db;

DELETE FROM menus
WHERE item_name = 'Salmon Nigiri';

DELETE FROM menus
WHERE restaurant_id = (
    SELECT id FROM restaurant WHERE name = 'Pasta Paradise'
);

DELETE FROM restaurant
WHERE name = 'Pasta Paradise';

SELECT * FROM menus;
SELECT * FROM restaurant;
