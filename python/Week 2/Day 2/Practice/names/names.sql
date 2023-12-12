SET SQL_SAFE_UPDATES = 0;
SELECT * FROM names.names;
INSERT INTO names (name) VALUES ("Khaled Hannachi");
INSERT INTO names (name) VALUES ("Yamna Jouili"),("Amen Allah");
UPDATE names
SET name = "walid Hannachi"
WHERE id=2;
DELETE FROM names WHERE id=3;
DELETE FROM names
WHERE name IN ("Yamna Jouili");
DELETE FROM names
WHERE name BETWEEN ("Ahmed Hannachi") AND ("Amen Allah");