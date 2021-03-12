from geometryHelpers import calculate_dist

#Класс точки  
class Point():
    
    def __init__(self, x : float , y : float) :
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return "Point: x = "+str(self.x)+"; y = "+str(self.y)
    
    def __eq__(self, other) -> bool:

        if self.x == other.x and self.y == other.y:
            return True
        
        return False

    def __sub__(self, other) -> float:
        return calculate_dist(self, other)

#класс позиции робота вместе с поворотом
class Position():
    pass