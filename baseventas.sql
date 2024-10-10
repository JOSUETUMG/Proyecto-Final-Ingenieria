create database Inventario_Ventas;

USE Inventario_Ventas;

CREATE TABLE Productos (
    Código INT PRIMARY KEY AUTO_INCREMENT,
    Nombre VARCHAR(100) NOT NULL,
    Existencia INT NOT NULL,
    Proveedor VARCHAR(100),
    Precio DECIMAL(10, 2) NOT NULL
);
 
 CREATE TABLE Clientes (
    Código INT PRIMARY KEY AUTO_INCREMENT,
    Nombre VARCHAR(100) NOT NULL,
    Apellido VARCHAR(100) NOT NULL,
    Direccion VARCHAR(255),
    Teléfono VARCHAR (12)
);

CREATE TABLE Ventas (
    Código INT PRIMARY KEY AUTO_INCREMENT,
    Código_Producto INT NOT NULL,
    Código_Cliente INT NOT NULL,
    Cantidad INT NOT NULL,
    Total DECIMAL(10, 2) NOT NULL,
    Fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (Código_Producto) REFERENCES Productos(Código),
    FOREIGN KEY (Código_Cliente) REFERENCES Clientes(Código)
);

CREATE TABLE detalle_ventas (
    Id INT PRIMARY KEY AUTO_INCREMENT,
    Código_Venta INT NOT NULL,
    Código_Producto INT NOT NULL,
    cantidad INT NOT NULL,
    subtotal DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (Código_Venta) REFERENCES Ventas(Código),
    FOREIGN KEY (Código_Producto) REFERENCES Productos(Código)
);