from flask import Flask,render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
from uuid import uuid4
import MySQLdb.cursors
import re
app = Flask(__name__)

app.secret_key="hehehayoapa"

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'proyekmanpro'
app.config['MYSQL_DB'] = 'dbmanpro'
 
mysql = MySQL(app)

@app.route('/hello')
def hello():
    return 'Hello World'

@app.route('/form')
def form():
    return render_template('loginManpro.html')
 
@app.route('/signup', methods = ['GET','POST'])
def signup():
    if request.method == 'POST' and 'signup-username' in request.form and 'signup-email' in request.form and 'signup-password' in request.form:
        user_id = str(uuid4())
        username = request.form['signup-username']
        email = request.form['signup-email']
        password = request.form['signup-password']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute("""INSERT INTO user VALUES(%s,%s,%s,%s)""",(user_id,username,email,password,))
        mysql.connection.commit()
        msg="You have successfully signed up"
        cursor.close()
        return render_template('loginManpro.html', msg=msg)
@app.route('/login', methods = ['GET','POST'])
def login():
    msg = ' '
    if request.method == 'POST' and 'signin-email' in request.form and 'signin-password' in request.form:
        email=request.form['signin-email']
        password=request.form['signin-password']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute("SELECT * FROM user WHERE user_email = %s and user_pass = %s",(email,password,))
        account = cursor.fetchone()
        if account:
            session['loggedin'] = True
            session['user_id'] = account['user_id']
            session['user_name'] = account['user_name']
            return 'Logged in successfully'
        else:
            msg = 'incorrect username/password'
        return render_template('loginManpro.html', msg=msg)
@app.route('/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('user_id', None)
    session.pop('user_name', None)
    return(redirect('/form'))
app.run(host='localhost', port=5000)