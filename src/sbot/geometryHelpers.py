from classes import Point
from math import sqrt

#Вычисление расстояния между двумя точками
def calculate_dest(first : Point, second : Point) -> float:
    return sqrt(
            (first.x - second.x) ** 2 + (first.y - second.y) ** 2
        )