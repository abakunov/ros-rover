from classes import Point
from math import sqrt

#Вычисление расстояния между двумя точками
def calculate_dist(first : Point, second : Point) -> float:
    return sqrt(
            (first.x - second.x) ** 2 + (first.y - second.y) ** 2
        )