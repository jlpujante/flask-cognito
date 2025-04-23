from flask import Flask, redirect, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return redirect('/login')

@app.route("/login")
def login():
    return "login"

@app.route("/logout")
def logout():
    return "logout"

@app.route("/welcome")
def welcome():
    return render_template("welcome.html")

if __name__ == '__main__':  
   app.run(debug=True)