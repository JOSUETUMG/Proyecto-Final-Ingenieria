import sqlite3

#ConexiOn a la base de datos
conn = sqlite3.connect('ventas.db')
c = conn.cursor()

#Crear tabla de productos
c.execute('''CREATE TABLE IF NOT EXISTS productos
             (codigo INTEGER PRIMARY KEY, nombre TEXT, existencia INTEGER, proveedor TEXT, precio REAL)''')

#Crear tabla de clientes
c.execute('''CREATE TABLE IF NOT EXISTS clientes
             (codigo INTEGER PRIMARY KEY, nombre TEXT, direccion TEXT)''')

#Crear tabla de ventas
c.execute('''CREATE TABLE IF NOT EXISTS ventas
             (codigo_producto INTEGER, codigo_cliente INTEGER, cantidad INTEGER, total REAL, cliente TEXT, fecha TEXT, producto TEXT)''')

conn.commit()

#Funcion para agregar producto a la base de datos
def agregar_producto_bd(codigo, nombre, existencia, proveedor, precio):
    c.execute("INSERT INTO productos VALUES (?, ?, ?, ?, ?)", (codigo, nombre, existencia, proveedor, precio))
    conn.commit()

#Funcion para listar productos desde la base de datos
def listar_productos_bd():
    c.execute("SELECT * FROM productos")
    return c.fetchall()

#Funcion para actualizar producto en la base de datos
def actualizar_producto_bd(codigo, nombre, existencia, proveedor, precio):
    c.execute("UPDATE productos SET nombre=?, existencia=?, proveedor=?, precio=? WHERE codigo=?", (nombre, existencia, proveedor, precio, codigo))
    conn.commit()

#Funcion para eliminar producto de la base de datos
def eliminar_producto_bd(codigo):
    c.execute("DELETE FROM productos WHERE codigo=?", (codigo,))
    conn.commit()

#Funcion para agregar cliente a la base de datos
def agregar_cliente_bd(codigo, nombre, direccion):
    c.execute("INSERT INTO clientes VALUES (?, ?, ?)", (codigo, nombre, direccion))
    conn.commit()

#Funcion para listar clientes desde la base de datos
def listar_clientes_bd():
    c.execute("SELECT * FROM clientes")
    return c.fetchall()

#Funcion para actualizar cliente en la base de datos
def actualizar_cliente_bd(codigo, nombre, direccion):
    c.execute("UPDATE clientes SET nombre=?, direccion=? WHERE codigo=?", (nombre, direccion, codigo))
    conn.commit()

#Funcion para eliminar cliente de la base de datos
def eliminar_cliente_bd(codigo):
    c.execute("DELETE FROM clientes WHERE codigo=?", (codigo,))
    conn.commit()

#Funcion para agregar venta a la base de datos
def agregar_venta_bd(codigo_producto, codigo_cliente, cantidad, total, cliente, fecha, producto):
    c.execute("INSERT INTO ventas VALUES (?, ?, ?, ?, ?, ?, ?)", (codigo_producto, codigo_cliente, cantidad, total, cliente, fecha, producto))
    conn.commit()

#Funcion para listar ventas desde la base de datos
def listar_ventas_bd():
    c.execute("SELECT fecha, producto, codigo_producto, cantidad, cliente, codigo_cliente, total FROM ventas")
    return c.fetchall()

#Funcion para anular venta en la base de datos
def anular_venta_bd(codigo_producto, codigo_cliente):
    c.execute("DELETE FROM ventas WHERE codigo_producto=? AND codigo_cliente=?", (codigo_producto, codigo_cliente))
    conn.commit()

#Funcion para obtener producto por código
def obtener_producto_por_codigo(codigo):
    c.execute("SELECT * FROM productos WHERE codigo=?", (codigo,))
    return c.fetchone()

#Funcion para obtener producto por nombre
def obtener_producto_por_nombre(nombre):
    c.execute("SELECT * FROM productos WHERE nombre=?", (nombre,))
    return c.fetchone()

#Funcion para obtener cliente por código
def obtener_cliente_por_codigo(codigo):
    c.execute("SELECT * FROM clientes WHERE codigo=?", (codigo,))
    return c.fetchone()

#Funcion para obtener cliente por nombre
def obtener_cliente_por_nombre(nombre):
    c.execute("SELECT * FROM clientes WHERE nombre=?", (nombre,))
    return c.fetchone()

#Funcion para actualizar existencia de producto
def actualizar_existencia_producto(codigo, nueva_existencia):
    c.execute("UPDATE productos SET existencia=? WHERE codigo=?", (nueva_existencia, codigo))
    conn.commit()

#Funcion para listar reportes desde la base de datos
def listar_reportes_bd():
    c.execute("SELECT fecha, cliente, total FROM ventas")
    return c.fetchall()

#Funcion para listar ventas por cliente desde la base de datos
def listar_ventas_por_cliente_bd(cliente):
    c.execute("SELECT fecha, codigo_cliente, cliente, total FROM ventas WHERE cliente LIKE ?", ('%' + cliente + '%',))
    return c.fetchall()

#Funcion para listar ventas por producto desde la base de datos
def listar_ventas_por_producto_bd(producto):
    c.execute("SELECT fecha, codigo_producto, producto, cantidad, total FROM ventas WHERE producto LIKE ?", ('%' + producto + '%',))
    return c.fetchall()








