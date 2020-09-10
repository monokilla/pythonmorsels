import math

class Cirlce:
    def __init__(self,radius=1):
        self.radius = radius
    
    def __repr__(self):
        return f"Circle({self.radius})"
    @property
    def diameter(self):
        return self.radius * 2
    @property    
    def area(self):
        return (self.radius**2)*math.pi

    
    
    




c = Cirlce(4)
c.radius=1

print(c.area)
print(c.diameter)
print(c)