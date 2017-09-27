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
    name = request.home['name']
    password = request.home['password']
    passv = request.home['passv']
    email = request.home['email']
    name_err = ''
    password_err = ''
    passv_err = ''
    email_err = ''
    

@app.route('/')
def redir():
    return redirect('/signup')

app.run()