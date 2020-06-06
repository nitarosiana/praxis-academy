from flask import Flask
# from flask_sqlite_new import flask_sqlite_new
from flask_mysql_mariaDB import MariaDB

app = Flask(__name__)
# app.config.from_pyfile('the-config.cfg')
db = MariaDB(app)

@app.route('/')
def show_all():
    try:
        cur = db.connection.cursor()
        return "berhasil"
    except:
        return "gagal"

