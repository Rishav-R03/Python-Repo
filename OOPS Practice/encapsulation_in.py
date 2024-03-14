class MyClass:
    def __init__(self):
        self.public = "Public"
        self._protected = "Protected" # single underscore means protected
        self.__private = "Private" # double underscore means private
obj = MyClass() 
print(obj.public)
print(obj._protected)
print(obj.__private) # this will raise attribute error