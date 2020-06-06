from flask import Flask

app = Flask(__name__)

@app.route("/")
def index_one():

    with app.app_context():
        string = 'connecting 3. . .'
        print(string)

    return "Aku ke 3"

if __name__ == "__main__":
    app.run()