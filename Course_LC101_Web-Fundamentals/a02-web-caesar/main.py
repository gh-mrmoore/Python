from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True


form = """
<!DOCTYPE html>

<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
        <form method="post">
        <label for="rot">Rotate by:</label>
        <input name="rot" id="rot" type="text" value="0" />
        <textarea cols="20" name="text" id="text" rows="2">{0}</textarea>
        <input type="submit" value="Encrypt!" />
        </form>

    </body>
</html>
"""

@app.route("/", methods=['POST'])
def encrypt():
    rotation = int(request.form['rot'])
    message = str(request.form['text'])

    encrypted_result = rotate_string(message, rotation)

    return form.format(encrypted_result)

@app.route("/")
def index():
    blank = ''
    #form = form.format(blank)
    
    return form.format(blank)

app.run()