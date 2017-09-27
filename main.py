from flask import Flask, request, render_template, redirect
import os
import jinja2

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape=True)



app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/signup', methods=['POST'])
def index():
    template = jinja_env.get_template('home.html')
    return template.render
    user_name = request.home['name']
    password = request.home['password']
    passv = request.home['passv']
    email = request.home['email']
    name_err = ''
    password_err = ''
    passv_err = ''
    email_err = ''

    if len user_name < 3 or len user_name > 15:
        return 'Your user name does not fit in parameters'
        user_name = ''

    elif len password < 3 or len password > 15:
        return 'Your password does not fit the parameters'
        password = ''

    elif len passv < 3 or len passv > 15:
        return 'Your verification does not fit the parameters'
        passv = ''

    elif passv != password:
        return 'Your user and password do not match'

    else:
        return 'Welcome to the website' + user_name


@app.route('/')
def redir():
    return redirect('/signup')

app.run()