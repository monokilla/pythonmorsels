import math

class Cirlce:
    def __init__(self,radius=1):
        self.radius = radius
    
    def __repr__(self):
        return f"Circle({self.radius})"
    
    @property
    def radius(self):
        return self._radius

        
    @property
    def diameter(self):
        return self.radius * 2
    @property
    def area(self):
        return (self.radius**2)*math.pi


    @diameter.setter
    def diameter(self, diameter):
        self.radius = diameter / 2
    
    @radius.setter
    def radius(self, radius):
        if radius < 0:
            raise ValueError("Radius cannot be negative")
        self._radius = radius




c = Cirlce(1)
c.diameter=4
print(c.radius)
