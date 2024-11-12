
-- Create Database
CREATE DATABASE PharmacyDB;
USE PharmacyDB;

-- Table: MedicineCategory
CREATE TABLE MedicineCategory (
    CategoryID VARCHAR(5) PRIMARY KEY,
    CategoryName VARCHAR(50) NOT NULL,
    Description TEXT
);

-- Table: Supplier
CREATE TABLE Supplier (
    SupplierID VARCHAR(5) PRIMARY KEY,
    Name VARCHAR(100) NOT NULL,
    ContactInfo VARCHAR(20),
    Address VARCHAR(255),
    ProductsSupplied TEXT
);

-- Table: Medicine
CREATE TABLE Medicine (
    MedicineID VARCHAR(5) PRIMARY KEY,
    Name VARCHAR(100) NOT NULL,
    CategoryID VARCHAR(5),
    DosageForm VARCHAR(50),
    Strength VARCHAR(20),
    QuantityInStock INT,
    Price DECIMAL(10, 2),
    ExpiryDate DATE,
    FOREIGN KEY (CategoryID) REFERENCES MedicineCategory(CategoryID)
);

-- Table: Customer
CREATE TABLE Customer (
    CustomerID VARCHAR(5) PRIMARY KEY,
    Name VARCHAR(100) NOT NULL,
    ContactNumber VARCHAR(20),
    Address VARCHAR(255),
    DateOfBirth DATE
);

-- Table: Employee
CREATE TABLE Employee (
    EmployeeID VARCHAR(5) PRIMARY KEY,
    Name VARCHAR(100) NOT NULL,
    Position VARCHAR(50),
    ContactNumber VARCHAR(20),
    HireDate DATE,
    Salary DECIMAL(10, 2),
    DateOfBirth DATE
);

-- Table: Sales
CREATE TABLE Sales (
    SaleID VARCHAR(5) PRIMARY KEY,
    MedicineID VARCHAR(5),
    CustomerID VARCHAR(5),
    QuantitySold INT,
    SaleDate DATE,
    TotalPrice DECIMAL(10, 2),
    FOREIGN KEY (MedicineID) REFERENCES Medicine(MedicineID),
    FOREIGN KEY (CustomerID) REFERENCES Customer(CustomerID)
);

-- Table: Prescription
CREATE TABLE Prescription (
    PrescriptionID VARCHAR(5) PRIMARY KEY,
    CustomerID VARCHAR(5),
    DoctorName VARCHAR(100),
    PrescriptionDate DATE,
    Notes TEXT,
    FOREIGN KEY (CustomerID) REFERENCES Customer(CustomerID)
);

-- Table: SupplierMedicine
CREATE TABLE SupplierMedicine (
    SupplierMedicineID VARCHAR(5) PRIMARY KEY,
    SupplierID VARCHAR(5),
    MedicineID VARCHAR(5),
    SupplyPrice DECIMAL(10, 2),
    SupplyDate DATE,
    FOREIGN KEY (SupplierID) REFERENCES Supplier(SupplierID),
    FOREIGN KEY (MedicineID) REFERENCES Medicine(MedicineID)
);

-- Table: Inventory
CREATE TABLE Inventory (
    InventoryID VARCHAR(5) PRIMARY KEY,
    MedicineID VARCHAR(5),
    StockQuantity INT,
    LastUpdated DATE,
    FOREIGN KEY (MedicineID) REFERENCES Medicine(MedicineID)
);
