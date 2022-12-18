
import PlantDBConfig as plantDBConf
import mysql.connector


class MySQL():
    PlantDB = "PlantDB_2018218046"

    def connect(self):
        conn = mysql.connector.connect(**plantDBConf.dbConfig)
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

    def createPlantDB(self):
        conn, cursor = self.connect()

        try:
            cursor.execute(
                "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(MySQL.PlantDB))
        except mysql.connector.Error as err:
            print("Failed to create DB: {}".format(err))

        self.close(cursor, conn)

    def usePlantDB(self, cursor):
        cursor.execute("USE PlantDB_2018218046")

    def createTables(self):
        conn, cursor = self.connect()

        self.usePlantDB(cursor)

        cursor.execute("CREATE TABLE Plants (                       \
                        Plant_ID INT NOT NULL AUTO_INCREMENT,       \
                        Date VARCHAR(25) NOT NULL,                  \
                        Time VARCHAR(20) NOT NULL,                          \
                        Recorder VARCHAR(10) NOT NULL,              \
                        Location INT NOT NULL,                      \
                        Seed_count INT NOT NULL,                    \
                        Seed_name VARCHAR(10) NOT NULL,             \
                        PRIMARY KEY(Plant_ID)                       \
                        ) ENGINE=InnoDB")

        cursor.execute("CREATE TABLE PlantMemo(                 \
                        PlantMemo_ID INT AUTO_INCREMENT,        \
                        Plants_Plant_ID INT,                    \
                        Humidity INT,                           \
                        Illuminance INT,                        \
                        Temperature INT,                        \
                        Defect INT,                             \
                        Tree_count INT,                         \
                        Flower_count INT,                       \
                        Fruit_count INT,                        \
                        Min_H INT,                              \
                        Max_H INT,                              \
                        Avg_H INT,                              \
                        Memo VARCHAR(50),                       \
                        PRIMARY KEY (PlantMemo_ID),             \
                        FOREIGN KEY (Plants_Plant_ID)           \
                            REFERENCES Plants(Plant_ID)         \
                            ON DELETE CASCADE                   \
                        ) ENGINE=innoDB")

        self.close(cursor, conn)

    def dropTables(self):
        conn, cursor = self.connect()

        self.usePlantDB(cursor)

        cursor.execute("DROP TABLES FROM PlantDB")
        print(cursor.fetchall())

        self.close(cursor, conn)

    def insertPlants(self, date, time, recorder, location, seed_count, seed_name,
                     Humidity, Illuminance, Temperature, Defect,
                     Tree_count, Flower_count, Fruit_count, Min_H, Max_H, Avg_H, Memo):
        conn, cursor = self.connect()

        self.usePlantDB(cursor)

        cursor.execute("INSERT INTO Plants (Date, Time, Recorder, Location, Seed_count, Seed_name)\
                        VALUES (%s, %s, %s, %s, %s, %s)",
                       (date, time, recorder, location, seed_count, seed_name))

        keyID = cursor.lastrowid

        cursor.execute("INSERT INTO PlantMemo (Plants_Plant_ID, Humidity, Illuminance, Temperature, Defect, Tree_count, Flower_count, Fruit_count, Min_H, Max_H, Avg_H, Memo) \
                       VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                       (keyID, Humidity, Illuminance, Temperature, Defect, Tree_count, Flower_count, Fruit_count, Min_H,
                       Max_H, Avg_H, Memo))

        conn.commit()

        self.close(cursor, conn)

    def delete(self, index):
        conn, cursor = self.connect()

        self.usePlantDB(cursor)
        cursor.execute("DELETE FROM Plants WHERE Plant_ID=%s", (index,))
        conn.commit()

        self.close(cursor, conn)

    def countRow(self):
        conn, cursor = self.connect()

        self.usePlantDB(cursor)

        cursor.execute("SELECT COUNT(*) FROM Plants")
        cnt = cursor.fetchall()
        return cnt[0]

        self.close(cursor, conn)

    def select(self, select, index):
        conn, cursor = self.connect()

        self.usePlantDB(cursor)
        sql = "SELECT {} FROM Plants WHERE Plant_ID=%s".format(select)
        cursor.execute(sql, (index,))
        sel = cursor.fetchall()
        return sel[0][0]

        self.close(cursor, conn)

    def selectPM(self, select, index):
        conn, cursor = self.connect()

        self.usePlantDB(cursor)
        sql = "SELECT {} FROM PlantMemo WHERE Plants_Plant_ID=%s".format(select)
        cursor.execute(sql, (index,))
        sel = cursor.fetchall()
        return sel[0][0]

        self.close(cursor, conn)

    def list(self):
        conn, cursor = self.connect()

        self.usePlantDB(cursor)

        cursor.execute("SELECT * FROM Plants")
        list = cursor.fetchall()
        return list

        self.close(cursor, conn)

    def selectT(self, index, select):
        conn, cursor = self.connect()

        self.usePlantDB(cursor)

        cursor.execute("SELECT * FROM Plants WHERE Plant_ID=%s", index)
        sel = cursor.fetchall()
        return sel[0][select-1]

        self.close(cursor, conn)

    def maxID(self):
        conn, cursor = self.connect()

        self.usePlantDB(cursor)

        cursor.execute("SELECT MAX(Plant_ID) FROM Plants")
        result = cursor.fetchall()
        return result[0][0]

        self.close(cursor, conn)

if __name__ == '__main__':
    mySQL = MySQL()
    print(mySQL.list()[mySQL.countRow()[0]-1][0])
