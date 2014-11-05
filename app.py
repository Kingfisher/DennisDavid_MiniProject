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
        if (validate(username,password) == False):
            error = 'Unregistered username or incorrect password'
        flash("You've logged in successfully")
        return render_template("private.html")
    return render_template("login.html")

@app.route('/signup', methods=["GET","POST"])
def signup():
    error = None
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if not database.addUser(username,password):
            flash("Registered username, too short username, or too short password.")
        if (database.addUser(username,password) == False):
            error = 'Unregistered username, too short username, or too short password'
            return render_template("signup.html")
        flash("Great! You've registered! Now you can log in.")
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

if __name__ == '__main__':
    app.debug=True
    app.run()
