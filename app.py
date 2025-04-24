from flask import Flask, redirect, render_template, session
from flask_cognito_lib import CognitoAuth
from flask_cognito_lib.decorators import (
    auth_required,
    cognito_login,
    cognito_login_callback,
    cognito_logout,
    cognito_refresh_callback,
)
from utils import get_env_var

app = Flask(__name__)
app.secret_key = get_env_var('FLASK_APP_SECRET')

# Configuration required for CognitoAuth
app.config["AWS_REGION"] = get_env_var('AWS_REGION')
app.config["AWS_COGNITO_USER_POOL_ID"] = get_env_var('AWS_COGNITO_USER_POOL_ID')
app.config["AWS_COGNITO_DOMAIN"] = get_env_var('AWS_COGNITO_DOMAIN')
app.config["AWS_COGNITO_USER_POOL_CLIENT_ID"] = get_env_var('AWS_COGNITO_USER_POOL_CLIENT_ID')
app.config["AWS_COGNITO_USER_POOL_CLIENT_SECRET"] = get_env_var('AWS_COGNITO_USER_POOL_CLIENT_SECRET')
app.config["AWS_COGNITO_REDIRECT_URL"] = get_env_var('AWS_COGNITO_REDIRECT_URL')
app.config["AWS_COGNITO_LOGOUT_URL"] = get_env_var('AWS_COGNITO_LOGOUT_URL')
app.config["AWS_COGNITO_REFRESH_FLOW_ENABLED"] = get_env_var('AWS_COGNITO_REFRESH_FLOW_ENABLED')
app.config["AWS_COGNITO_REFRESH_COOKIE_ENCRYPTED"] = get_env_var('AWS_COGNITO_REFRESH_COOKIE_ENCRYPTED')
app.config["AWS_COGNITO_REFRESH_COOKIE_AGE_SECONDS"] = get_env_var('AWS_COGNITO_REFRESH_COOKIE_AGE_SECONDS')

auth = CognitoAuth(app)

@app.route("/")
def home():
    return redirect('/login')

@app.route("/login")
@cognito_login
def login():
    pass

@app.route("/postlogin")
@cognito_login_callback
def postlogin():
    return redirect('/welcome')

@app.route("/refresh", methods=["POST"])
@cognito_refresh_callback
def refresh():
    pass

@app.route("/logout")
@cognito_logout
def logout():
    pass

@app.route("/postlogout")
def postlogout():
    return redirect('/')

@app.route("/welcome")
@auth_required()
def welcome():
    return render_template("welcome.html", userdata=session['user_info'])

if __name__ == '__main__':  
   app.run(debug=get_env_var('DEBUG'))