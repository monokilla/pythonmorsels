import math

class Cirlce:
    def __init__(self,r=1):
        self.r = r
    
    def __repr__(self):
        return f"Circle({self.r})"

    
    def radius(self):
        return self.r

    @property
    def diameter(self):
        return self.r * 2
    @property    
    def area(self):
        return (self.r**2)*math.pi
    
    




c = Cirlce(4)
c.radius=1
print(c.area)
print(c.diameter)
print(c)