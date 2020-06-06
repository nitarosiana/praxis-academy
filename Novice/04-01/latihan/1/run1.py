from flask import Flask, render_template, request, url_for
app = Flask(__name__)

from flask.views import View

class ShowUsers(View):
    def dispatch_request(self):
        # users = User.query.all()
        return render_template('home.html', my_string="Hallo", content="Pluggable Views")

app.add_url_rule('/home/', view_func=ShowUsers.as_view('show_users'))

class ListView(View):

    def get_template_name(self):
        raise NotImplementedError()

    def render_template(self, context):
        return render_template(self.get_template_name(), **context)

    def dispatch_request(self):
        context = {'objects': self.get_objects()}
        return self.render_template(context)

class UserView(ListView):

    def get_template_name(self):
        return 'users.html'

    def get_objects(self):
        return User.query.all()

if __name__ == '__main__':
    app.run(debug=True)
