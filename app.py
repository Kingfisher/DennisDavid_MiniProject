from flask import Flask, render_template, request, redirect, session
import qcheck
import text

app=Flask(__name__)

@app.route("/",methods=["GET","POST"])
def index():
    return render_template("home.html", error_message=error_message)
    
@app.route("/a1")
def a1():
    #print l1
    return redirect(l1)
    

if __name__=="__main__":
    app.debug = True
    app.run()
