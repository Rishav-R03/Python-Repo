class Animal:
    def __init__(self,name,type):
        self.name = name
        self.type = type
    def display(self):
        print("I am {}".format(self.name),"and I am a {}".format(self.type))

animal1 = Animal("Parrot","Bird")
animal2 = Animal("Snake","Reptile")
animal3 = Animal("Cow","Mammal")

animal1.display()
animal2.display()
animal3.display()