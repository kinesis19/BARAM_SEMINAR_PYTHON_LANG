class Circle:
    
    def __init__(self, radius):
        self._radius = radius
        
    def get_radius(self):
        return self._radius
    
    def set_radius(self, radius):
        self._radius = radius
    
circle = Circle(5)
print(circle.get_radius())

circle = Circle(7)
print(circle.get_radius())