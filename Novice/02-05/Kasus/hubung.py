
import mysql.connector


db = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="12345"
)

cursor = db.cursor()
cursor.execute("CREATE DATABASE if not exists rental")

sql = """use rental"""
cursor.execute(sql)
if db.is_connected():
    print("Berhasil terhubung")

