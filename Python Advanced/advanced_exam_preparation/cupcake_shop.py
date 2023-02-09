def stock_availability(*args):
    in_stock, action, *flavours = args
    flavours = [int(x) if type(x) == int else x for x in flavours]

    if action == "delivery":
        [in_stock.append(x) for x in flavours]

    elif in_stock:
        if not flavours: in_stock.pop(0)
        elif type(flavours[0]) == int: in_stock = in_stock[flavours[0]:]
        else: in_stock = [x for x in in_stock if x not in flavours]

    return in_stock


print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie","banana"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))