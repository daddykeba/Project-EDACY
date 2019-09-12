from flask import Flask, render_template, request, flash, url_for
from sqlalchemy.dialects import mysql
from werkzeug.utils import redirect
from wtforms import StringField, PasswordField, validators, Form
from flask_mysqldb import MySQL

app = Flask(__name__)

mysql = MySQL(app)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'daddy6189'
app.config['MYSQL_DB'] = 'flask'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

@app.route('/')
def index():
    nom = 'Keba'
    list = ["Alpha", "Fatou", "Adama"]
    return render_template('index.html', nom = nom, person=list)

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/edacy')
def edacy():
    return """<html><body><h2>Data Science</h2><p>Ceci est la page HTML de EDACY</p></body></html>"""

@app.route('/hello/<nom>')
def hello(nom):
    return ('Bienvenu {} dans le site de EDACY').format(nom)

class RegisterForm(Form):
    email = StringField('Email', validators=[
        validators.DataRequired('Email is required')])
    passwords = PasswordField('Password', validators=[
        validators.DataRequired('Password is required')])


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        email = form.email.data
        passwords = form.passwords.data

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO users(email,passwords) VALUES(%s, %s)", (email, passwords))

        mysql.connection.commit()

        cur.close()
        flash('Enregistrement réussi')
        return render_template('signup.html')
    return render_template('signup.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        passwords = request.form['passwords']
        app.logger.info('%s check email', email)

        cur = mysql.connection.cursor()
        result = cur.execute("SELECT * FROM users WHERE email = %s AND passwords = %s", [email, passwords])
        app.logger.info('%s check result', result)

        if result:
            #flash('Enregistrement réussi')
            return redirect(url_for('profile'))

        return render_template('index.html')
    return render_template('index.html')

if __name__ == '__main__':
    app.debug = True
    app.run()
