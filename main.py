from flask import Flask, render_template, request, session, redirect, url_for
from flask_mysqldb import MySQL
from datetime import timedelta

app = Flask(__name__)
app.secret_key = "WEB DEV'S CLUB"
app.permanent_session_lifetime = timedelta(days=5)



app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'ffrn1234'
app.config['MYSQL_DB'] = 'webdevmembers'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql =  MySQL(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template("about.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        if 'registered' in session:
            print("you've been redirected")
            return redirect(url_for('home'))
        else:
            first = request.form['firstname']
            last = request.form['lastname']
            email = request.form["email"]
            cursor = mysql.connection.cursor()
            cursor.execute(''' INSERT INTO users(Firstname, Lastname, Email) Values(%s, %s, %s)''', (first, last, email))
            mysql.connection.commit()
            session['registered'] = True
            print('in session')
            return redirect(url_for('home'))
    return render_template("register.html")

@app.route("/logout")
def logout():
    session.pop('registered', None)
    print("logged out from session")
    return redirect(url_for("home"))


if __name__ == '__main__':
    app.run(debug=True)