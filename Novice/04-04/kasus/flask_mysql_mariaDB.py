import mysql.connector
from flask import current_app, _app_ctx_stack


class MariaDB(object):
    def __init__(self, app=None):
        self.app = app
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        app.config.setdefault('MYSQL_DATABASE', ':memory:')
        app.teardown_appcontext(self.teardown)

    def connect(self):
        return mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="123")

    def teardown(self, exception):
        ctx = _app_ctx_stack.top
        if hasattr(ctx, 'mysql_db'):
            ctx.mysql_db.close()

    @property
    def connection(self):
        ctx = _app_ctx_stack.top
        if ctx is not None:
            if not hasattr(ctx, 'mysql_db'):
                ctx.mysql_db = self.connect()
            return ctx.mysql_db