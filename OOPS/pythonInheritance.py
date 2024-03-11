class Person(object):
    def __init__(self,name,idNo):
        self.name = name
        self.idNo = idNo
    def display(self):
        print(self.name)
        print(self.idNo)
    def details(self):
        print("My name is {}".format(self.name))
        print("My id is {}".format(self.idNo))

class Employee(Person):
    def __init__(self, name, idNo,salary,post):
        self.salary = salary
        self.post = post
        Person.__init__(self,name, idNo) # invoking the __init__ of parent class
    def details(self):
        print("My name is {}".format(self.name))
        print("My name is {}".format(self.idNo))
        print("My salary is {}".format(self.salary))
        print("My post is {}".format(self.post))
a = Employee('Rahul',886012,200000000,"Intern")

a.display()        
a.details()        