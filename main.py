from flask import Flask, request, render_template, redirect
import cgi
import os
import jinja2

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape=True)



app =  Flask(__name__)
app.config['DEBUG'] = True

@app.route('/signup')

@app.route('/')
def redir():
    return redirect('/signup')

app.run()