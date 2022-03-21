#Create a Class with instance attributes

------------------------------------------


class cal :
  def __init__(self,a,b):
    self.speed=a
    self.milage=b
    print("hi")
    self.po()

  def po(self):
    print("kiii {} is speed and {} is millage".format(self.speed,self.milage))

hi=cal(22,3)
print(hi.speed,hi.milage)
hi.po()

  -----------------------------------
 #       Output:
 #         hi
 #         kiii 22 is speed and 3 is millage
 #         22 3
 #         kiii 22 is speed and 3 is millage
