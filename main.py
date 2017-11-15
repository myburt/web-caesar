from flask import Flask, request
from caesar import rotate_string
import cgi

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>

<html>
    <head>
        <style>
            form 
            {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea 
            {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
      <form action="" method="POST">
        <label>Rotate by:
            <input type="text" name="rot" value="0" />
        </label>
        <p><textarea name="text">{txt_area_text}</textarea></p>
        
        <input type="submit" value="Submit Query" />
      </form>
    </body>
</html>
"""

@app.route("/")
def index():
    return form.format(txt_area_text = '')

def is_integer(num):
    try:
        int(num)
        return True
    except ValueError:
        return False

@app.route("/", methods = ['POST'])
def encrypt():
    message = request.form['text']
    rotator = request.form['rot']

    if is_integer(rotator):
        rotator = int(rotator)
        encrypted_text = rotate_string(message, rotator)
        encrypted_text = cgi.escape(encrypted_text)
        return form.format(txt_area_text = encrypted_text)
    else: 
        return form.format(txt_area_text = cgi.escape(rotator + " is not a number please change yourRotate by:")) 

app.run()