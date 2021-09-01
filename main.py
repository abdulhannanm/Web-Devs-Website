from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'ffrn1234'
app.config['MYSQL_DB'] = 'webdevmembers'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql =  MySQL(app)

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        first = request.form['firstname']
        last = request.form['lastname']
        email = request.form["email"]
        cursor = mysql.connection.cursor()
        cursor.execute(''' INSERT INTO users(Firstname, Lastname, Email) Values(%s, %s, %s)''', (first, last, email))
        mysql.connection.commit()
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)


