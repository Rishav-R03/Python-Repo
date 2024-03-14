from abc import ABC, abstractmethod

class AbstractAnimal(ABC):
    @abstractmethod
    def speak(self):
        pass
class dog(AbstractAnimal):
    def speak(self):
        return "woof woof!"
# you can not instantiate an AbstractAnimal
# animal = AbstractAnimal()  --> this will type a TypeError

Dog = dog()
print(Dog.speak())