import mysql.connector
import GuiDBConfig as guiConf


class MySQL():
    GUIDB = "GuiDB"

    def connect(self):
        conn = mysql.connector.connect(**guiConf.dbConfig)
        cursor = conn.cursor()
        return conn, cursor

    def close(self, cursor, conn):
        cursor.close()
        conn.close()

    def showDBs(self):
        conn, cursor = self.connect()

        cursor.execute("SHOW DATABASES")
        print(cursor)
        print(cursor.fetchall())

        self.close(cursor, conn)

    def createGuiDB(self):
        conn, cursor = self.connect()

        try:
            cursor.execute(
                "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(MySQL.GUIDB))
        except mysql.connector.Error as err:
            print("Failed to create DB: {}".format(err))

        self.close(cursor, conn)

    def useGuiDB(self, cursor):
        cursor.execute("USE guidb")

    def createTables(self):
        conn, cursor = self.connect()

        self.useGuiDB(cursor)

        cursor.execute("CREATE TABLE Books (                        \
                        Book_ID INT NOT NULL AUTO_INCREMENT,                    \
                        Book_Title VARCHAR(25) NOT NULL,Book_Page INT NOT NULL, \
                        PRIMARY KEY(Book_ID)                                    \
                        ) ENGINE=InnoDB")

        cursor.execute("CREATE TABLE Quotations(        \
                        Quote_ID INT AUTO_INCREMENT,    \
                        Quotation VARCHAR(250),         \
                        Books_Book_ID INT,              \
                        PRIMARY KEY (Quote_ID),         \
                        FOREIGN KEY (Books_Book_ID)     \
                            REFERENCES Books(Book_ID)   \
                            ON DELETE CASCADE           \
                       ) ENGINE=innoDB")

        self.close(cursor, conn)

    def dropTables(self):
        conn, cursor = self.connect()

        self.useGuiDB(cursor)

        cursor.execute("DROP TABLES FROM guidb")
        print(cursor.fetchall())

        self.close(cursor, conn)

    def showTables(self):
        conn, cursor = self.connect()

        cursor.execute("SHOW TABLES FROM guidb")
        print(cursor.fetchall())

        self.close(cursor, conn)

    def insertBooks(self, title, page, bookQuote):
        conn, cursor = self.connect()

        self.useGuiDB(cursor)

        cursor.execute("INSERT INTO books (Book_Title, Book_Page) VALUES (%s, %s)", (title, page))

        keyID = cursor.lastrowid

        cursor.execute("INSERT INTO quotations (Quotation, Books_Book_ID) VALUES (%s, %s)",
                       (bookQuote, keyID))

        conn.commit()

        self.close(cursor, conn)

    def insertBooksExample(self):
        conn, cursor = self.connect()

        self.useGuiDB(cursor)

        cursor.execute("INSERT INTO books (Book_Title, Book_Page) VALUES ('Design Patterns', 17)")

        keyID = cursor.lastrowid

        cursor.execute("INSERT INTO quotations (Quotation, Books_Book_ID) VALUES (%s, %s)",
                       ("Programming to an Interface, not an Implementation", keyID))

        conn.commit()

        self.close(cursor, conn)

    def showBooks(self):
        conn, cursor = self.connect()

        self.useGuiDB(cursor)

        cursor.execute("SELECT * FROM Books")
        allBooks = cursor.fetchall()
        print(allBooks)

        self.close(cursor, conn)

        return allBooks

    def showColumns(self):
        conn, cursor = self.connect()

        self.useGuiDB(cursor)

        cursor.execute("SHOW COLUMNS FROM quotations")
        print(cursor.fetchall())

        print('\n Pretty Print:\n------------')
        from pprint import pprint

        cursor.execute("SHOW COLUMNS FROM quotations")
        pprint(cursor.fetchall())

        self.close(cursor,conn)

    def showData(self):
        conn, cursor = self.connect()

        self.useGuiDB(cursor)

        cursor.execute("SELECT * FROM books")
        print(cursor.fetchall())

        cursor.execute("SELECT * FROM quotations")
        print(cursor.fetchall())

        self.close(cursor, conn)


if __name__ == '__main__':
    mySQL = MySQL()

    mySQL.showBooks()
#     try:
#         mySQL.createTables()
#         mySQL.showTables()
#
#         mySQL.showBooks()
#
#         mySQL.showColumns()
#
#         mySQL.insertBooksExample()
#
#         mySQL.insertBooks('Design Patterns', 7, 'Programming to an Interface, not an implementation')
#         mySQL.insertBooks('xUnit Test Patterns', 31, 'Programming to an Interface, not an implementation')
#         mySQL.showData()
#
#     except Exception as ex:
#         print(ex)