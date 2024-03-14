class Pizza(object):
    def __init__(self): # constructors in python
        self.toppings = []
    def __call__(self,topping): # method used to write classes where instances behave like function
        # when using '@instance_of_pizza' before function defination
        # the function gets passed onto 'topping'.
        self.toppings.append(topping())
    def __repr__(self): # python repr function return printable representation of an object in form of string
        return str(self.toppings)
pizza = Pizza()

@pizza 
def cheese():
    return 'cheese'
@pizza 
def sauce():
    return 'sauce'

print(pizza)
