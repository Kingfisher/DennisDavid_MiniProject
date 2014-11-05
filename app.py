from flask import Flask, session, flash, redirect, render_template, request, url_for
import database
import os
app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route('/', methods=["GET","POST"])
@app.route('/login', methods=["GET","POST"])
def login():
    error = None
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if not database.validateUser(username,password):
            flash('Unregistered username or incorrect password')
            return render_template("login.html")
        session['username'] = username
        return redirect(url_for('private'))
    return render_template("login.html")

@app.route('/signup', methods=["GET","POST"])
def signup():
    error = None
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if not database.addUser(username,password):
            flash("Unregistered username, too short username, or too short password.")
            return render_template("signup.html")
        flash("Great! You've registered! Now you can log in.")
        return redirect(url_for("login"))
    return render_template("signup.html")
@app.route('/posts/private',methods=["GET","POST"])
def public():
    return render_template("public.html")
@app.route('/posts/public',methods=["GET","POST"])
def private():
    if 'username' in session:
        return render_template("private.html")
    flash('You are not logged in')
    return redirect(url_for("login"))
@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))    

if __name__ == '__main__':
    app.debug=True
    app.run()
