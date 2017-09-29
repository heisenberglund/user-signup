from flask import Flask, request, redirect
import os
import cgi
import jinja2

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
            .table{{
                font-family: helvetica;
            }}
            #headline{{font-family: helvetica; 
            color: green
            }}
        </style>
    </head>

    <body>
        <h1 id="headline">User Signup</h1>
    <form method='POST'>
        <table class="table">
            <tbody>
                <tr>
                    <td>
                        <label>User Name:</label>
                    </td>
                    <td>
                        <input type="text" value='{user}' name="user-name" />
                        <span class="error">{name_err}</span>
                    </td>
                </tr>
                <tr>
                    <td>
                        <label>Password:</label>
                    </td>
                    <td>
                        <input type="password" value='{password}' name="password" />
                        <span class="error">{password_err}</span>
                    </td>
                </tr>
                <tr>
                    <td>
                        <label> Verify Password:</label>
                    </td>
                    <td>
                        <input type="password" value='{vpass}' name="vpass" />
                        <span class="error">{vpass_err}</span>
                        
                    </td>
                </tr>
                <tr>
                    <td>
                        <label>Email:</label>
                    </td>
                    <td>
                        <input type="text" value='{email}' name="email" />
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
    return form.format(user='', name_err='', password = '', password_err='', vpass = '', vpass_err='', email = '', email_err='')

@app.route("/", methods=['POST'])
def user_signup():
    user = request.form['user-name']
    password = request.form['password']
    vpass = request.form['vpass']
    email = request.form['email']
    name_err = ''
    password_err = ''
    vpass_err = ''
    email_err = ''

    if email is None:
        email = email

        if '@' not in email:
            email_err = 'Your e-mail is not valid'
            email = ''
    
        if '.' not in email:
            email_err = 'Your e-mail is not valid'
            email = ''


    if len(user) > 20 or len(user) < 3:
        name_err = 'Your user name does not fit the parameters'
        user = ''
    
    if len(password) > 20 or len(password) < 3:
        password_err =  'Your password does not fit the parameters'
        password = ''

    if len(vpass) > 20 or len(vpass) < 3:
        vpass_err = 'Your verification does not fit the parameters'
        vpass = ''
    
    if password != vpass:
        vpass_err = 'Your password and verification do not match'
        vpass = ''
    
    if not name_err and not password_err and not vpass_err and not email_err:
        user = user
        return redirect('/completed-signup?user={0}'.format(user))        

    else:
        return form.format(user=user, name_err=name_err,
        password=password, password_err=password_err,
        vpass=vpass, vpass_err=vpass_err, 
        email=email, email_err=email_err)

@app.route('/completed-signup')
def completed_signup():
    user = request.args.get('user')
    return '<h1>Welcome to the site {0}</h1>'.format(user)


app.run()