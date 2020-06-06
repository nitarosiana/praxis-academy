from flask import Flask

app = Flask(__name__)

@app.route("/")
def index_one():

    with app.app_context():
        string = 'connecting 2. . .'
        print(string)

    return "Aku ke 2"

if __name__ == "__main__":
    app.run()