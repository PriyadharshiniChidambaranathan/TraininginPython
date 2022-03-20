import math

pi=math.pi
def circle(radius):
  return pi*(radius**2)

def cube(side):
  return 6*side*side

def sphere(radius):
  return 2*pi*(radius**2)

def cyclinder(radius,height):
  return 2*pi*radius + 2*pi*height


print("circle area is:{}" .format(circle(2)))
print("cude area is :{}".format(cube(3)))




--------------------------------
#output:
#       circle area is:12.566370614359172
#       cude area is :54
