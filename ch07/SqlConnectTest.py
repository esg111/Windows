import mysql.connector

conn = mysql.connector.connect(user='root', password='qwop0526.',
                               host='127.0.0.1')
print(conn)
conn.close()