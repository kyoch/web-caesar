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
                        background-color:#eee;
                        padding: 20px;
                        margin: 0 auto;
                        width: 540px;
                        font: 10px san-serif;
                        border-radius:10px;
                    }}
                    textarea {{
                        margin: 10px 0;
                        width: 540px;
                        height: 120px;
                    }}
                </style>
            </head>
            <body>
                <form action = "/" method="post">
                    <label for = "rot">
                            Rotate by:
                    </label>
                    <input type = "text" name = "rot" id = "rot" value = "0">
                    <p>    
                    <textarea type ="text" name = "text" id ="text">{0}</textarea>
                    <input type = "submit" value = "Submit Query">
                </form>

            </body>
        </html>
        """                

@app.route("/")
def index():
        return form.format("")

@app.route("/", methods=['POST'])
def encrypt():
    rot_amt = request.form["rot"]
    text_to_convert = request.form["text"]
    
    encrypted = rotate_string(text_to_convert, int(rot_amt));
    encrypted_element = "<h1>" + encrypted + "</h1>"

    content= """
    <!DOCTYPE = html>
    <html>
        <head>
            <title>Web Caesar</title>
        </head>
        <body>
        """ + encrypted_element + """
        </body>
    </html>
    """
    return form.format(encrypted) 

app.run()

