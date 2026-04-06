CREATE DATABASE productDB;
GO

USE productDB;
GO

CREATE TABLE dbo.products (
    id INT PRIMARY KEY,
    title NVARCHAR(200),
    price DECIMAL(10,2),
    description NVARCHAR(MAX),
    category NVARCHAR(100),
    image NVARCHAR(MAX),
    rating INT
);