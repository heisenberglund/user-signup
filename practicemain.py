from flask import Flask, request, redirect
import os
import cgi

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!doctype html>
<html>
    <body>
    <form>
        <label>User Name:
            <input type="text" name="user-name" />
        </label>
            <br>
        <label>Password:
            <input type="password" name="password" />
        </label>
            <br>
        <label> Verify Password:
            <input type="password name="password" />
        </label>
            <br>
        <label>Email:
            <input type="email name="email />
        </label>
    </form>
    </body>
</html>
"""

@app.route("/")
def index():
    return form

app.run()