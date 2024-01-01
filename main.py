from flask import Flask
from flask import render_template

# creates a Flask application
app = Flask(__name__, template_folder='static/template')

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/signup")
def signup():
    return render_template('signup.html')

@app.route("/countdown")
def countdown():
    return render_template('countdown.html')

# run the application
if __name__ == "__main__":
    app.run(debug=False)