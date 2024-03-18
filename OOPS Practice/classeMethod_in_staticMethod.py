class myClass:
    @classmethod
    def class_method(cls):
        return "Class method called"
    @staticmethod
    def static_method():
        return "static method called"
print(myClass.class_method())
print(myClass.static_method())