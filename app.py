from flask import Flask, session, flash, redirect, render_template, request, url_for
import database
import os
app = Flask(__name__)

@app.route('/', methods=["GET","POST"])
@app.route('/login', methods=["GET","POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        return render_template("login.html")
    return render_template("login.html")

@app.route('/signup', methods=["GET","POST"])
def signup():
    flash("hi")
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if not database.addUser(username,password):
            flash('Sorry, that username/password has already been taken')
            return render_template("signup.html")
        return render_template("login.html")
    return render_template("signup.html")
@app.route('/posts/private',methods=["GET","POST"])
def public():
    return render_template("public.html")
@app.route('/posts/public',methods=["GET","POST"])
def private():
    return render_template("private.html")
@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))    
app.secret_key = os.urandom(24)

if __name__ == '__main__':
    app.debug=True
    app.run()
