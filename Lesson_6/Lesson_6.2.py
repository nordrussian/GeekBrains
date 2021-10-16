class Road:
    
    def __init__(self, lenght, width):
        self._lengt = lenght
        self._width = width

    def get_weight(self, spec_grav, thick):
        return self._width * self._lengt * spec_grav * thick / 1000
        
r = Road(10000, 30)
print(r.get_weight(25, 5))