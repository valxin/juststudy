from flask import Flask
from flask import render_template, request, session
from flask_mysqldb import MySQL
import MySQLdb.cursors
import os

# creates a Flask application
app = Flask(__name__, template_folder='static/template')

app.secret_key = 'will set secret key'

app.config['MYSQL_HOST'] = os.environ.get("DB_HOST", "localhost")
app.config['MYSQL_USER'] = os.environ.get("DB_USER", "root")
app.config['MYSQL_PASSWORD'] = os.environ.get("DB_PWD", "")
app.config['MYSQL_DB'] = 'mathcounts'
mysql = MySQL(app)


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/mathcounts")
def mathcounts():
    return render_template('mathcounts.html')


@app.route("/countdown", methods=['GET', 'POST'])
def countdown():
    level = 2
    year = 2022
    if request.method == 'POST':
        level = request.form['level']
        year = request.form['year']
        print("Level/year:  ", level, year)
        session['level'] = level
        session['year'] = year
    else:
        level = session['level']
        year = session['year']

    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute(
        "SELECT q.question, q.answers, IFNULL(i.url, '') AS imageUrl " +
        "FROM mathcounts.questions q " +
        "LEFT JOIN mathcounts.images i ON q.question_id = i.question_id " +
        "WHERE q.level_id = % s AND q.round_id = 4 AND q.year = % s ORDER BY RAND() LIMIT 1",
        (level, year,))
    records = cursor.fetchone()

    return render_template('countdown.html', question=records["question"], answers=records["answers"], imageUrl=records["imageUrl"])


@app.route("/api/sprint", methods=['POST'])
def sprint():
    level = 2
    year = 2022
    if request.method == 'POST':
        level = request.form['level']
        year = request.form['year']
        print("Level/year:  ", level, year)
        session['level'] = level
        session['year'] = year
    else:
        level = session['level']
        year = session['year']

    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute(
        "SELECT q.question, q.answers, IFNULL(i.url, '') AS imageUrl " +
        "FROM mathcounts.questions q " +
        "LEFT JOIN mathcounts.images i ON q.question_id = i.question_id " +
        "WHERE q.level_id = % s AND q.round_id = 1 AND q.year = % s",
        (level, year,))
    records = cursor.fetchall()
    print("question", len(records))
    return render_template('sprint_round.html', questions=records, total=len(records))


@app.route("/api/target", methods=['POST'])
def target():
    level = 2
    year = 2023
    if request.method == 'POST':
        level = request.form['level']
        year = request.form['year']
        print("Level/year:  ", level, year)
        session['level'] = level
        session['year'] = year
    else:
        level = session['level']
        year = session['year']

    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute(
        "SELECT q.question, q.answers, IFNULL(i.url, '') AS imageUrl " +
        "FROM mathcounts.questions q " +
        "LEFT JOIN mathcounts.images i ON q.question_id = i.question_id " +
        "WHERE q.level_id = % s AND q.round_id = 2 AND q.year = % s",
        (level, year,))
    records = cursor.fetchall()
    print("question", len(records))
    return render_template('target_round.html', questions=records, total=len(records))


@app.route("/api/contact", methods=['POST'])
def contact():
    name = request.form['name']
    email = request.form['email']
    subject = request.form['subject']
    message = request.form['message']

    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('INSERT INTO mathcounts.contact_message (name,email,subject,message) VALUES (% s, % s, % s, % s)',
                   (name, email, subject, message,))
    mysql.connection.commit()
    return render_template('contact.html')

# run the application
if __name__ == "__main__":
    app.run(debug=False)
