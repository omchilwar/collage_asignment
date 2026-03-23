class vehicle:
    def move(self):
        print("the vheicle is moving")

class Car(vehicle):
 def move(self):
   print("Driving on the road")


class Bicycle(vehicle):
 def move(self):
  print("Pedaling on the road")        


vehicles = [Car(), Bicycle()]

for v in vehicles:
 v.move()