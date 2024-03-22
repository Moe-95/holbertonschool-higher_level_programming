-- List by best score
-- Execute: cat 10-top_score.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
USE hbtn_0c_0;
SELECT * FROM second_table ORDER BY score DESC;
