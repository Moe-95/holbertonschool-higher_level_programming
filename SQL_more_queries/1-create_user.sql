-- Check if the user exists, drop if it does
DROP USER IF EXISTS 'user_0d_1'@'localhost';

-- Create the user with all privileges and set password
CREATE USER 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost' WITH GRANT OPTION;
