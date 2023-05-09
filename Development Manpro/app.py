from flask import Flask,render_template, request, redirect, url_for, session, flash, jsonify
from nltk.tokenize import sent_tokenize
from sklearn.feature_extraction.text import CountVectorizer
import hashlib
import numpy as np
from docx import Document
from flask_mysqldb import MySQL
from uuid import uuid4
import MySQLdb.cursors
import re
app = Flask(__name__, static_folder="D:/Kuliah/Manpro/static")

app.secret_key="hehehayoapa"

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'proyekmanpro'
app.config['MYSQL_DB'] = 'dbmanpro'
 
mysql = MySQL(app)

allowedExt={'docx', 'pdf', 'jpg'}
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in allowedExt
@app.route('/hello')
def hello():
    return 'Hello World'

@app.route('/form')
def form():
    return render_template('loginManpro.html')

@app.route('/contact')
def contact():
    return render_template('Contact.html')

@app.route('/aboutus')
def aboutus():
    return render_template('AboutUs.html')
 
@app.route('/signup', methods = ['GET','POST'])
def signup():
    if request.method == 'POST' and 'signup-username' in request.form and 'signup-email' in request.form and 'signup-password' in request.form:
        user_id = str(uuid4())
        username = request.form['signup-username']
        email = request.form['signup-email']
        password = request.form['signup-password']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute("SELECT * FROM user WHERE user_email = %s", (email,))
        account= cursor.fetchone()
        if account:
            flash('Account already exists')
        elif not re.match(r'[^@]+@[^@]+\.[^@]+',email):
            flash('Invalid email address')
        elif not re.match(r'^[a-zA-Z0-9]+$',username):
            flash('Username must contain only characters and numbers')
        elif not username or not password or not email:
            flash('Please fill out the form')
        else:
            cursor.execute("""INSERT INTO user VALUES(%s,%s,%s,%s)""",(user_id,username,email,password,))
            mysql.connection.commit()
            msg="You have successfully signed up"
        cursor.close()
        return render_template('loginManpro.html', msg=msg)
    return redirect('/form')
@app.route('/login', methods = ['GET','POST'])
def login():
    msg = ''
    if request.method == 'POST' and 'signin-email' in request.form and 'signin-password' in request.form:
        email = request.form['signin-email']
        password = request.form['signin-password']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute("SELECT * FROM user WHERE user_email = %s and user_pass = %s", (email, password,))
        account = cursor.fetchone()
        if account:
            session['loggedin'] = True
            session['user_id'] = account['user_id']
            session['user_name'] = account['user_name']
            flash('You have successfully logged in')
            redirect ('/form')
        else:
            error = "incorrect password/username"
            return render_template('loginManpro.html', error = error)
    return render_template('loginManpro.html',session=session, msg=msg)
@app.route('/test')
def test():
    return session.get('user_id', 'no user id')
@app.route('/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('user_id', None)
    session.pop('user_name', None)
    return(redirect('/form'))

@app.route('/upload', methods=['GET','POST'])
def upload_file():
    file = request.files['file']
    filename=file.filename
    docid=str(uuid4())
    if file and allowed_file(filename):
        docContent=file.read()
        if 'user_id' in session:
            cursor = mysql.connection.cursor()
            cursor.execute("INSERT INTO document (document_id, user_id, doc_name, doc_content)VALUES (%s, %s, %s, %s)", (docid, session['user_id'], file.filename, docContent, ))
            mysql.connection.commit()
            flash('File uploaded successfully')
        else:
            flash('Please login to upload file')
    else:
        return 'Invalid file type'
def jaccard_similarity(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    intersection = set1.intersection(set2)
    union = set1.union(set2)
    return len(intersection) / len(union)

@app.route('/jaccard_similarity', methods=['GET','POST'])
def calculate_jaccard_similarity():
    # file1 = request.files['tes.docx']
    # file2 = request.files['tes2.docx']
    document = Document('D:/MATERI KULIAH SUTAN/SEMESTER 6/MANPRO/tes.docx')
    document2 = Document('D:/MATERI KULIAH SUTAN/SEMESTER 6/MANPRO/tes2.docx')

    paragraf_docx = ""
    paragraf_docx2 = ""
    for paragraph in document.paragraphs:
        paragraf_docx += paragraph.text.lower()
   
    for paraf in document2.paragraphs:
        paragraf_docx2 += paraf.text.lower()

    arrTeks = []
    arrResHash = []
    for i in sent_tokenize(paragraf_docx):
        i = i.replace(" ", "")
        arrTeks.append(i)
        i = hashlib.sha256(i.encode())
        i = i.hexdigest()
        arrResHash.append(i)

    arrTeks2 = []
    arrResHash2 = []
    for i in sent_tokenize(paragraf_docx2):
        i = i.replace(" ", "")
        arrTeks2.append(i)
        i = hashlib.sha256(i.encode())
        i = i.hexdigest()
        arrResHash2.append(i)

    result_jaccard = jaccard_similarity(arrResHash, arrResHash2) * 100
    jaccard_dec = np.around(result_jaccard, decimals=4)
    # final_result = np.char.mod('%.4f%%', jaccard_dec)

    final_result = '{:.4f}%'.format(jaccard_dec)
    return jsonify({'result': final_result})
app.run(host='localhost', port=5000)


    
    