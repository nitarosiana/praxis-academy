from mysql.connector import (connection)

cnx = connection.MySQLConnection(user='root', password='nita010799',
                                 host='localhost',
                                 database='kuliah')
cnx.close()

print(cnx)