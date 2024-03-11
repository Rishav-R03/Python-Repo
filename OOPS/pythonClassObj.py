class Dog:
    att1 = "mammal"

    def __init__(self,name):
        self.name = name
    def speak(self):
        print("My name is {}".format(self.name))

Rodger_ob = Dog("Rodger") # Rodger_ob is object of Dog class
Horse_ob = Dog("Horse") # Horse_ob is a object of Dog class

Rodger_ob.speak()
Horse_ob.speak()