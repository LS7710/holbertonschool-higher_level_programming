-- Create the MySQL server user user_0d_1 with all privileges

-- Check if the user already exists and create if not
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';

-- Check if the user already has all privileges and grant if not
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost' WITH GRANT OPTION;

-- Apply changes
FLUSH PRIVILEGES;
