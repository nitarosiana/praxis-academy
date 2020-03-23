import mysql.connector

cnx = mysql.connector.connect(user='root', password='nita010799',
                              host='localhost',
                              database='kuliah')
cnx.close()

print(cnx)