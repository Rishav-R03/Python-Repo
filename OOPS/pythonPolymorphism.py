class bird:
    def intro(self):
        print("There are many types of birds")
    def flight(self):
        print("Most of the birds can fly but some cannot ")
    
class sparrow(bird):
    def flight(self):
        print("Sparrow can fly ")
    
class ostrich(bird):
    def flight(self):
        print("Ostrich cannot fly")

obj_bird = bird()
obj_spr = sparrow()
obj_os = ostrich()

obj_bird.intro()
obj_bird.flight()

obj_spr.intro()
obj_spr.flight()

obj_os.intro()
obj_os.flight()