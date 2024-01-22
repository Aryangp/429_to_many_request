from flask import Flask , request,abort,redirect,url_for
from markupsafe import escape

app= Flask(__name__)

@app.route("/<name>")
def hello_world(name):
    return f"Hello, {escape(name)}!"

# convertor types are string , int , float , path , uuid
@app.route("/itemno/<int:no>")
def item_no(no):
    return f"item no , {escape(no)}!"

@app.route("/error")
def item_no(no):
    abort(401)
    return f"there is error"