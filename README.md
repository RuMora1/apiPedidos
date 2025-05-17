# apiPedidos

**A considerar:**

1. Hecho en Flask + SQL Server 2018
2. Debe ser montado en local.
3. El usuario debe usar el servidor "localhost" en SQL Server.
4. Nombre de la Base de Datos: DB_PEDIDOS
5. Nombre de la Tabla: pedidos
6. Usuario: sa
7. Contraseña: admin123
8. Python 3.10 o superior requerido
9. Se requiere el Driver ODBC 17 de SQL Server instalado.
10. URL por defecto: http://127.0.0.1:5001

-------------------------------------------------------------------
Se adjunta el Script SQL para la creación de la BDD y la tabla, 
además del BackUP de la BDD.

-------------------------------------------------------------------
Para instalar dependencias (dentro del directorio):

pip install -r requirements.txt

-------------------------------------------------------------------
El cambio de alguna credencial o parámetro también debe ser cambiado en el archivo **main.py**, en:

"app.config['SQLALCHEMY_DATABASE_URI'] = (
    'mssql+pyodbc://sa:admin123@localhost/DB_PEDIDOS?driver=ODBC+Driver+17+for+SQL+Server'
)"

-------------------------------------------------------------------
**Si hace las peticiones por medio de la página:**

GET: Solo necesita llenar el campo ID.

POST: Todos los campos **EXCEPTO EL ID** son requeridos.

PUT: Todos los campos son requeridos.

DELETE: Solo necesita llenar el campo ID.

-------------------------------------------------------------------
**Uso de métodos en Postman:**

GET: http://127.0.0.1:5001/pedidos --- Devuelve TODOS los pedidos.

GET: http://127.0.0.1:5001/pedidos/{id} --- Devuelve el pedido acuerdo al ID.

POST: http://127.0.0.1:5001/pedidos --- Crea un nuevo pedido

{
  "cliente": "Juan Perez",
  "categoria": "Herramientas",
  "marca": "Bosch",
  "producto": "Taladro",
  "cantidad": 2,
  "precio": 69990
}

PUT: http://127.0.0.1:5001/pedidos/{id} --- Actualiza un pedido de acuerdo al ID

{
  "cliente": "Juan Gonzalez",
  "categoria": "Electricidad",
  "marca": "Makita",
  "producto": "Esmeril",
  "cantidad": 1,
  "precio": 84990
}

DELETE: http://127.0.0.1:5001/pedidos/{id} --- Borra el pedido del ID seleccionado

-------------------------------------------------------------------

