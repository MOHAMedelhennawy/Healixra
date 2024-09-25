-- prepares a MySQL server for the project

CREATE DATABASE IF NOT EXISTS Healixra;
CREATE USER IF NOT EXISTS '{{username}}'@'localhost' IDENTIFIED BY '{{password}}';
GRANT ALL PRIVILEGES ON `Healixra`.* TO '{{username}}'@'localhost';
GRANT SELECT ON `performance_schema`.* TO '{{username}}'@'localhost';
FLUSH PRIVILEGES;