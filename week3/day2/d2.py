class Shape:
  sides = 4 #first property
  name = "Square" #second property
  def description(a): #method defined
    return ("A square with 4 sides")

s1 = Shape() #creating an object of Shape
print ("Name of shape is:",s1.name)
print ("Number of sides are:",s1.sides)
print (s1.description())