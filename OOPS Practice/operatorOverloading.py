class Mango:
    def __init__(self,x):
        self.x = str(x)
    def __add__(self,y):
        return self.x + y.x

ob1 = Mango(7)
ob2 = Mango('mongoes')
print(ob1+ob2)
