SELECT * FROM users;
INSERT INTO users (first_name, last_name) VALUES ("Jane", "Amsden"),("Emily" ,"Dixon"),("Theodore" ,"Dostoevsky"),("William" ,"Shapiro"),("Lao" ,"Xiu");

INSERT INTO books (title) VALUES ("C Sharp"), ("Java"), ("Python"),( "PHP"), ("Ruby");
SELECT * FROM books;
UPDATE books SET title = "C#" WHERE id=1;

UPDATE users SET first_name = "bill" WHERE id=4;

INSERT INTO favorites(user_id ,book_id) VALUES (1, 1) ,(1,2);

INSERT INTO favorites(user_id ,book_id) VALUES (2, 1) ,(2,2),(2,3);

INSERT INTO favorites(user_id ,book_id) VALUES (3, 1) ,(3,2),(3,3),(3,4);
INSERT INTO favorites(user_id ,book_id) VALUES (4, 1) ,(4,2),(4,3),(4,4),(4,5);


SELECT * FROM favorites;
SELECT users.* FROM favorites join users on favorites.user_id = users.id where favorites.book_id=3;

DELETE FROM favorites WHERE favorites.book_id=3 limit 1;

INSERT INTO favorites(user_id ,book_id) VALUES (5, 2);

select books.* From books join favorites on books.id = favorites.book_id where favorites.user_id=3;
SELECT users.* FROM users join favorites on favorites.user_id = users.id where favorites.book_id=5;
