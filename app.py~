from flask import Flask, flash, redirect, render_template, request, url_for
import database
app = Flask(__name__)

@app.route('/', methods=["GET","POST"])
@app.route('/login', methods=["GET","POST"])
def login():
    if request.method == "GET":
        return render_template("private.html")
    return render_template("login.html")

@app.route('/signup', methods=["GET","POST"])
def signup():
    flash("hi")
    if request.method == "GET":
        username1 = request.form["username"]
        password1 = request.form["password"]
        if (database.checkUsername(username1) and database.checkPassword(password1)):
            flash('Sorry, that username/password has already been taken')
            return render_template("signup.html")
        else:
            database.addUser(username1,password1)
        return render_template("login.html")
    flash("hi")
    return render_template("signup.html")
@app.route('/posts/private',methods=["GET","POST"])
def public():
    pass
@app.route('/posts/public',methods=["GET","POST"])
def private():
    pass
@app.route('/logout')
def logout():
    pass
    
if __name__ == '__main__':
    app.debug=True
    app.run()
