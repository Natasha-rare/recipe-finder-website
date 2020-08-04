from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template("main.html")

@app.route("/contacts")
def contacts():
    return render_template("contacts.html")

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')