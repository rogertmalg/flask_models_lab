from app import app
from flask import render_template

@app.route('/orders')
def orders():
    return render_template("index.html", title="Orders")