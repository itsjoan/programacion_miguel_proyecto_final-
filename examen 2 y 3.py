import mysql.connector
import pandas as pd

def conexion():
    return mysql.connector.connect(
    user= "root",
    password= "123456",
    host= "localhost",
    database = "ventass.csv",
    port = "3306")
def crear_tablas():
    conn = conexion()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE ventas_nuevas1 (
            id INT AUTO_INCREMENT PRIMARY KEY,
            fecha DATE,
            coche VARCHAR(255),
            precio DECIMAL(10, 2),
            vendedor VARCHAR(255),
            vendido VARCHAR(255)
        )
    ''')
    conn.commit()
    cursor.close()
    conn.close()
def introducir_datos_tabla(datos):
    conn = conexion()
    cursor = conn.cursor()

    for ventas in datos:
        cursor.execute('''
        INSERT INTO ventas_nuevas (fecha, coche, precio, marca, vendedor, vendido)
        VALUES (%s,%s,%s,%s,%s,%s)
        ''',(ventas['fecha'], ventas['coche'], ventas['precio'], ventas['marca'], ventas['vendedor'], ventas['vendido'])
        )
    conn.commit()
    cursor.execute()
    conn.close()
def tabla_new():
    crear_tablas()
    datos_venta=[
        {'fecha': '2023-01-15', 'coche': 'Toyota Corolla', 'precio': 25000.00, 'vendedor': 'Juan Pérez',
         'vendido': 'Sí'},
        {'fecha': '2023-02-20', 'coche': 'Honda Civic', 'precio': 22000.00, 'vendedor': 'María García',
         'vendido': 'Sí'},
        {'fecha': '2023-03-10', 'coche': 'Ford Mustang', 'precio': 35000.00, 'vendedor': 'Pedro López',
         'vendido': 'Sí'},
        {'fecha': '2023-04-05', 'coche': 'Chevrolet Camaro', 'precio': 40000.00, 'vendedor': 'Ana Martínez',
         'vendido': 'Sí'},
        {'fecha': '2023-05-12', 'coche': 'Nissan Altima', 'precio': 27000.00, 'vendedor': 'Luis Rodríguez',
         'vendido': 'Sí'},
        {'fecha': '2023-06-18', 'coche': 'Volkswagen Golf', 'precio': 20000.00, 'vendedor': 'Laura Sánchez',
         'vendido': 'Sí'},
        {'fecha': '2023-07-22', 'coche': 'BMW 3 Series', 'precio': 45000.00, 'vendedor': 'Carlos Gómez',
         'vendido': 'Sí'},
        {'fecha': '2023-08-30', 'coche': 'Mercedes-Benz C-Class', 'precio': 48000.00, 'vendedor': 'Sofía Díaz',
         'vendido': 'Sí'},
        {'fecha': '2023-09-14', 'coche': 'Audi A4', 'precio': 42000.00, 'vendedor': 'Elena Ruiz', 'vendido': 'Sí'},
        {'fecha': '2023-10-25', 'coche': 'Subaru Outback', 'precio': 32000.00, 'vendedor': 'Pablo Fernández',
         'vendido': 'Sí'}
    ]
    introducir_datos_tabla(datos_venta)

if __name__ =="__main__":
    introducir_datos_tabla()