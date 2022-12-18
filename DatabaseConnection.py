import pyodbc as odbc

DRIVER_NAME = 'SQL SERVER'
SERVER_NAME = 'MOSALAH'
DATABASE_NAME = 'Northwind'

# uid=<username>;
# pwd=<password>;
connection_string = f"""
    DRIVER={{{DRIVER_NAME}}};
    SERVER={SERVER_NAME};
    DATABASE={DATABASE_NAME};
    Trust_Connection=yes;
"""

conn = odbc.connect(connection_string)
cursor = conn.cursor()
cursor.execute('SELECT * FROM Musteriler')
rows = cursor.fetchall()
for row in rows:
    print(row)
print(conn)

