from flask import Flask, render_template, request, url_for
import mysql.connector as mariadb
from werkzeug.urls import url_parse
app = Flask(__name__)


@app.route("/")
def home():

    con = mariadb.connect(
        host="localhost",
        user="root",
        passwd="12345",
        database='kuliah'
    )