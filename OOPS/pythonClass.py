class dog:
    att1 = "mammal" # create instance of 

    def __init__(self,name):
        self.name = name

Rodger = dog("Rodger")
Tommy  = dog("Tommy")

print("Rodger is a {}".format(Rodger.__class__.att1))
print("Tommy is also a  {}".format(Rodger.__class__.att1))

print("My name is {}".format(Rodger.name))
print("My name is {}".format(Tommy.name))