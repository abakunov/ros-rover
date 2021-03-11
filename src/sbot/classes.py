from geometryHelpers import calculate_dest

#Класс точки  
class Point():
    
    def __init__(self, x : int , y : int) :
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return "Point: x = "+str(self.x)+"; y = "+str(self.y)
    
    def __sub__(self, other) -> float:
        return calculate_dest(self, other)

#класс позиции робота вместе с поворотом
class Position():
    pass