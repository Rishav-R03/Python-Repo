# item1 = "Phone"
# item_price = 10
# item_quantity = 10
# item_price_total = 100

# print(type(item1))
# print(type(item_price))
# print(type(item_quantity))
# print(type(item_price_total))

class Item: # creating class

    def __init__(self) -> None: # constructor 
        print("Hello I am created like that")
    # pass
    def cal_total(self,x,y): # method
        return x * y

item1 = Item()
# creating attributes
item1.name = "Phone"
item1.price = 100
item1.quantity = 50
# total = item1.cal_total(item1.price,item1.quantity)
# print(total)

item2 = Item()
# creating attributes
item2.name = "Laptop"
item2.price = 1000
item2.quantity = 10
# print(type(item2))

# total1 = item2.cal_total(item2.price,item2.quantity)
# print(total1)