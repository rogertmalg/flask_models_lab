from app import app

@app.route('/orders')
def orders():
    return "Orders"