from flask import Flask, request, redirect
import os
import cgi

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!doctype html>
<html>
    <body>
    <form method="post">
        <label>User Name:
            <input type="text" name="user-name" />
        </label>
            <br>
        <label>Password:
            <input type="password" name="password" />
        </label>
            <br>
        <label> Verify Password:
            <input type="password" name="vpass" />
        </label>
            <br>
        <label>Email:
            <input type="email" name="email" />
        </label>
            <input type="submit" name="submit" value="Sign Up" />
    </form>
    </body>
</html>
"""

@app.route("/")
def index():
    return form.format('')

@app.route("/", methods=['POST'])
def user_signup():
    user = request.form['user-name']
    password = request.form['password']
    passv = request.form['vpass']
    email = request.form['email']
    name_err = ''
    password_err = ''
    passv_err = ''
    email_err = ''

    if len(user) > 15 or len(user) < 3:
        return 'Your user name does not fit the parameters'
        user = ''
    
    if len(password) > 15 or len(password) < 3:
        return 'Your password does not fit the parameters'
        password = ''

    if len(passv) > 15 or len(passv) < 3:
        return 'Your verification does not fit the parameters'
        passv = ''
    if password != passv:
        return 'Your password and verification do not match'

    else:
        return 'Welcome,' + user


app.run()