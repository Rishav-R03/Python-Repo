class Animal(object):
    def __init__(self,name,kind) :
        self.name = name
        self.kind = kind
    def display(self):
        print("I am {}".format(self.name),"and I am a {}".format(self.kind))

class Dog(Animal):
    def __init__(self,name,kind,sound):
        self.sound = sound
        Animal.__init__(self,name,kind)
    def details(self):
        print("I am {}".format(self.name),"I am a ".format(self.kind),"and I sound ".format(self.sound))

animal1 = Dog("Dog","Mammal","Bark")
animal2 = Dog("Snake","Reptile","Hiss")
animal3 = Dog("Cockroach","Insect","None")

animal1.display()
animal2.display()
animal3.display()


animal1.details()
animal2.details()
animal3.details()