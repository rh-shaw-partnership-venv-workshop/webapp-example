from flask import Flask
import requests
import base64
import io

app = Flask(__name__)

@app.route("/")
def hello_world():
    resp = requests.get("https://cataas.com/cat/says/hello%20world", stream=True)
    resp.raise_for_status()
    img_io = io.BytesIO(resp.content)
    data = base64.b64encode(img_io.getbuffer()).decode("ascii")
    img = f'<img src="data:image/png;base64,{data}" alt="A cat" height="240px" width="300px">'
    return f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
    <meta charset="UTF-8">
    <title>Hello World!</title>
    </head>
    <body>
    <h1>Hello World!</h1>
     <center><h3>A cat</h3>{img}</center>
    </body>
    </html>
    """
