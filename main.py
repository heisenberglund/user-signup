from flask import Flask, request, redirect
import os
import cgi
import jinja2

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader (template_dir))


app = Flask(__name__)
app.config['DEBUG'] = True



@app.route("/")
def display_form():
    template = jinja_env.get_template('homepage.html')
    return template.render(user='', name_err='', password = '', password_err='', vpass = '', vpass_err='', email = '', email_err='')

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
    template = jinja_env.get_template('request.html')

    if email is None:
        email = email

    if '@' not in email:
        email_err = 'Your e-mail is not valid'
        email = ''
    
    if '.' not in email:
        email_err = 'Your e-mail is not valid'
        email = ''


    if len(user) > 20 or len(user) < 4:
        name_err = 'Your user name does not fit the parameters'
        user = ''
    
    if len(password) > 20 or len(password) < 4:
        password_err =  'Your password does not fit the parameters'
        password = ''

    if len(vpass) > 20 or len(vpass) < 4:
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