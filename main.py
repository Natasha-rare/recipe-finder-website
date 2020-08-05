from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')  # main page
@app.route('/index')
def index():
    return render_template("main.html")


@app.route("/contacts")  # page contacts
def contacts():
    return render_template("contacts.html")


@app.route("/policy")  # page Privacy Policy
def policy():
    return render_template("privacyPolicy.html")


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')