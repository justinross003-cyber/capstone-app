
-- DROP TABLES if re-running (dev convenience)
DROP TABLE IF EXISTS Orders;
DROP TABLE IF EXISTS Customers;

CREATE TABLE Customers (
    CustomerId TEXT PRIMARY KEY,
    Name       TEXT NOT NULL,
    Email      TEXT NOT NULL UNIQUE,
    CreatedAt  TEXT NOT NULL
);

CREATE TABLE Orders (
    OrderId     TEXT PRIMARY KEY,
    CustomerId  TEXT NOT NULL,
    Total       REAL NOT NULL,
    CreatedAt   TEXT NOT NULL,
    FOREIGN KEY (CustomerId) REFERENCES Customers(CustomerId)
);
