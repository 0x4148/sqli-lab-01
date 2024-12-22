CREATE DATABASE IF NOT EXISTS dummy_org;

USE dummy_org;

CREATE TABLE employees (
    id INT AUTO_INCREMENT PRIMARY KEY,
    firstname VARCHAR(50),
    lastname VARCHAR(50),
    phone VARCHAR(15),
    email VARCHAR(50)
);

CREATE TABLE system_users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50),
    password VARCHAR(32),
    email VARCHAR(50),
    role VARCHAR(20)
);

CREATE TABLE news (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(100),
    details TEXT,
    date DATE
);

INSERT INTO employees (firstname, lastname, phone, email) VALUES
('John', 'Doe', '123-456-7890', 'john.doe@example.com'),
('Jane', 'Doe', '234-567-8901', 'jane.doe@example.com'),
('Jim', 'Beam', '345-678-9012', 'jim.beam@example.com'),
('Jack', 'Daniels', '456-789-0123', 'jack.daniels@example.com'),
('Johnny', 'Walker', '567-890-1234', 'johnny.walker@example.com'),
('James', 'Bond', '678-901-2345', 'james.bond@example.com'),
('Bruce', 'Wayne', '789-012-3456', 'bruce.wayne@example.com'),
('Clark', 'Kent', '890-123-4567', 'clark.kent@example.com'),
('Peter', 'Parker', '901-234-5678', 'peter.parker@example.com'),
('Tony', 'Stark', '012-345-6789', 'tony.stark@example.com');

INSERT INTO system_users (username, password, email, role) VALUES
('admin', 'dummypassword', 'admin@example.com', 'admin'),
('johndoe', 'dummypassword', 'john.doe@example.com', 'user'),
('janedoe','dummypassword', 'jane.doe@example.com', 'user'),
('jimbeam', 'dummypassword', 'jim.beam@example.com', 'user'),
('jackdaniels', 'dummypassword', 'jack.daniels@example.com', 'user'),
('johnnywalker', 'dummypassword', 'johnny.walker@example.com', 'user'),
('jamesbond', 'dummypassword', 'james.bond@example.com', 'user'),
('brucewayne','dummypassword', 'bruce.wayne@example.com', 'user'),
('clarkkent', 'dummypassword', 'clark.kent@example.com', 'user'),
('peterparker', 'dummypassword', 'peter.parker@example.com', 'user');

INSERT INTO news (title, details, date) VALUES
('News 1', 'Details of news 1', '2024-01-01'),
('News 2', 'Details of news 2', '2024-02-01'),
('News 3', 'Details of news 3', '2024-03-01'),
('News 4', 'Details of news 4', '2024-04-01'),
('News 5', 'Details of news 5', '2024-05-01'),
('News 6', 'Details of news 6', '2024-06-01'),
('News 7', 'Details of news 7', '2024-07-01'),
('News 8', 'Details of news 8', '2024-08-01'),
('News 9', 'Details of news 9', '2024-09-01'),
('News 10', 'Details of news 10', '2024-10-01');

CREATE USER 'cyard_01'@'%' IDENTIFIED BY 'cyardP@ss';
CREATE USER 'cyard_01'@'localhost' IDENTIFIED BY 'cyardP@ss';
GRANT SELECT ON dummy_org.* TO 'cyard_01'@'%';
GRANT SELECT ON dummy_org.* TO 'cyard_01'@'localhost';
FLUSH PRIVILEGES;


CREATE DATABASE BooksLibrary;

USE BooksLibrary;


CREATE TABLE Books (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255),
    author VARCHAR(255),
    year INT,
    sales INT
);
INSERT INTO Books (title, author, year, sales) VALUES ('The Amazing Journey', 'John Smith', 2005, 1200);
INSERT INTO Books (title, author, year, sales) VALUES ('The Mysterious Quest', 'Jane Johnson', 2012, 4500);
INSERT INTO Books (title, author, year, sales) VALUES ('The Enchanted Saga', 'Robert Williams', 1998, 2300);
INSERT INTO Books (title, author, year, sales) VALUES ('The Fantastic Adventure', 'Emily Brown', 2020, 1500);
INSERT INTO Books (title, author, year, sales) VALUES ('The Incredible Mystery', 'Michael Jones', 2017, 3200);
INSERT INTO Books (title, author, year, sales) VALUES ('The Brilliant Chronicles', 'Sarah Garcia', 2001, 1800);
INSERT INTO Books (title, author, year, sales) VALUES ('The Fabulous Tale', 'David Miller', 2010, 3900);
INSERT INTO Books (title, author, year, sales) VALUES ('The Enchanted Quest', 'Laura Davis', 2019, 2900);
INSERT INTO Books (title, author, year, sales) VALUES ('The Amazing Saga', 'Chris Rodriguez', 2021, 1700);
INSERT INTO Books (title, author, year, sales) VALUES ('The Mysterious Journey', 'Anna Martinez', 2015, 4100);
-- Add the rest of the entries here
GRANT SELECT ON BooksLibrary.* TO 'cyard_01'@'%';
GRANT SELECT ON BooksLibrary.* TO 'cyard_01'@'localhost';
FLUSH PRIVILEGES;
