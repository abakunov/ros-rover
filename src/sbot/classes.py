from geometryHelpers import calculate_dist, quaternion_to_theta
import math

#Ориентация в квантерионах
class QuantPos:

    x : float
    y : float
    z : float
    w : float


    def __init__(self, z : float = 0 , w : float = 0 , x : float = 0, y : float  = 0):
        self.w = w
        self.z = z
        self.x = x
        self.y = y

    def __sub__(self, other):
        return (self.toTheta() - other.toTheta())%360
    
    def toTheta(self):
        return quaternion_to_theta(self)

    def __repr__(self):
        return "quant:"+str(self.x)+str(self.y)+str(self.z)+str(self.w)+"\n deg:"+str(self.toTheta())


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

#класс позиции робота вместе с углом поворота
class Position(Point):
    
    theta : QuantPos

    def __init__(self, theta : QuantPos, *args, **kwargs):
        self.theta = theta
        super(Position, self).__init__(*args,**kwargs)

    def __repr__(self):
        return super(Position,self).__repr__()+"\n"+self.theta.__repr__()