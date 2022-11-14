import mysql.connector

dbConfig = {
    'user': 'root',
    'password': 'qwop0526.',
    'host': '127.0.0.1',
    'port': 3306,
}

conn = mysql.connector.connect(**dbConfig)
print(conn)
conn.close()
