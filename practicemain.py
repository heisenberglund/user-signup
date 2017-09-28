from flask import Flask, request, redirect
import os
import cgi

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!doctype html>
<html>
    <head>
        <style>
            .error {{
                color: red;
            }}
        </style>
    </head>

    <body>
        <h1>User Signup</h1>
    <form method="post">
        <table>
            <tbody>
                <tr>
                    <td>
                        <label for "user-name">User Name:</label>
                    </td>
                    <td>
                        <input type="text" name="user-name" />
                        <span class="error">{name_err}</span>
                    </td>
                </tr>
                <tr>
                    <td>
                        <label>Password:</label>
                    </td>
                    <td>
                        <input type="password" name="password" />
                        <span class="error">{password_err}</span>
                    </td>
                </tr>
                <tr>
                    <td>
                        <label> Verify Password:</label>
                    </td>
                    <td>
                        <input type="password" name="vpass" />
                        <span class="error">{passv_err}</span>
                    </td>
                </tr>
                <tr>
                    <td>
                        <label>Email:</label>
                    </td>
                    <td>
                        <input type="email" name="email" />
                        <span class="error">{email_err}</span>
                    </td>
                </tr>
            </tbody>
        </table>
            <input type="submit" name="submit" value="Sign Up" />
    </form>
    </body>
</html>
"""

@app.route("/")
def display_form():
    return form.format(user='', name_err='', password = '', password_err='', vpass = '', passv_err='', email = '', email_err='')

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

    if len(user) > 20 or len(user) < 3:
        name_err = 'Your user name does not fit the parameters'
        user = ''
    
    if len(password) > 20 or len(password) < 3:
        password_err =  'Your password does not fit the parameters'
        password = ''

    if len(passv) > 20 or len(passv) < 3:
        passv_err = 'Your verification does not fit the parameters'
        passv = ''
    if password != passv:
        passv_err = 'Your password and verification do not match'

    else:
        return 'Welcome,' + user

app.run()