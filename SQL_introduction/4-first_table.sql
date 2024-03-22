-- create a table if not exist
-- Exceute: cat 4-first_table.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
USE hbtn_0c_0;
CREATE TABLE IF NOT EXISTS first_table (
    id INT,
    name VARCHAR(256)
);
