from collections import namedtuple, defaultdict
from pprint import pprint
from csv import reader

def get_orders():
    orders = list([])
    with open("data/OrderItems.csv") as f:
        read = reader(f)
        Order = namedtuple("Order", next(read))
        for line in read:
            orders.append(Order(*line))
    return orders

def get_dict(orders):
    res = defaultdict(lambda: 0)
    for order in orders:
        res[order.ProductID] += int(order.Quantity)
    return res

def main():
    orders = get_orders()
    inventory = get_dict(orders)
    pprint(dict(inventory))


if __name__ == "__main__":
    main()