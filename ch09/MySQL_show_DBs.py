import mysql.connector
import GuiDBConfig as guiConf

GUIDB = 'GuiDB'

conn = mysql.connector.connect(**guiConf.dbConfig)
cursor = conn.cursor()

cursor.execute("USE guidb")
cursor.execute("CREATE TABLE Books (                        \
                Book_ID INT NOT NULL AUTO_INCREMENT,                    \
                Book_Title VARCHAR(25) NOT NULL,Book_Page INT NOT NULL, \
                PRIMARY KEY(Book_ID)                                    \
                ) ENGINE=InnoDB")

conn.close()
