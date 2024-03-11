
# creating a base class
# __ double underscore represents private attribute
class Base:
    def __init__(self):
        self.a = "GeekforGeeks"
        self.__c = "GeekforGeeks"

class Derived(Base):
    def __init__(self):
        # calling constructor of base class
        Base.__init__(self)
        print("Calling private member of base class")
        print(self.__c)
ob1 = Base()
print(ob1.a)