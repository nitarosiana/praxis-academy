from flask import Flask
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from werkzeug.exceptions import NotFound

from appke1 import app as appke1
from appke2 import app as appke2
from appke3 import app as appke3

app = Flask(__name__)

app.wsgi_app = DispatcherMiddleware(NotFound(), {
    '/appke1': appke1,
    '/appke2': appke2,
    '/appke3': appke3
})


if __name__ == "__main__":
    app.run()