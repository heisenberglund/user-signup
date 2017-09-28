import html
from flask import Flask, request, redirect
import os 
#import cgi
#import jinja2

#template_dir = os.path.join(os.path.dirname(__file__), 'templates')
#jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape=True)

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!doctype html>

<link rel="stylesheet" type="text/css" href="style.css" />
    <html>
        <header>
            <h1>User Signup</h1>
        </header>
        <body>
            <form action="/signup">
            <label>Name:</label>
                <br>
            <input name="name" type="text" />
                <br>
            <label>Password:</label>
                <br>
            <input name="password" type="password" />
                <br>
            <label>Verify Password:</label>
                <br>
            <input name="passv" type="password" />
                <br>
            <label>Email:</label>
                <br>
            <input name="email" type="email" />
                <br>
            <input name="submit" type="submit" value="Sign Up" />
            </form>
        </body>
    </html>
    """




@app.route('/signup')
def index():
    #template = jinja_env.get_template('home.html')
    #return template.render
    user_name = request.form['name']
    password = request.form['password']
    passv = request.form['passv']
    email = request.form['email']
    name_err = ''
    password_err = ''
    passv_err = ''
    email_err = ''

    #if len(user_name) < 3 or len(user_name) > 15:
        #return 'Your user name does not fit in parameters'
        #user_name = ''

    #if len(password) < 3 or len(password) > 15:
        #return 'Your password does not fit the parameters'
        #password = ''

    #if len(passv) < 3 or len(passv) > 15:
        #return 'Your verification does not fit the parameters'
        #passv = ''

    #if passv != password:
        #return 'Your password and verification do not match'

    #else:
        #return 'Welcome to the website' + user_name


@app.route('/')
def redir():
    return redirect('/signup')

app.run()