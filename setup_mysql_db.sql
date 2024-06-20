-- prepares a MySQL server for the project

CREATE DATABASE IF NOT EXISTS Healixra;
CREATE USER IF NOT EXISTS 'Name'@'localhost' IDENTIFIED BY 'Password';
GRANT ALL PRIVILEGES ON `Healixra`.* TO 'Name'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'Name'@'localhost';
FLUSH PRIVILEGES;