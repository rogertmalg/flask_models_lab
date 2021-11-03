from models.order import *
import datetime

order1 = Order("Charlie", datetime.date(2021, 11, 3), "1", "Banana")
order2 = Order("Ana", datetime.date(2021, 11, 1), "3", "Traffic")

orders_list = [order1, order2]
