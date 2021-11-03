from app import app
from flask import render_template
from models.orders import *

@app.route('/orders')
def orders():
    # print(orders)
    # print(orders.order1)
    return render_template("index.html", title="Orders", orders=orders_list)

@app.route('/orders/<index>')
def order(index):
    return render_template("order.html", title="Order", order=orders_list[int(index)])