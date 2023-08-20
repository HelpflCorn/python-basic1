CREATE TABLE cool_table (
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER
);

INSERT INTO cool_table (name, AGE) VALUES
("Petro Mostavchuk", 35), ("Vasyl  Motyvator", 40);

SELECT name, age FROM cool_table

ALTER TABLE cool_table RENAME TO very_cool_table;

ALTER TABLE very_cool_table ADD COLUMN email TEXT;

UPDATE very_cool_table SET email = 'mostavchuk@motyvator_ukrainy.com' WHERE name = 'Petro Mostavchuk';

DELETE FROM very_cool_table WHERE name = "Vasyl Motyvator";

SELECT * FROM very_cool_table